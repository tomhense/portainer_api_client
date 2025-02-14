import os.path
from enum import Enum
from pathlib import Path

import swagger_client


class PortainerApiClient:
    class StackStatus(Enum):
        RUNNING = 1
        STOPPED = 2

    def __init__(self, url: str, verify_ssl: bool = True):
        self.client = swagger_client.ApiClient()
        self.stacks_api = swagger_client.StacksApi(self.client)
        self.backup_api = swagger_client.BackupApi(self.client)
        self.auth_api = swagger_client.AuthApi(self.client)
        self.url = url
        self.verify_ssl = verify_ssl

    def _reauthenticate_user(
        self,
        username: str,
        password: str,
    ):
        self.auth_api.api_client.configuration.host = self.url
        self.auth_api.api_client.configuration.verify_ssl = self.verify_ssl
        response = self.auth_api.authenticate_user({"username": username, "password": password})
        token = response.jwt
        self.client.set_default_header("Authorization", f"Bearer {token}")
        return token

    def _get_xdg_cache_home(self) -> Path:
        # Cross platform XDG compliant config location detection
        XDG_CONFIG_HOME = os.getenv("XDG_CACHE_HOME")
        if XDG_CONFIG_HOME is None:
            XDG_CONFIG_HOME = "~/.cache"
        return Path(os.path.expanduser(XDG_CONFIG_HOME))

    def authenticate_user(self, username: str, password: str):
        JWT_TOKEN_PATH = self._get_xdg_cache_home() / Path("portainer_jwt_token")
        jwt_token = None
        if JWT_TOKEN_PATH.exists():
            with open(JWT_TOKEN_PATH, "r") as f:
                jwt_token = f.read()

        if jwt_token is None or not self.auth_api.validate_o_auth({"jwt": jwt_token}):
            jwt_token = self._reauthenticate_user(username, password)
            assert jwt_token is not None
            with open(JWT_TOKEN_PATH, "w") as f:
                f.write(jwt_token)

    def get_stacks(self):
        stacks = self.stacks_api.stack_list()
        return stacks

    def stop_stack(self, stack):
        self.stacks_api.stack_stop(stack.id, stack.endpoint_id)

    def start_stack(self, stack):
        self.stacks_api.stack_start(stack.id, stack.endpoint_id)

    def backup(self, destination: Path, password: str | None = None):
        if password is None:
            backup = self.backup_api.backup()
        else:
            backup = self.backup_api.backup(password=password)

        with open(destination, "wb") as f:
            f.write(backup)
            f.write(backup)

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
        self.url = url.rstrip("/") + "/api"
        self.verify_ssl = verify_ssl
        print(f"URL: {self.url}, Verify SSL: {self.verify_ssl}")

    def authenticate_user(
        self,
        username: str,
        password: str,
    ):
        # The token is only valid for 8 hours, so there is no need to store it
        self.auth_api.api_client.configuration.host = self.url
        self.auth_api.api_client.configuration.verify_ssl = self.verify_ssl
        response = self.auth_api.authenticate_user({"username": username, "password": password})
        jwt_token = response.jwt
        self.client.set_default_header("Authorization", f"Bearer {jwt_token}")

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

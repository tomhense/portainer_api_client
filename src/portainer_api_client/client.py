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

    def authenticate_user(
        self,
        username: str,
        password: str,
    ):
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
        body = {"password": password} if password else None
        resp = self.backup_api.backup(_preload_content=False, body=body)

        with open(destination, "wb") as f:
            f.write(resp.data)

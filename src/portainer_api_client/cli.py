import argparse
import configparser
import os.path
from pathlib import Path

from portainer_api_client.client import PortainerApiClient


def stacks_action(client, args):
    if args.action == "start-all":
        for stack in client.get_stacks():
            if stack.status == PortainerApiClient.StackStatus.STOPPED.value:
                print(f"Starting {stack.name}")
                client.start_stack(stack)

    elif args.action == "stop-all":
        for stack in client.get_stacks():
            if stack.status == PortainerApiClient.StackStatus.RUNNING.value:
                print(f"Stopping {stack.name}")
                client.stop_stack(stack)

    elif args.action == "list":
        for stack in client.get_stacks():
            stack_status = PortainerApiClient.StackStatus(stack.status).name
            print(f"{stack.name}\t{stack_status}")


def backup_action(client, args):
    if args.action == "create":
        backup_path = Path(args.destination)
        client.backup(backup_path, args.password)


def get_xdg_config_home() -> Path:
    # Cross platform XDG compliant config location detection
    XDG_CONFIG_HOME = os.getenv("XDG_CONFIG_HOME")
    if XDG_CONFIG_HOME is None:
        XDG_CONFIG_HOME = "~/.config"
    return Path(os.path.expanduser(XDG_CONFIG_HOME))


def get_config(config_path: str | None = None) -> configparser.ConfigParser:
    if config_path is not None:
        config = configparser.ConfigParser()
        config.read(config_path)
        return config
    else:
        possible_config_paths = [
            Path("/etc/portainer-api-client/config.conf"),
            get_xdg_config_home() / Path("portainer-api-client.conf"),
        ]
        config = configparser.ConfigParser()
        for path in possible_config_paths:
            if path.exists():
                config.read(path)
                return config
        raise FileNotFoundError("Configuration file not found")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config", "-c", help="Path to the configuration file", required=False, default=None, dest="config_path"
    )
    subparsers = parser.add_subparsers(dest="subparser_name", required=True)

    stack_subparser = subparsers.add_parser("stacks")
    stack_subparser.add_argument("action", help="Action to perform", choices=["start-all", "stop-all", "list"])
    stack_subparser.set_defaults(func=stacks_action)

    backup_subparser = subparsers.add_parser("backups")
    backup_subparser.add_argument("action", help="Action to perform", choices=["create"])
    backup_subparser.add_argument("--password", help="Password to encrypt the backup", required=False, default=None)
    backup_subparser.add_argument("destination", help="Destination of the backup")
    backup_subparser.set_defaults(func=backup_action)

    args = parser.parse_args()

    config = get_config(args.config_path)
    assert config.has_option("host", "url")
    assert config.has_option("admin", "username")
    assert config.has_option("admin", "password")

    client = PortainerApiClient(config["host"]["url"], config["host"].getboolean("verify_ssl", True))
    client.authenticate_user(config["admin"]["username"], config["admin"]["password"])

    args.func(client, args)


if __name__ == "__main__":
    main()

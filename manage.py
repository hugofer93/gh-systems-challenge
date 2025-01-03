#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from django.core.management.commands.runserver import Command as RunServerCommand
from dotenv import load_dotenv


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ghsystems.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def change_runserver_default_port():
    """Change the default port of the runserver command."""
    HOST_PORT = os.environ.get('HOST_PORT')
    RunServerCommand.default_port = HOST_PORT


if __name__ == '__main__':
    change_runserver_default_port()
    main()

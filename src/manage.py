import logging
import subprocess
from pathlib import Path
from typing import Sequence, Type, Union

import click

from containers import AppContainer

BASE_DIR = Path(__file__).resolve().parent
logger = logging.getLogger(__name__)


@click.group("App manager")
def manage():
    container = AppContainer()
    logger.info('wire')
    container.wire(modules=[__name__])


@manage.command('makemigrations')
@click.option('-m', '--message')
def makemigrations(message):
    if not message:
        return click.BadParameter('message is required')

    subprocess.run(['alembic', 'revision', '--autogenerate', '-m', message])


@manage.command('migrate')
def migrate():
    subprocess.run(['alembic', 'upgrade', 'head'])

# -*- coding: utf-8 -*-
import os

import click
from flask.cli import with_appcontext
from desafio.extensions import db


HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(HERE, os.pardir)
TEST_PATH = os.path.join(PROJECT_ROOT, 'tests')


@click.command("init-db")
@with_appcontext
def init_db_command():
    db.drop_all()
    db.create_all()
    """Clear existing data and create new tables."""
    click.echo("Initialized the database.")


@click.command()
def test():
    """Run the tests."""
    import pytest
    rv = pytest.main([TEST_PATH, '--verbose'])
    exit(rv)
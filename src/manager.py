#!/usr/bin/env python
# coding: utf-8

"""
    manage
    ~~~~~~

    Set of some useful management commands.
"""

import subprocess
from flask.ext.script import Shell, Manager, Server
from application import app
from application import mongo

manager = Manager(app)

@manager.command
def clean_pyc():
    """Removes all *pyc files from the project folder"""
    clean_command = "find . -name *.pyc -delete".split()
    subprocess.call(clean_command)

manager.add_command("shell", Shell(make_context=lambda: {"app": app, "mongo": mongo}))
manager.add_command("runserver", Server(host="0.0.0.0", port=app.config['PORT']))

if __name__ == "__main__":
    manager.run()

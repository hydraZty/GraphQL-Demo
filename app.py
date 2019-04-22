#!/usr/bin/env python

from flask import Flask

from database import db_session, init_db

app = Flask(__name__)
app.debug = True


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    init_db()
    app.run()

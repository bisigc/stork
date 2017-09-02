import os
import controller/dbController
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
	DATABASE=os.path.join(app.root_path, 'stork.db'),
	SECRET_KEY='development key',
	USERNAME='admin',
	PASSWORD='default'
	)
)

# Load additional (or overwrite) configuration from a file set in the env variable STORK SETTINGS. If not sent, no exception will be thrown (silent)
app.config.from_envvar('STORK_SETTINGS', silent=True)


@app.route("/")
def index():
    return render_template('index.html')


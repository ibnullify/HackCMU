from flask import Flask, url_for, render_template, request, session, flash, redirect
from os import path
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

DIR = path.dirname(__file__)
@app.route('/')
def root():
    return render_template('homepage.html')


@app.route('/analyzing_album', methods=['GET'])
def analyzing_album():
    return render_template('analyze.html')



if __name__ == '__main__':
    app.debug = True #DANGER DANGER! Set to FALSE before deployment!
    app.run()

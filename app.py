from flask import Flask, url_for, render_template, request, session, flash, redirect
from os import path
import os
import subprocess

app = Flask(__name__)
app.secret_key = os.urandom(32)


UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
DIR = path.dirname(__file__)
@app.route('/')
def root():
    return render_template('index.html')


@app.route('/analyzing_album', methods=['GET','POST'])
def analyzing_album():
    #return render_template('analyze.html')
    result = request.form
    file = request.files['pic']
    url = result['url']
    print url, file
    
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
    file.save(f)

    album_id = get_flickr_albumid(url)
    print album_id
    #url = request.form["url"]

    generate_urls_from_album(album_id)
    run_clarifai()
    
    return render_template('temp.html', result = result)


def get_flickr_albumid( url ):
    if (url.endswith("/")):
        url = url[:len(url) - 1]
    arr = []
    arr.append(url.rfind("/"))
    arr.append(url.rfind("-"))
    arr.append(url.rfind("_"))

    return url[max(arr) + 1:]


def generate_urls_from_album( album_id):
    f = open("urls.txt", "w")
    subprocess.call(["python", "flickrpy/trunk/photos_for_pool.py", album_id], stdout = f)
    f.close()

def run_clarifai():
    subprocess.call(["python", "clariftest.py"])
    

if __name__ == '__main__':
    app.debug = True #DANGER DANGER! Set to FALSE before deployment!
    app.run()

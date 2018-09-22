import json

from clarifai.rest import ClarifaiApp

from math import sqrt

from numpy import linalg

from numpy import array

 

# Initalize Clarifai and get the Face Embedding model

app = ClarifaiApp(api_key='b2e8ea4c70c849079fffe4a69b1e7ff2')

model = app.models.get("d02b4508df58432fbb84e800597b8959")

 

# Dataset

kunalPhoto = "http://imageshack.com/a/img922/6780/2ceUHj.jpg"

momPhoto = "http://imageshack.com/a/img922/2448/tvuLfa.jpg"

dadPhoto = "http://imageshack.com/a/img923/1862/G1VINZ.png"

 

# Function to get embedding from image

def getEmbedding(image_url):

    # Call the Face Embedding Model

    jsonTags = model.predict_by_url(url=image_url)

 

    # Storage for all the vectors in a given photo

    faceEmbed = []

 

    # Iterate through every person and store each face embedding in an array

    for faces in jsonTags['outputs'][0]['data']['regions']:

        for face in faces['data']['embeddings']:

            embeddingVector = face['vector']

            faceEmbed.append(embeddingVector)

    return faceEmbed[0]

 

# Get embeddings and put them in an array format that Numpy can use

kunalEmbedding = array(getEmbedding(kunalPhoto))

momEmbedding = array(getEmbedding(momPhoto))

dadEmbedding = array(getEmbedding(dadPhoto))

 

# Get Distances useing Numpy

momDistance = linalg.norm(kunalEmbedding-momEmbedding)

print "Mom Distance: "+str(momDistance)

 

dadDistance = linalg.norm(kunalEmbedding-dadEmbedding)

print "Dad Distance: "+str(dadDistance)

 

# Print results

print ""

print "**************** Results are In: ******************"

if momDistance < dadDistance:

    print "Kunal looks more similar to his Mom"

elif momDistance > dadDistance:

    print "Kunal looks more similar to his Dad"

else:

    print "Kunal looks equally similar to both his mom and dad"

print ""


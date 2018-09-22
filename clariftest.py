from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

import json
from math import sqrt
from numpy import linalg
from numpy import array


app = ClarifaiApp(api_key='b2e8ea4c70c849079fffe4a69b1e7ff2')

#model = app.models.get('general-v1.3')
model = app.models.get("d02b4508df58432fbb84e800597b8959")
#image = ClImage(url='https://samples.clarifai.com/metro-north.jpg')


def getEmbedding(image_url):
    #jsonTags = model.predict([image])
    jsonTags = model.predict_by_url(url=image_url)
    faceEmbed = []

    for faces in jsonTags['outputs'][0]['data']['regions']:

        for face in faces['data']['embeddings']:

            embeddingVector = face['vector']

            faceEmbed.append(array(embeddingVector))

    return faceEmbed


#holds strings of the urls of the images we are searching through
images = ["https://c2.staticflickr.com/4/3524/5829354207_cd72fd7bba_b.jpg",
          "https://c2.staticflickr.com/8/7126/7516733842_7bc567bd29_b.jpg",
          "http://cdn01.cdn.justjared.com/wp-content/uploads/headlines/2018/09/anna-kendrick-barack-obama-asshole1.jpg",
          "https://s.abcnews.com/images/Video/GTY_barack_obama_1_jt_160803_16x9_1600.jpg"]



search_for = []
pictures_faces = []

for url in images:
    pictures_faces.append(getEmbedding(url))


search_for.append(getEmbedding("https://www.whitehouse.gov/wp-content/uploads/2017/12/44_barack_obama1.jpg"))
#print len(pictures_faces[1])

for face in search_for[0]:
    for i in range(len(pictures_faces)):
    #for picture in pictures_faces:
        for potential_face in pictures_faces[i]:
            if (linalg.norm(face - potential_face) < 1):
                print images[i]
        

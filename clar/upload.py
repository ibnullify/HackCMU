# upload.py
import os
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

app = ClarifaiApp(api_key='b2e8ea4c70c849079fffe4a69b1e7ff2')

FILE_NAME = 'food-data.txt'
FILE_PATH = os.path.join(os.path.curdir, FILE_NAME)

# Counter variables
current_batch = 0
counter = 0
batch_size = 32

with open(FILE_PATH) as data_file:
    images = [url.strip() for url in data_file]
    row_count = len(images)
    print("Total number of images:", row_count)

while(counter < row_count):
    print("Processing batch: #", (current_batch+1))
    imageList = []

    for current_index in range(counter, counter+batch_size - 1):
        try:
            imageList.append(ClImage(url=images[current_index]))
        except IndexError:
            break

    app.inputs.bulk_create_images(imageList)

    counter = counter + batch_size
    current_batch = current_batch + 1

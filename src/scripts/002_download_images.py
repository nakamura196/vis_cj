import base64
import json
import os
from PIL import Image
import sys
import urllib.request
import time
import requests
import shutil
import yaml

with open('../../.env.yml') as file:
    yml = yaml.load(file, Loader=yaml.SafeLoader)


def download_img(url, file_name):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

# path to thumbnail dir
thumb_dir = yml["thumb_dir"]

# path to curation
curation_path = "../data/src/curation.json"

count = 0

with open(curation_path) as f:
    curation = json.load(f)

    selections = curation["selections"]

    for selection in selections:
        members = selection["members"]

        for member in members:

            count += 1

            if count % 100 == 1:
                print(count)

            thumbnail = member["thumbnail"]

            id = member["id"]

            opath = thumb_dir + "/" + id + ".jpg"

            if not os.path.exists(opath):
                download_img(thumbnail, opath)

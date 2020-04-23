from collections import Counter
import json
import math
from pprint import pprint
import re
import sys
import urllib.request
import glob
import yaml
import os

with open('../../.env.yml') as file:
    yml = yaml.load(file, Loader=yaml.SafeLoader)

json_dir = yml["json_dir"]

files = glob.glob(json_dir + "/converted/*/*.json")
files = sorted(files)

selections = []

prefix = "https://nakamura196.github.io/vis_cj"

for i in range(len(files)):
    file = files[i]

    # メイン
    if i % 1000 == 0:
        print(str(i+1)+"/"+str(len(files))+"\t"+file)

    try:
        with open(file) as f:
            df = json.load(f)

            id = df["_id"]

            path = yml["thumb_dir"] + "/" + id + ".jpg"

            if not os.path.exists(path):
                continue

            images = df["image"]

            metadata = [
                {
                    "label" : "基本区分",
                    "value" : df["type_ja"][0]
                }
            ]

            value = "None"
            if len(df["source_ja"]) > 0:
                value = df["source_ja"][0]
            metadata.append({
                "label" : "収録データベース",
                "value" : value
            })

            value = "None"
            if len(df["access_ja"]) > 0:
                value = df["access_ja"][0]
            metadata.append({
                "label" : "所在（所蔵機関）",
                "value" : value
            })

            value = "None"
            if len(df["objects_ja"]) > 0:
                value = df["objects_ja"][0]
            metadata.append({
                "label" : "機械タグ",
                "value" : value
            })

            label = df["title_ja"][0]

            thumbnail = images[0]

            related = "https://cultural.jp/item/"+id

            member = {
                "@id": related,
                "id" : id,
                "@type": "sc:Canvas",
                "label": label,
                "metadata": metadata,
                "thumbnail": thumbnail,
                "related": related
            }

            members = [member]

            selection = {
                "@id": prefix + "/iiif/curation/"+id+"/range1",
                "@type": "sc:Range",
                "label": "Characters",
                "members": members,
                "within": {
                    "@id": related,
                    "@type": "sc:Manifest",
                    "label": label
                }
            }
            selections.append(selection)
    except Exception as e:
        print(file, e)


OUTPUT_FILE = "../data/src/curation.json"


curation = {
    "@context": [
        "http://iiif.io/api/presentation/2/context.json",
        "http://codh.rois.ac.jp/iiif/curation/1/context.json"
    ],
    "@id": prefix + "/iiif/curation/curation.json",
    "@type": "cr:Curation",
    "label": "Character List",
    "selections": selections
}

fw = open(OUTPUT_FILE, 'w')
json.dump(curation, fw, ensure_ascii=False, indent=4,
          sort_keys=True, separators=(',', ': '))

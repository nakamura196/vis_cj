import glob
import shutil
import os

import yaml

with open('../../.env.yml') as file:
    yml = yaml.load(file, Loader=yaml.SafeLoader)

json_dir = yml["json_dir"]

thumb_dir = json_dir.replace("/json", "/thumbnail")

files = glob.glob(thumb_dir + "/[!dignl]*/*.jpg")

for i in range(len(files)):
    file = files[i]
    if i % 1000 == 0:
        print(i+1, len(files), file)

    filename = os.path.basename(file)
    path = thumb_dir.replace("/cj", "/cj_vis") + "/" + filename


    if not os.path.exists(path):
        shutil.copyfile(file, path)
import glob
import shutil
import os

thumb_dir = "/Users/nakamura/git/thumbnail"

files = glob.glob(thumb_dir + "/cj/*/*.jpg")

for i in range(len(files)):
    file = files[i]
    if i % 1000 == 0:
        print(i+1, len(files), file)

    filename = os.path.basename(file)
    path = thumb_dir + "/cj_vis/" + filename


    if not os.path.exists(path):
        shutil.copyfile(file, path)
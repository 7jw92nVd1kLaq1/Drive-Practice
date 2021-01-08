import os
import shutil

directory = "/Users/iusemacandarch/epub_files/Pictures"
question = 701
folders = os.listdir(directory)

folders.sort()

for each in folders[:-3]:
    if each.isdigit():
        files = os.listdir(directory + "/" + each)
        
        for damn in sorted(files):
            shutil.copyfile(directory + "/" + each + "/" + damn, "./{}.jpg".format(question))

            question += 1 


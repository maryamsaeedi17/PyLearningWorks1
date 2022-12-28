import os
import imageio

file_list=sorted(os.listdir("pic for gif"))

IMAGES=[]
for file_name in file_list:
    file_path="pic for gif/"+file_name
    image=imageio.imread(file_path)
    IMAGES.append(image)

imageio.mimsave("my_first_gif.gif",IMAGES,duration=0.4)




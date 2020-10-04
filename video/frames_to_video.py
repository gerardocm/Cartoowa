import numpy as np
import cv2
import os
import glob

OUTPUT_PATH="output_video.mov"
CODEC="output_video.mov"
# Folder where the frames are stored
FRAMES_PATH="frames"
FPS_OUTPUT=1

img_array = []
for filename in glob.glob(FRAMES_PATH+'/*.jpg'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
# Codec for MOV (OSX)
out = cv2.VideoWriter(OUTPUT_PATH,cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), FPS_OUTPUT, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
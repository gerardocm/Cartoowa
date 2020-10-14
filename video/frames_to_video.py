import os
import sys
import getopt
import glob
import cv2
import numpy as np

def convert_to_video(input_path, output_path, fps=30):
    '''
        Converts frames to video 

        Parameters: 
        input_path (string)  : path of the folder with frames
        output_path (string) : path of the output video, default name "output.mp4"
        fps (int)            : frames per second, output rate
    '''

    # Check or create output directory
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)
    except:
        print("Error: invalid output path")
        retun

    img_array = []
    size = None
    for filename in glob.glob(input_path+'/*.jpg'):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)

    # Codec for MOV (OSX)
    if img_array is not None and size is not None:
        out = cv2.VideoWriter(output_path+'/output.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, size)
    
        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()

def __main(argv):
    input_path = ''
    output_path = ''
    frames = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:f:",["iimag=","oimg=","frames="])
    except getopt.GetoptError:
        print('frames_to_video.py -i <inputpath> -o <outputpath>')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print('frames_to_video.py -i <inputpath> -o <outputpath> -f <fps>')
            print('frames_to_video.py -iimag <inputpath> -oimg <outputpath> -fps <fps>')
            sys.exit()
        elif opt in ("-i", "--iimag"):
            input_path = arg
        elif opt in ("-o", "--oimg"):
            output_path = arg
        elif opt in ("-f", "--fps"):
            frames = int(arg)

    print('Input folder path: ', input_path)
    print('Output video: ', output_path)
    print('Frames per second: ', frames)
    convert_to_video(input_path, output_path, frames)
    print("Process complete")

if __name__ == "__main__":
    __main(sys.argv[1:])
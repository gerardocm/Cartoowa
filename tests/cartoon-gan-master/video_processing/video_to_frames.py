import os
import sys
import getopt
import cv2
import numpy as np

def convert_to_frames(input_path, output_path, frames=30, size=(320,320)):
    '''
        Converts video to frames 

        Parameters: 
        input_path (string)  : path of the input video 
        output_path (string) : path of the output frames
        frames (int)         : convertion rate of frames default=30
        size (tuple)         : size of the output frame (x,y) default=(320,320)
    '''
    if frames is None:
        frames=30
    if size is None:
        size=(320,320)

    cap = cv2.VideoCapture(input_path)
    totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    duration = totalFrames / fps
    rate_to_save = int(fps / frames)

    # print('---- Video info ---- ')
    # print("Total Frames: {}".format(totalFrames))
    # print("FPS: {}".format(fps))
    # print("Duration: {}".format(duration))
    # print("Rate to save: {}".format(rate_to_save))

    # Check or create output directory
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)
    except:
        print("Error: invalid output path")
        retun

    count = 0
    frame_name = 0
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        count = count + 1

        if frame is None or cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Display the resulting frames
        # Uncomment this lines to watch the video
        # cv2.imshow('frame',frame)

        if rate_to_save == 0 or not count % rate_to_save:
            resize_img = cv2.resize(frame, size)
            if frame_name < 10:
                
                cv2.imwrite(output_path+"/frame0%d.jpg" % frame_name, resize_img)
            else:
                cv2.imwrite(output_path+"/frame%d.jpg" % frame_name, resize_img) 
            frame_name = frame_name+1
            print("save")


    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def __main(argv):
    input_video = ''
    output_path = ''
    frames = ''
    size = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:f:s:",["iimag=","oimg=","frames=","size"])
    except getopt.GetoptError:
        print('video_to_frames.py -i <inputpath> -o <outputpath>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('video_to_frames.py -i <inputpath> -o <outputpath> -f <framespersecond> -s <h,w>')
            print('video_to_frames.py -iimag <inputpath> -oimg <outputpath> -frames <framespersecond> -size <h,w>')
            sys.exit()
        elif opt in ("-i", "--iimag"):
            input_video = arg
        elif opt in ("-o", "--oimg"):
            output_image = arg
        elif opt in ("-f", "--frames"):
            frames = int(arg)
        elif opt in ("-s", "--size"):
            try:
                size = tuple(map(int, arg.split(',')))
            except:
                print("Invalid size")
                return

    print('Input video: ', input_video)
    print('Output path: ', output_path)
    print('Frames per second: ', frames)
    print('Size: ', size)
    convert_to_frames(input_video, output_path, frames, size)
    print("Process complete")


if __name__ == "__main__":
    __main(sys.argv[1:])
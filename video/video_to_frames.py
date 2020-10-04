import numpy as np
import cv2

VIDEO_PATH="simpsons_video.mov"
FRAMES_PATH="frames"
FPS_TO_SAVE=1
IMG_SIZE=(320,320)

cap = cv2.VideoCapture(VIDEO_PATH)
totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS)
duration = totalFrames / fps
rate_to_save = int(fps / FPS_TO_SAVE)

print("Total Frames: {}".format(totalFrames))
print("FPS: {}".format(fps))
print("Duration: {}".format(duration))
print("Rate to save: {}".format(rate_to_save))


count = 0
frame_name=0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    count = count + 1

    # Display the resulting frames
    # Uncomment this lines to watch the video
    # if not count % 60:
    #     print("showing")
    #     cv2.imshow('frame',gray)
    if not count % rate_to_save:
        resize_img = cv2.resize(frame, IMG_SIZE)
        cv2.imwrite(FRAMES_PATH+"/frame%d.jpg" % frame_name, resize_img) 
        frame_name=frame_name+1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
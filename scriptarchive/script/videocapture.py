import cv2

from imageprocessing import measurefish
from imageprocessing import photomosaic
import controller
import GUI
import videocapture
import queuemodule
from imageprocessing.photomosaic import photomosaicVideo
from imageprocessing.photomosaic import photomosaicStart

videoCaptureObject = cv2.VideoCapture(0)
photomosaicCount = 0

def videoCapture():
    global photomosaicVideo
    global photomosaicStart
    global photomosaicCount
    ret, frame = videoCaptureObject.read()
    cv2.imshow("Capturing Video", frame)
    # deletes every frame as the next one comes on, closes all windows when q is pressed
    if cv2.waitKey(1) == ord('q'):
        videoCaptureObject.release()
        cv2.destroyAllWindows()
    if photomosaicVideo == True:
        #print("photomosaic true")
        if keyboard.is_pressed('s'):
            # and the index is less than the length of the snapshot list
            if photomosaicCount < len(snapshots):
                cv2.imwrite(snapshots[photomosaicCount], frame)
                cropping(snapshots[photomosaicCount])
                center_height = cv2.imread(snapshots[0]).shape[0]
                center_width = cv2.imread(snapshots[0]).shape[1]
                width_ratio = center_width/cv2.imread(snapshots[photomosaicCount]).shape[1]
                height_ratio = center_height/cv2.imread(snapshots[photomosaicCount]).shape[0]
                if photomosaicCount < 3:
                    resized = resize_image(cv2.imread(snapshots[photomosaicCount]), width_ratio, width_ratio)
                else:
                    resized = resize_image(cv2.imread(snapshots[photomosaicCount]), height_ratio, height_ratio)

                cv2.imwrite(snapshots[photomosaicCount], resized)
                print("Snapshot #" + str(photomosaicCount) + " taken")
                #cv2.imshow(snapshots[i], frame)
                time.sleep(1)
                photomosaicCount += 1
            else:
                print("PhotomosaicStart true")
                photomosaicVideo = False
                photomosaicStart = True

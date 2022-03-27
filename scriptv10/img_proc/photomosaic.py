import glob
import cv2
import imutils

def stitch():
    top1 = cv2.imread(glob.snapshots[0])
    top2 = cv2.imread(glob.snapshots[1])
    top3 = cv2.imread(glob.snapshots[2])
    top4 = cv2.imread(glob.snapshots[3])
    bottom1 = cv2.imread(glob.snapshots[4])
    bottom2 = cv2.imread(glob.snapshots[5])
    bottom3 = cv2.imread(glob.snapshots[6])
    bottom4 = cv2.imread(glob.snapshots[7])

    print("Starting Photomosaic Process")
    topLeft = cv2.hconcat([cv2.imread(glob.snapshots[0]), cv2.imread(glob.snapshots[1])])
    cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\topLeft.png", topLeft)

    #----------concat second top two-----------------
    topRight = cv2.hconcat([cv2.imread(glob.snapshots[2]), cv2.imread(glob.snapshots[3])])
    cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\topRight.png", topRight)

    topTile = cv2.hconcat([topLeft, topRight])
    cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\topTile.png", topTile)

    #-------------concat bottom two--------------
    bottomLeft = cv2.hconcat([cv2.imread(glob.snapshots[4]), cv2.imread(glob.snapshots[5])])
    cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\bottomLeft.png", bottomLeft)

    #------------concat second bottom two----------
    bottomRight = cv2.hconcat([cv2.imread(glob.snapshots[6]), cv2.imread(glob.snapshots[7])])
    cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\bottomLeft.png", bottomLeft)

    bottomTile = cv2.hconcat([bottomLeft, bottomRight])
    cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\bottomTile.png", bottomTile)

    #---------stitch together all the tiles-----------
    photomosaic = cv2.vconcat([topTile, bottomTile])
    cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\photomosaic.png", photomosaic)
    cv2.imshow("PHOTOMOSAIC", photomosaic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #definitely have to add this back in later
    #global photomosaicStart
    #photomosaicStart = False

def resize_image(img, scale_w, scale_h):
    return cv2.resize(img, (int(img.shape[1]*scale_h), int(img.shape[0]*scale_w)))

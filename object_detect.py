import cv2 as cv

tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'CSRT', 'MOSSE']

stream = cv.VideoCapture(0)
#tracker = cv.TrackerMOSSE_create() #TrackerMOSSE is faster but loses target more easily
tracker = cv.TrackerCSRT_create() #TrackerCSRT is much slower but slightly more reliable
success, img = stream.read()
bbox = cv.selectROI("Tracking", img, False)
tracker.init(img, bbox)

counter = 0
fps = 0.0

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv.rectangle(img, (x,y), ((x+w),(y+h)), (0,255,0),3,1)
    cv.putText(img, "Object Found", (50, 75), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0),2)

while True:
    timer = cv.getTickCount()
    success, img = stream.read()

    success, bbox = tracker.update(img)
    #cv.putText(img, "Tracker: ", (50, 25), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0),2)

    if success:
        drawBox(img, bbox)
    else:
        cv.putText(img, "Lost", (50, 75), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255),2)

    counter += 1
    if counter%4 == 0:
        fps = cv.getTickFrequency()/(cv.getTickCount()-timer)
    cv.putText(img, str(int(fps)), (50,50), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0),2)

    cv.imshow("Stream", img)
    if cv.waitKey(1) & 0xff == ord('q'):
        break

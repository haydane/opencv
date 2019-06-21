import cv2


def ask_for_tracker():
    print("welcome! what tracker api would you like to use?")
    print("enter 0 for BOOSTING: ")
    print("enter 1 for MIL: ")
    print("enter 2 for KCF: ")
    print("enter 3 for TLD: ")
    print("enter 4 for MEDIANFLOW: ")
    choice = input("please select your tracker: ")

    if choice == '0':
        tracker = cv2.TrackerBoosting_create()
    if choice == '1':
        tracker = cv2.TrackerMIL_create()
    if choice == '2':
        tracker = cv2.TrackerKCF_create()
    if choice == '3':
        tracker = cv2.TrackerTLD_create()
    if choice == '4':
        tracker = cv2.TrackerMedianFlow_create()
    return tracker


tracker = ask_for_tracker()
tracker_name = str(tracker).split()[0][1:]

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

# special function allows us to draw on the very first frame our desired roi
roi = cv2.selectROI(frame, False)
ret = tracker.init(frame, roi)

while True:
    # read a new frame
    ret, frame = cap.read()

    # update tracker
    success, roi = tracker.update(frame)

    # roi variable is a tuple of 4 floats
    # we need each value and we need them as integers
    (x, y, w, h) = tuple(map(int, roi))

    # draw rectangel as tracker moves
    if success:
        # tracking succes
        p1 = (x, y)
        p2 = (x+w, y+h)
        cv2.rectangle(frame, p1, p2, (0, 255, 0), 3)
    else:
        # tracking failure
        cv2.putText(frame, "Failure to Detect Tracking!",
                    (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    # display tracker type of frame
    cv2.putText(frame, tracker_name, (20, 400),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    # display result
    cv2.imshow(tracker_name, frame)

    k = cv2.waitKey(1) & 0xff

    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()

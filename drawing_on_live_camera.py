import cv2
import matplotlib.pyplot as plt


# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# global variables
pt1 = (0, 0)
pt2 = (0, 0)
topLeftClicked = False
botRightClicked = False

# call back function rectangle


def draw_rectangle(event, x, y, flags, param):
    global pt1, pt2, topLeftClicked, botRightClicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # reset the rectangle
        if topLeftClicked == True and botRightClicked == True:
            pt1 = (0, 0)
            pt2 = (0, 0)
            topLeftClicked = False
            botRightClicked = False

        if topLeftClicked == False:
            pt1 = (x, y)
            topLeftClicked = True
        elif botRightClicked == False:
            pt2 = (x, y)
            botRightClicked = True


# connect to the callback
cap = cv2.VideoCapture(0)
cv2.namedWindow('frame')
cv2.setMouseCallback('frame', draw_rectangle)
# top left corner
# x = width // 2
# y = height // 2

# width and height of rectangle
# w = width // 4
# h = height // 4

# bottom right x+w , y+h


while True:
    ret, frame = cap.read()
    # cv2.rectangle(frame, (x, y), (x+w, y+h), color=(0, 0, 255), thickness=3)

    # drawing on the frame based off the glbal vairables
    if topLeftClicked == True:
        cv2.circle(frame, center=pt1, radius=5, color=(0, 0, 255))
    if topLeftClicked == True and botRightClicked == True:
        cv2.rectangle(frame, pt1, pt2, (0, 0, 255), 3)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()

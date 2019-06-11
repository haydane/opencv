import cv2
import numpy as np
# matlplotlib RED GREEN BLUE
import matplotlib.pyplot as plt
from PIL import Image


pic = Image.open('puppy.jpg')
type(pic)
# convert img to num py array
pic_arr = np.asarray(pic)
# plt.show(plt.imshow(pic_arr))


# copy pic_array value to pic_red
pic_red = pic_arr.copy()
# plt.show(plt.imshow(pic_red[:,:,1]))
# plt.show(plt.imshow(pic_red[:,:,0],cmap='gray'))
# plt.show(plt.imshow(pic_red[:,:,1],cmap='gray'))
# plt.show(plt.imshow(pic_red[:,:,2],cmap='gray'))

# give value 0 to green
pic_red[:, :, 0] = 0
# give value 0 to blue
pic_red[:, :, 1] = 0
# plt.show(plt.imshow(pic_red))

# print(pic_red[:,:,0])

# cv 2 ----> BLUE GREEN RED
img = cv2.imread('puppy.jpg')
# plt.show(plt.imshow(img))
fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.show(plt.imshow(fix_img))
img_gray = cv2.imread('puppy.jpg', cv2.IMREAD_GRAYSCALE)
# plt.show(plt.imshow(img_gray,cmap='magma'))
# new_img = cv2.resize(fix_img,(800,300))
# plt.show(plt.imshow(new_img))
# print(img_gray.shape)

# ratio
w_ratio = 0.5
h_ratio = 0.5
img_ratio = cv2.resize(fix_img, (0, 0), fix_img, w_ratio, h_ratio)


# pass converted img to new variable
# img_changed = cv2.flip(img,-1);
# cv2.imwrite("changed.jpg",img_changed);

# 3########## frame size when showing img
# fig = plt.figure(figsize=(2, 2))
# fig = fig.add_subplot(111)
# plt.show(fig.imshow(fix_img))


# wait_key
# cv2.imshow('puppy',img);
# while True:
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
# cv2.destroyAllWindows()


# blank_img
blank_img = np.zeros(shape=(500, 500, 3), dtype=np.uint8)

cv2.rectangle(blank_img, pt1=(125, 125), pt2=(
    375, 375), color=(0, 255, 0), thickness=10)
cv2.rectangle(blank_img, pt1=(0, 450), pt2=(
    50, 400), color=(0, 0, 255), thickness=10)
cv2.circle(blank_img, center=(50, 50), radius=50,
           color=(255, 0, 0), thickness=8)
cv2.circle(blank_img, center=(420, 420), radius=50,
           color=(255, 0, 0), thickness=-1)
cv2.line(blank_img, pt1=(0, 0), pt2=(500, 500),
         color=(46, 233, 200), thickness=5)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blank_img, text='Hello', org=(10, 500), fontFace=font,
            fontScale=2, color=(255, 255, 255), thickness=3, lineType=cv2.LINE_AA)
plt.imshow(blank_img)
plt.show()

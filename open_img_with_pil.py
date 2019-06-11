# open image with PIL
import matplotlib.pyplot as plt
from PIL import Image

dog = Image.open('haydane.jpg');
plt.imshow(dog);
plt.show()



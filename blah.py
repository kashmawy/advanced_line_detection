import numpy as np
import cv2
import glob
from scipy.misc import imread, imresize, imsave
import matplotlib.pyplot as plt
from lane import Lane
# %matplotlib qt
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from moviepy.editor import VideoFileClip
from datetime import datetime
from transform import TopDownTransform


# plt.subplot(1, 2, 1)
# plt.imshow(imread('./test_images/test1.jpg'))
# plt.subplot(1, 2, 2)
# plt.imshow(imread('solutions/threshold_new.png'))
plt.imshow(imread('solutions/threshold_new.png'), cmap='gray')
plt.plot()
plt.show()

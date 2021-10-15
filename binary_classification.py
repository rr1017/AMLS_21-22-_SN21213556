from PIL import Image, ImageFilter, ImageStat
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

# Load file names and labels
df = pd.read_csv('dataset/label_data.csv')

# Create stacked numpy array of images

im_array = np.zeros((3000,512,512))
acc = 0
for filename in df.loc[:,'file_name']:
    im_array[acc,:,:] = np.array(Image.open('dataset/image/'+filename).convert('L'))
    acc+=1

# Calculate the ratio between pixel intensity at the top and bottom of the left diagonal
ratio = []
for i in tqdm(range(0,3000)):
    top=0
    bottom=0
    for j in range(0,512):
        for k in range(0,512-j):
            top = top+im_array[i,j,k]
    for k in range(0,512):
        for j in range(0,k):
            bottom = bottom+im_array[i,j,k]

    ratio.append(top/bottom)

print(ratio)

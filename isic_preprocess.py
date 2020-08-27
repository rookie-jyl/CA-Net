#!/usr/bin/python3
#  these code is for ISIC 2018: Skin Lesion Analysis Towards Melanoma Detection
# -*- coding: utf-8 -*-
# @Author  : Ran Gu

import os
import random
import numpy as np
from skimage import io
from PIL import Image

root_dir = '/gr/Skin segmentation/'                # change it in your saved original data path
save_dir = 'data/ISIC2018_Task1_npy_all'


if __name__ == '__main__':
    imgfile = os.path.join(root_dir, 'ISIC2018_Task1-2_Training_Input')
    labfile = os.path.join(root_dir, 'ISIC2018_Task1_Training_GroundTruth')
    filename = sorted([os.path.join(imgfile, x) for x in os.listdir(imgfile) if x.endswith('.jpg')])
    random.shuffle(filename)
    labname = [filename[x].replace('ISIC2018_Task1-2_Training_Input', 'ISIC2018_Task1_Training_GroundTruth'
                                   ).replace('.jpg', '_segmentation.png') for x in range(len(filename))]

    for i in range(len(filename)):
        fname = filename[i].rsplit('/', maxsplit=1)[-1]
        lname = labname[i].rsplit('/', maxsplit=1)[-1]

        image = Image.open(filename[i])
        label = Image.open(labname[i])

        image = image.resize((342, 256))
        label = label.resize((342, 256))

        images_img_filename = os.path.join(save_dir, 'image', fname)
        labels_img_filename = os.path.join(save_dir, 'label', lname)
        image.save(images_img_filename)
        label.save(labels_img_filename)

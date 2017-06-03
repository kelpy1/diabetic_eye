import numpy as np
import pandas as pd
import random

import PIL
from PIL import Image

import os
from os.path import join

IMG_SIZE = (256, 256)

train_labels_path = '/workdir/data/trainLabels.csv'
raw_data_dir = '/workdir/data/raw/train/'
save_data_dir = '/workdir/data/preproc/'
val_split = 0.8


def transform(img):
    img = img.resize(IMG_SIZE)
    return img

def mkdir(new_dir):
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
        
def save_data_folder(df_labels, folder_path, raw_data_dir):
    mkdir(folder_path)
    for name, row in df_labels.iterrows():
        img_path = join(raw_data_dir, name+'.jpeg')
        image = Image.open(img_path)
        image = transform(image)
        cls_folder = join(folder_path, str(row.level))
        mkdir(cls_folder)
        image.save(join(cls_folder, name), 'jpeg')
        
def save_dataset(train_labels_path, raw_data_dir, save_data_dir, val_split):
    train_labels = pd.read_csv(train_labels_path, index_col=0)
    img_names = list(train_labels.index)
    random.shuffle(img_names)
    int_val_split = int(val_split*len(img_names))
    train_img_names = img_names[:int_val_split]
    val_img_names = img_names[int_val_split:]
    
    df_train_labels = train_labels.loc[train_img_names]
    df_val_labels = train_labels.loc[val_img_names]
    
    save_data_folder(df_train_labels, join(save_data_dir, 'train'), raw_data_dir)
    save_data_folder(df_val_labels, join(save_data_dir, 'val'), raw_data_dir)
    
    
if __name__ == '__main__':
    save_dataset(train_labels_path, raw_data_dir, save_data_dir, val_split)
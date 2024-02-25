# Importing all the libraries needed
import numpy as np

from tensorflow.keras.preprocessing import image
import tensorflow as tf
import pandas as pd
import os, requests, random
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import models
from tensorflow.keras import Sequential, layers
from keras.preprocessing.image import ImageDataGenerator
from tensorflow import keras

from tensorflow.keras.models import load_model

def prediction(path):
    print(path)
    model=load_model('cnn.h5')
    img=image.load_img(path,target_size=(224,224))
    print(img)
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    ## Scaling
    x=x/255
    x = np.expand_dims(x, axis=0)
    predictions = model.predict(x)
    print(predictions)
    predicted_classes = np.argmax(predictions,axis=1)
    print(predicted_classes)
path=str("fb967f21-6c02-4bd3-9145-ee91db7eb2c8___Com.G_TgS_FL_8059.JPG")
prediction(path)
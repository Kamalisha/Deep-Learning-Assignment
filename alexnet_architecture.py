# -*- coding: utf-8 -*-
"""AlexNet Architecture

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nbQGNOWDC5axaEiwd2epyH-1VNHoUp9Z
"""

!pip install tensorflow
import tensorflow as tf

import keras
from keras.datasets import cifar10
from keras.optimizers import SGD
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D, BatchNormalization

# AlexNet
resize = 227
model = Sequential()

# part 1
model.add(Conv2D(filters=96, kernel_size=(11,11),
                 strides=(4,4), padding='valid',
                 input_shape=(resize,resize,3),
                 activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(3,3),
                       strides=(2,2),
                       padding='valid'))
# part 2
model.add(Conv2D(filters=256, kernel_size=(5,5),
                 strides=(1,1), padding='same',
                 activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(3,3),
                       strides=(2,2),
                       padding='valid'))
# part 3
model.add(Conv2D(filters=384, kernel_size=(3,3),
                 strides=(1,1), padding='same',
                 activation='relu'))
model.add(Conv2D(filters=384, kernel_size=(3,3),
                 strides=(1,1), padding='same',
                 activation='relu'))
model.add(Conv2D(filters=256, kernel_size=(3,3),
                 strides=(1,1), padding='same',
                 activation='relu'))
model.add(MaxPooling2D(pool_size=(3,3),
                       strides=(2,2), padding='valid'))
# part 4
model.add(Flatten())
model.add(Dense(4096, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(4096, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(1000, activation='relu'))
model.add(Dropout(0.5))

# Output Layer
model.add(Dense(2))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

model.summary()
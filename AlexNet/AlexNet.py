#coding=utf-8
from keras.models import Sequential
from keras.layers import Dense,Flatten,Dropout
from keras.layers.convolutional import Conv2D,MaxPooling2D
from keras import optimizers

class AlexNet:
    def __init__(self):
        model = Sequential()
        model.add(Conv2D(96,(11,11),strides=(4,4),input_shape=(227,227,3),padding='valid',activation='relu',kernel_initializer='uniform'))
        model.add(MaxPooling2D(pool_size=(3,3),strides=(2,2)))
        model.add(Conv2D(256,(5,5),strides=(1,1),padding='same',activation='relu',kernel_initializer='uniform'))
        model.add(MaxPooling2D(pool_size=(3,3),strides=(2,2)))
        model.add(Conv2D(384,(3,3),strides=(1,1),padding='same',activation='relu',kernel_initializer='uniform'))
        model.add(Conv2D(384,(3,3),strides=(1,1),padding='same',activation='relu',kernel_initializer='uniform'))
        model.add(Conv2D(256,(3,3),strides=(1,1),padding='same',activation='relu',kernel_initializer='uniform'))
        model.add(MaxPooling2D(pool_size=(3,3),strides=(2,2)))
        model.add(Flatten())
        model.add(Dense(4096,activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(4096,activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(2,activation='softmax'))
        model.compile(loss='categorical_crossentropy',optimizer="sgd",metrics=['accuracy'])
        self.model = model
    

    
    
    

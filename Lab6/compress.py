import os
import sys
import numpy as np
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

print(tf.__version__)

fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
train_images = train_images.reshape((60000, 28, 28, 1))
test_images = test_images.reshape((10000, 28, 28, 1))

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0
model = models.Sequential()
model.add(layers.Flatten(input_shape= (28, 28, 1)))
model.add(layers.Dense(200))
model.add(layers.Dense(1568, activation= 'relu'))
model.add(layers.Dense(784))
model.add(layers.Reshape((28, 28)))

model.compile(loss= 'mean_squared_error', metrics= ['accuracy'])
model.fit(train_images, train_images, epochs=10, batch_size = 64)
model_loss, model_acc = model.evaluate(test_images, test_images)

model.summary()                                 

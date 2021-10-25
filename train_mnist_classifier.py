#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
- Create and train a basic mnist digit classifier
- Save the train model as 
   1. keras (.h5) format
   2. SavedModel (.pb) format
   
Created on Mon Oct 25 19:42:27 2021

@author: twentyface
"""

import tensorflow as tf
import numpy as np
print("TensorFlow version:", tf.__version__)

# Load a dataset and convert the data from integers to floating-point numbers
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
'''
for i in range(5):
    plt.subplot(1,5,i+1)
    plt.imshow(x_test[i], cmap=plt.get_cmap('gray'))
plt.show()
'''
x_train, x_test = x_train / 255.0, x_test / 255.0# normalized data

# Build a machine learning model (tf.keras.Sequential model by stacking layers)
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
    ])

# the model returns a vector of logits or log-odds scores, one for each class.
predictions = model(x_train[:1]).numpy()

# loss function for training, which takes a vector of logits and a True index 
# and returns a scalar loss for each example
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

# configure and compile the model
model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

# train the  model (adjust model parameters and minimize loss)
model.fit(x_train, y_train, epochs=5)
# evaluate the  model
model.evaluate(x_test,  y_test, verbose=2)

# to return a probability, wrap the trained model, and attach the softmax to it
probability_model = tf.keras.Sequential([
    model,
    tf.keras.layers.Softmax()])

probability_model.summary()


# test
input_image = x_test[:1]# (1,28,28)
output1 = probability_model.predict(input_image)
# alternative test
img = x_test[0,:,:]# (28,28)
img = np.expand_dims(img, axis=0)# # (1,28,28)
#img = np.transpose(img, (2, 1, 0))#a.reshape(28,28,1)
#imgg = img.reshape((img.shape[0], img.shape[1], 1))
output2 = probability_model.predict(img)

# SAVE THE MODEL

# Save the entire model to a HDF5 file.
probability_model.save('./models/mnist.h5')
# Recreate the exact same model, including its weights and the optimizer
#new_model = tf.keras.models.load_model('my_model.h5')

# Save the entire model as a SavedModel.
probability_model.save('./models/mnist')
new_model = tf.keras.models.load_model('./models/mnist')

# Convert .h5 to savedmodel?
# model_h5 = tf.keras.models.load_model('./models/mnist.h5')
# model_h5.save('./models/mnist')

'''
# Save the weights using the `checkpoint_path` format
model.save_weights(checkpoint_path.format(epoch=0))
# Load the previously saved weights
model.load_weights(latest)
# Save the weights
model.save_weights('./checkpoints/my_checkpoint')
# Restore the weights
model.load_weights('./checkpoints/my_checkpoint')
'''

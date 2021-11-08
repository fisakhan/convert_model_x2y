#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


Created on Fri Feb 19 09:26:57 2021
Source: https://www.tensorflow.org/lite/convert
Model load and save: https://www.tensorflow.org/tutorials/keras/save_and_load

@author: Asif Khan
"""

import tensorflow as tf

#print('\nVersion of installed TensorFlow: ', tf.__version__) 
#print('\nhelp(tf.lite.TFLiteConverter): ', help(tf.lite.TFLiteConverter))

path2h5model = './models/210729_42.h5'

h5_model = tf.keras.models.load_model(path2h5model)

# Convert the model.
converter = tf.lite.TFLiteConverter.from_keras_model(h5_model)

#converter.post_training_quantize = True

tflite_model = converter.convert()

# Save the model.
with open('./models/210729_42.tflite', 'wb') as f:
  f.write(tflite_model)

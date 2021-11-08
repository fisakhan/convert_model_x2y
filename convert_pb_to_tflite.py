#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 09:26:57 2021


Source: https://www.tensorflow.org/lite/convert

@author: t
"""

import tensorflow as tf

print('\nVersion of installed TensorFlow: ', tf.__version__) 
print('\nhelp(tf.lite.TFLiteConverter): ', help(tf.lite.TFLiteConverter))

# Convert the model
saved_model_dir = './tf-serving-facenet/2'# path to .pb model directory
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir) # path to the SavedModel directory
tflite_model = converter.convert()

# Save the model.
with open('facenet_V2_sm.tflite', 'wb') as f:
  f.write(tflite_model)

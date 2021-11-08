#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Load a savedmodel format and write to disk as .h5 format

******* WORKS FOR 20FACENET BUT NOT FOR RETINAFACE ************
***************************************************************

Created on Tue Sep 28 11:52:24 2021

@author: twentyface
"""

import tensorflow as tf

path2savedmodel = '/home/twentyface/Projects/TF24/Model/tf-serving-retinaface_mbv2/1'#'./models/210729_42'
#path2savedmodel = './models/210729_42'

# Loading the Tensorflow Saved Model (PB)
model = tf.keras.models.load_model(path2savedmodel)

# Saving the Model in H5 Format
tf.keras.models.save_model(model, 'h5_model.h5')

# Verify .h5 model --- loading the H5 Saved Model
loaded_model_from_h5 = tf.keras.models.load_model('h5_model.h5')
print(loaded_model_from_h5.summary())
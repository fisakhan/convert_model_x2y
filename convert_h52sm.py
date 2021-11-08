#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Load a keras model (.h5) and write to disk as SavedModel format

SavedModel is the more comprehensive save format that saves the model 
architecture, weights, and the traced Tensorflow subgraphs of the call functions. 
This enables Keras to restore both built-in layers as well as custom objects.

Created on Tue Sep 28 11:52:24 2021

@author: Asif Khan
"""

import os
from tensorflow import keras

path2h5 = './models/mnist.h5'
path2SavedModel = './models/mnist'

if not os.path.exists(path2SavedModel):
    os.makedirs(path2SavedModel)


# load keras model .h5
model_h5 = keras.models.load_model(path2h5)

# save loaded model as SavedModel
model_h5.save(path2SavedModel)
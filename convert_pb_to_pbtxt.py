#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert TF saved model from protobuf binary to text format (.pbtxt)

Created on Wed Oct 20 15:25:36 2021

@author: t
"""

import os, sys

import google.protobuf
from tensorflow.core.protobuf import saved_model_pb2
import tensorflow as tf


def convert_saved_model_to_pbtxt(path):
    saved_model = saved_model_pb2.SavedModel()
    with open(os.path.join(path, 'saved_model.pb'), 'rb') as f:
        saved_model.ParseFromString(f.read())
        
    with open(os.path.join(path, 'saved_M.pbtxt'), 'w') as f:
        f.write(google.protobuf.text_format.MessageToString(saved_model))

'''
for path in sys.argv[1:]:
    convert_saved_model_to_pbtxt(path)
''' 

path2savedmodel = './models/210729_42'
path2txt = ''   

saved_model = saved_model_pb2.SavedModel()

with open(os.path.join(path2savedmodel, 'saved_model.pb'), 'rb') as f:
    saved_model.ParseFromString(f.read())
    
with open('./models/210729_42.pbtxt', 'w') as f:
    f.write(google.protobuf.text_format.MessageToString(saved_model))

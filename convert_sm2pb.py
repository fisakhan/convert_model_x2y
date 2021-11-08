#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Load a SavedModel format and write to disk as frozen graph (.pb)

Created on Tue Sep 28 11:52:24 2021

@author: Asif Khan
"""

import tensorflow as tf
from tensorflow.python.framework.convert_to_constants import convert_variables_to_constants_v2

path2SavedModel = './models/mnist'
path2frozengraph = './models/mnist.pb'

loaded = tf.saved_model.load(path2SavedModel)
infer = loaded.signatures['serving_default']# use saved_model_cli to get this info

# if saved_model_cli returns shape: (-1, 160, 160, 3)
#f = tf.function(infer).get_concrete_function(input_1=tf.TensorSpec(shape=[None, 160, 160, 3], dtype=tf.float32))

# if saved_model_cli returns shape: (-1, 28, 28)
f = tf.function(infer).get_concrete_function(input_1=tf.TensorSpec(shape=[None, 28, 28, 1], dtype=tf.float32))

f2 = convert_variables_to_constants_v2(f)
graph_def = f2.graph.as_graph_def()# Export frozen graph

# write frozen graph (single file) to disk
with tf.io.gfile.GFile(path2frozengraph, 'wb') as f:
   f.write(graph_def.SerializeToString())


# saved_model_cli tool
'''
step 1: 
    on commond line execute the following
    saved_model_cli show --dir path/to/models/mnist

step2 : 
    on commond line execute the following
    saved_model_cli show --dir path/to/models/mnist --tag_set serve
    
step 3:
    saved_model_cli show -dir path/to/models/mnist --tag_set serve --signature_def serving_default
'''
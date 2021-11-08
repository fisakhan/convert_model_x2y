#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Load a SavedModel format and write to disk as .onnx

Created on Tue Sep 28 11:52:24 2021

@author: Asif Khan
"""

# step1: pip install -U tf2onnx
# step2: run the following command from command prompt
# python3 -m tf2onnx.convert --saved-model /models/mnist --output /models/mnist.onnx

print("""
      Please follow the following steps
      
      step1: pin install -U tf2onnx
      
      step2: run the following command from command prompt
          python3 -m tf2onnx.convert --saved-model /models/mnist --output /models/mnist.onnx"""
      )


#https://github.com/onnx/tensorflow-onnx
#example: https://github.com/onnx/tutorials/blob/master/tutorials/TensorflowToOnnx-1.ipynb
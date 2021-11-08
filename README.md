# convert_model_x2y
Convert neural network model from one format (x) to other (y)

# Conversion of models

:bell:   **ALL models are available for non-commercial research purposes only.**

## 0. Train and save keras model format (.h5) and SavedModel format from scratch
run: ``python3 train_mnist_classify.py``

| x                | y                       | command                  | Alignment    | Attributes | Model-Size |
| ---------------- | ----------------------- | ------------------------ | ------------ | ---------- | ---------- |
| keras model (.h5)| SavedModel              | python3 convert_h52sm.py | - | abc | 7MB |
| SavedModel       | keras model (.h5)       | python3 convert_sm2h5.py | - | abc | 6MB |
| SavedModel       | Frozen graph (.pb)      | python3 convert_sm2pb    | - | abc | 3MB |
| SavedMOdel       | ONNX (.onnx)            | python3 convert_sm2onnx  | - | abc | 9MB |
| SavedModel       | TensorFlow Lite (.tflit)| python3 convert_sm2tflit | - | xyz | 6MB |



### Conversion of models ###
Markup : 1. create keras model format (.h5) and savedmodel format from scratch, also convert .h5 model to savedmodel format
	python3 train_mnist_classify.py
              2. Which is numbered
          2. Which is numbered


* create keras model format (.h5) and savedmodel format from scratch, also convert .h5 model to savedmodel format
	* train_mnist_classify.py

Markup :  `code()`

# Conversion of models

:bell:   **ALL models are available for non-commercial research purposes only.**

## 0. Train and save keras model format (.h5) and SavedModel format from scratch

To run: ``python3 train_mnist_classify.py``

## 1. Convert keras model format (.h5) to SavedModel format

To run: ``python3 train_mnist_classify.py``

To use the specific model pack:

```
model_pack_name = 'buffalo_l'
app = FaceAnalysis(name=model_pack_name)
```

# Conversion of models (convert_model_x2y)
Convert neural network model from one format (x) to other (y)

:bell:   **ALL models are available for non-commercial research purposes only.**

## 0. Train and save keras model format (.h5) and SavedModel format from scratch
run: ``python3 train_mnist_classify.py``

## 1. Conversion of models
| x                | y                       | command                  | Attributes | Model-Size |
| ---------------- | ----------------------- | ------------------------ | ---------- | ---------- |
| keras model (.h5)| SavedModel              | ''python3 convert_h52sm.py''    | abc | 7MB |
| SavedModel       | keras model (.h5)       | ''python3 convert_sm2h5.py''    | abc | 6MB |
| SavedModel       | Frozen graph (.pb)      | ''python3 convert_sm2pb.py''    | abc | 3MB |
| SavedModel       | ONNX (.onnx)            | ''python3 convert_sm2onnx.py''  | abc | 9MB |
| SavedModel       | TensorFlow Lite (.tflit)| ''python3 convert_sm2tflit.py'' | xyz | 6MB |

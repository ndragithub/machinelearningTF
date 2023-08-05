import tensorflow as tf

if tf.test.is_gpu_available():
    print("GPU is available")
else:
    print("no GPU")

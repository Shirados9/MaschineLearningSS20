import tensorflow as tf

import warnings
# warnings.filterwarnings("ignore")

print(tf.__version__)
print(tf.keras.__version__)
d0 = tf.ones((1,))
print(d0)

d3 = tf.ones((2,2,2))
print(d3.numpy())
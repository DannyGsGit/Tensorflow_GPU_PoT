

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Import dependencies ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import tensorflow as tf



#~~~~~~~~~~~~~~~~~~~~~
#### Hellow World ####
#~~~~~~~~~~~~~~~~~~~~~

hello = tf.constant('Hello From TensorFlow!')
sess = tf.Session()
print(sess.run(hello))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Simple math operation ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

a = tf.constant(10)
b = tf.constant(32)
print(sess.run(a + b))


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


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Confirm available devices ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# The above code confirms the functionality of TensorFlow, but does not guarantee
# that our GPU(s) are properly configured. Use the following function to query
# available devices.

# Import the device library
from tensorflow.python.client import device_lib

# Function to query tensorflow for available devices
def get_available_devices():
    local_device_protos = device_lib.list_local_devices()
    return [x.name for x in local_device_protos]

# Get the list of GPUs
get_available_devices()


# -*- coding: utf-8 -*-

import tensorflow as tf

"""

Created on Mon Jul 16 20:05:52 2018



@author: Lenovo

"""

number1 = tf.constant(3)

number2 = tf.constant(4)

result=tf.add(number1,number2)

sess = tf.Session()

result=sess.run(result)

print("结果是")

print(result)

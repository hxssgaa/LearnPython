from random import random

import tensorflow as tf

# Model parameters

n = 3
theta = [tf.Variable(random() * 2 - 1, tf.float32) for _ in xrange(n)]
# Model input and output
x = tf.placeholder(tf.float32)
linear_model = theta[0] + theta[1] * x + theta[2] * (x ** 2)
y = tf.placeholder(tf.float32)
# loss
loss = tf.reduce_sum(tf.square(linear_model - y))  # sum of the squares
# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.0005)
train = optimizer.minimize(loss)
# training data
x_train = [1, 7, 9, 2, 5, 6, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# mu, sigma = mean(x_train), std(x_train)
# x_train = (x_train - mu) / sigma
y_train = [-233, 367, 567, -133, 167, 267, 2067, 2167, 2267, 2367, 2467, 2567, 2667, 2767, 2867, 2967, 3067, 3167  ]

# evaluate training accuracy
with tf.Session() as sess:
    # training loop
    init = tf.global_variables_initializer()
    sess.run(init)  # reset values to wrong
    for i in range(50000):
        sess.run(train, {x: x_train, y: y_train})

    writer = tf.summary.FileWriter('logs', sess.graph)
    curr_res = sess.run(theta + [loss], {x: x_train, y: y_train})
    writer.close()
print("Theta: %s loss: %s" % (curr_res[:-1], curr_res[-1]))

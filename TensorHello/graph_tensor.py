import tensorflow as tf

# Model parameters
from numpy import mean, std

W = tf.Variable([.8], tf.float32)
b = tf.Variable([-.6], tf.float32)
# Model input and output
x = tf.placeholder(tf.float32)
linear_model = W * x + b
y = tf.placeholder(tf.float32)
# loss
loss = tf.reduce_sum(tf.square(linear_model - y))  # sum of the squares
# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.007)
train = optimizer.minimize(loss)
# training data
x_train = [1, 7, 9, 2]
mu, sigma = mean(x_train), std(x_train)
x_train = (x_train - mu) / sigma
y_train = [-233, 367, 567, -133]

# evaluate training accuracy
with tf.Session() as sess:
    # training loop
    init = tf.global_variables_initializer()
    sess.run(init)  # reset values to wrong
    for i in range(5000):
        sess.run(train, {x: x_train, y: y_train})

    writer = tf.summary.FileWriter('logs', sess.graph)
    curr_W, curr_b, curr_loss = sess.run([W, b, loss], {x: x_train, y: y_train})
    writer.close()
print("For x=30, y=%d" % round(curr_W * (30 - mu) / sigma + curr_b))
print("W: %s b: %s loss: %s" % (round(curr_W), round(curr_b), curr_loss))

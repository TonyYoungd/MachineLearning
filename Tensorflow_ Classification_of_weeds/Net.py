"""
    使用VGG识别图像
"""

import tensorflow as tf
import Loading_images

# 图像大小
IMAGE_SIZE = 224

# 定义学习率
LEARNING_RATE = 0.001

# 定义批次
BATCH_SIZE = 32

# drop_out
KEEP_PROB = 0.6

# 定义两个placeholder
x = tf.placeholder(tf.float32, [None, IMAGE_SIZE, IMAGE_SIZE, 3], name="x")
y = tf.placeholder(tf.float32, [None, 12], name='y')
keep_prob = tf.placeholder(tf.float32, name='prob')


# 定义权值
def weight_variable(shape):
    initial = tf.truncated_normal(shape=shape, stddev=0.1)
    return tf.Variable(initial)


# 定义偏置
def bias_variable(shape):
    initial = tf.truncated_normal(shape=shape, stddev=0.1)
    return tf.Variable(initial)


# 定义卷积层
def conv2d(x, W):
    # x是一个tensor,[batch, in_height, in_width, in_channels(通道数)]
    # W-卷积核[height, width, in_channels, out_channels]
    # strides 步长
    # padding 是否补0
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


# 定义池化层
def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


"""定义神经网络的结构"""
def net(x_image, keep_prob, name_net):
    # 初始化第一卷积层
    W_conv1 = weight_variable([3, 3, 3, 16])
    b_conv1 = bias_variable([16])
    h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1, name='h_conv1')
    b_pool1 = max_pool_2x2(h_conv1)

    # 第二个卷基层
    W_conv2_1 = weight_variable([3, 3, 16, 32])
    b_conv2_1 = bias_variable([32])
    h_conv2_1 = tf.nn.relu(conv2d(b_pool1, W_conv2_1) + b_conv2_1, name='h_conv2_1')
    W_conv2_2 = weight_variable([3, 3, 32, 32])
    b_conv2_2 = bias_variable([32])
    h_conv2_2 = tf.nn.relu(conv2d(h_conv2_1, W_conv2_2) + b_conv2_2, name='h_conv2_2')
    b_pool2 = max_pool_2x2(h_conv2_2)

    # 第三个卷基层
    W_conv3 = weight_variable([3, 3, 32, 64])
    b_conv3 = bias_variable([64])
    h_conv3 = tf.nn.relu(conv2d(b_pool2, W_conv3) + b_conv3, name='h_conv3')
    b_pool3 = max_pool_2x2(h_conv3)

    """定义全连接层"""
    # 初始化第一个全连接层的权值
    W_fc1 = weight_variable([28 * 28 * 64, 512])
    b_fc1 = bias_variable([512])

    # 把池化层2的输出扁平化为1维
    h_pool2_flat = tf.reshape(b_pool3, [-1, 28 * 28 * 64])
    # 求第一个全连接层的输出
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

    # keep_prob用来表示神经元的输出概率
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

    # 初始化第二个全连接层
    W_fc2 = weight_variable([512, 12])
    b_fc2 = bias_variable([12])

    # 计算输出
    prediction = tf.matmul(h_fc1_drop, W_fc2, name=name_net) + b_fc2

    return prediction


# 进行预测
prediction = net(x, keep_prob, 'CNN_net')

# 交叉熵代价函数
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y, logits=prediction), name="cross_entropy")

# 使用AdamOptimizer进行优化
train_step = tf.train.AdamOptimizer(LEARNING_RATE, name="train_step").minimize(cross_entropy)

""" 测试准确率 """

# 将结果放在布尔列表中
correct_prediction = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))

# 求准确率
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32), name="accuracy")

# 加载数据
batch_xs, batch_ys = Loading_images.Load_image(IMAGE_SIZE, BATCH_SIZE)
# batch_xs_test, batch_ys_test = Loading_images.Load_test_images(IMAGE_SIZE, 10)
# 保存模型
saver = tf.train.Saver()
# 保存prediction以便在预测的时候使用
tf.add_to_collection('pred_network', prediction)

with tf.Session() as sess:
    sess.run([tf.global_variables_initializer(), tf.local_variables_initializer()])
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    for epoch in range(500):
        for batch in range(133):
            batch_x, batch_y = sess.run([batch_xs, batch_ys])
            sess.run(train_step, feed_dict={x: batch_x, y: batch_y, keep_prob: KEEP_PROB})
            if batch % 10 == 0:
                loss, acc = sess.run([cross_entropy, accuracy], feed_dict={x: batch_x, y: batch_y, keep_prob: KEEP_PROB})
                # sum = 0.0
                # for _ in range(10):
                    # batch_x_test, batch_y_test = sess.run([batch_xs_test, batch_ys_test])
                    # acc_test = sess.run(accuracy, feed_dict={x:batch_x_test, y: batch_y_test, keep_prob: 1})
                    #sum += acc_test
                # acc_test = sum/10
                print("Epoch" + str(epoch) + ",batch" + str(batch) + ",loss is " + str(loss) + ",Accuracy in train is" + str(acc))
        if epoch <= 30:
            saver.save(sess, "net1/my-model", global_step=epoch)
        else:
            saver.save(sess, "net2/my-model", global_step=epoch)
    coord.request_stop()
    coord.join(threads)
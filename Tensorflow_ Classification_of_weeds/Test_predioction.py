import Loading_images
import tensorflow as tf
import matplotlib.pyplot as plt
import Loading_images

import numpy as np
"""
    测试模型模块
"""
batch_xs, batch_ys = Loading_images.Load_image(224, 1)
import os

with tf.Session() as sess:

    saver = tf.train.import_meta_graph('./net2/my-model-39.meta')
    saver.restore(sess, './net2/my-model-39')
    sess.run(tf.local_variables_initializer())

    """恢复图和参数"""
    graph = tf.get_default_graph()
    net = tf.get_collection('pred_network')[0]
    accuracy = graph.get_tensor_by_name('accuracy:0')
    x = graph.get_tensor_by_name('x:0')
    y = graph.get_tensor_by_name('y:0')
    keep_prob = graph.get_tensor_by_name('prob:0')
    h_conv1 = graph.get_tensor_by_name('h_conv1:0')

    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    mulu = ['Black-grass', 'Scentless Mayweed', 'Charlock', 'Cleavers', 'Small-flowered Cranesbill','Shepherds Purse','Loose Silky-bent','Sugar beet','Fat Hen','Common Chickweed','Maize','Common wheat']
    list = []

    for _ in range(474):
        batch_x_test, batch_y_test = sess.run([batch_xs, batch_ys])
        acc = sess.run(net, feed_dict={x: batch_x_test, keep_prob: 1})
        n = np.argmax(acc)
        list.append(mulu[n])
    print(list)
    dataset_dir = './ceshi_dataset/1/'
    dataset = []
    for _ in os.listdir(dataset_dir):
        dataset.append(_)
    print(dataset)
    print('==============')
    for _ in range(474):
        print(dataset[_][:-4]+","+list[_])
    print('==============')


    coord.request_stop()
    coord.join(threads)
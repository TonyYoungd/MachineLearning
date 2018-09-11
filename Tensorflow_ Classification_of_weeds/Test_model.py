import Loading_images
import tensorflow as tf
import matplotlib.pyplot as plt
import Loading_images

"""
    测试模型模块
"""
batch_xs, batch_ys = Loading_images.Load_test_images(224, 10)

with tf.Session() as sess:

    saver = tf.train.import_meta_graph('./model/my-model-30.meta')
    saver.restore(sess, './model/his/my-model-30')
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
    for e in range(8):
        sum = 0.0
        for _ in range(100):
            batch_x_test, batch_y_test = sess.run([batch_xs, batch_ys])
            acc = sess.run(accuracy, feed_dict={x: batch_x_test, y: batch_y_test, keep_prob: 1})
            sum += acc
        print(sum/100)
    coord.request_stop()
    coord.join(threads)
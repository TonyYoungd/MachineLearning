# -*- coding:utf-8 -*-
"""
    为模型读取文件
"""
import tensorflow as tf
import Preprocess_image


"""读取训练数据"""

def Load_image(image_size, batch_size):
    # 神经网络输入层的大小
    IMAGE_SIZE = image_size
    # 最大队列长度
    MIN_AFTER_DEQUEUE = 500
    # 每一批的大小
    BATCH_SIZE = batch_size
    # 创建队列
    files = tf.train.match_filenames_once("./ceshi_dataset/image_train*.tfrecord")
    filename_queue = tf.train.string_input_producer(files, shuffle=False)
    # 从队列中读取图形做预处理
    reader = tf.TFRecordReader()
    _, serialized_example = reader.read(filename_queue)
    features = tf.parse_single_example(
        serialized_example,
        features={
            'image': tf.FixedLenFeature([], tf.string),
            'label': tf.FixedLenFeature([], tf.int64),
        }
    )
    image = features['image']
    label = features['label']
    # 从原始图形数据解析出像素矩阵, 并根据图像尺寸还原图形
    decoded_image = tf.image.decode_png(image, 3)
    decoded_image = tf.image.convert_image_dtype(decoded_image, dtype=tf.float32)
    # 定义神经网络输入层的大小
    image_size = IMAGE_SIZE
    # 处理图像
    distorted_image = Preprocess_image.preprocess_for_train(decoded_image, image_size, image_size, None)
    label = tf.one_hot(label, 12, 1, 0)
    # 将处理够的图像和标签数据通过tf.train.shuffle_batch整理成神经网络训练时需要的batch
    min_after_dequeue = MIN_AFTER_DEQUEUE
    batch_size = BATCH_SIZE
    capacity = min_after_dequeue + 3*batch_size  # 队列的最大容量
    image_batch, label_batch = tf.train.batch([distorted_image, label], batch_size=batch_size, capacity=capacity)
    return image_batch, label_batch



"""读取测试数据"""

# 参数：传入图像的大小
def Load_test_images(image_size, batch_size):
    IMAGE_SIZE = image_size
    # 最大队列长度
    MIN_AFTER_DEQUEUE = 500
    # 每一批的大小
    BATCH_SIZE = batch_size
    # 创建队列
    files = tf.train.match_filenames_once("./Data/image_test*.tfrecord")
    filename_queue = tf.train.string_input_producer(files, shuffle=False)
    # 从队列中读取图形做预处理
    reader = tf.TFRecordReader()
    _, serialized_example = reader.read(filename_queue)
    features = tf.parse_single_example(
        serialized_example,
        features={
            'image': tf.FixedLenFeature([], tf.string),
            'label': tf.FixedLenFeature([], tf.int64),
        }
    )
    image = features['image']
    label = features['label']
    # 从原始图形数据解析出像素矩阵, 并根据图像尺寸还原图形
    decoded_image = tf.image.decode_png(image, 3)
    decoded_image = tf.image.convert_image_dtype(decoded_image, dtype=tf.float32)
    # 定义神经网络输入层的大小
    image_size = IMAGE_SIZE
    # 处理图像--->统一图像的大小
    distorted_image = Preprocess_image.preprocess_for_train(decoded_image, image_size, image_size, None)
    label = tf.one_hot(label, 12, 1, 0)
    # 将处理够的图像和标签数据通过tf.train.shuffle_batch整理成神经网络训练时需要的batch
    min_after_dequeue = MIN_AFTER_DEQUEUE
    batch_size = BATCH_SIZE
    capacity = min_after_dequeue + 3 * batch_size  # 队列的最大容量
    image_batch_test, label_batch_test = tf.train.shuffle_batch([distorted_image, label], min_after_dequeue = MIN_AFTER_DEQUEUE, batch_size=batch_size, capacity=capacity)
    return image_batch_test, label_batch_test
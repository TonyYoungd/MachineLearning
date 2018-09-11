# -*- coding:utf-8 -*-
"""
    图像预处理
"""
import tensorflow as tf
import numpy as np

def preprocess_for_train(image, height, width, bbox):
    # 如果没有标注框，则认为整个图像就是需要关注的部分
    if bbox is None:
        bbox = tf.constant([0.0, 0.0, 1.0, 1.0])

    # 转换图像张量类型
    if image.dtype != tf.float32:
        image = tf.image.convert_image_dtype(image, dtype=tf.float32)
    image = tf.image.resize_images(image, size=[height, width], method=np.random.randint(4))
    
    # 随机左右翻转图像
    #distored_image = tf.image.random_flip_left_right(image)

    # 随机上下翻转
    #　distored_image = tf.image.random_flip_up_down(distored_image)

    return image
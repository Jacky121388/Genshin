import os
import random
import shutil
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt  # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片


def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)


def copy_file(file_dir):
    path_dir = os.listdir(file_dir)  # 获取图片原始路径
    file_num = len(path_dir)
    pick_num = 8
    sample = random.sample(path_dir, pick_num)  # 随机选取pick_num数量的样本图
    print(sample)
    for name in sample:
        shutil.copy(file_dir + name, tar_dir + name)
    return sample


def show_images(images, title):
    for i in range(len(images)):
        plt.subplot(2, 4, i+1)
        plt.imshow(images[i])
        plt.title(title[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()


if __name__ == '__main__':
    file_direction = "./source/"
    tar_dir = "./result/"
    del_file(tar_dir)
    sample_list = copy_file(file_direction)
    src = []
    titles = []
    for i in sample_list:
        a = mpimg.imread("source/" + i)
        src.append(a)
        titles.append(i[:-4])
    show_images(src, titles)

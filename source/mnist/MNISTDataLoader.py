import os
import struct
import numpy as np
from array import array

Class MNISTDataLoader(object):
    def __init__(self, source_path)):
        self.train_img_path = os.path.join(source_path, 'train-images-idx3-ubyte')
        self.train_lbl_path = os.path.join(source_path, 'train-labels-idx1-ubyte')
        self.test_img_path = os.path.join(source_path, 't10k-images-idx3-ubyte')
        self.test_lbl_path = os.path.join(source_path, 't10k-labels-idx1-ubyte')

    def read_images_labels(dataset="train"):
        img_path = ""
        lbl_path = ""
        if dataset is "train":
            img_path = self.train_img_path
            lbl_path = self.train_lbl_path
        elif dataset is "test":
            img_path = self.test_img_path
            lbl_path = self.test_lbl_path
        else:
            raise ValueError, "dataset must be 'testing' or 'training'"

        labels = []
        with open(lbl_path, 'rb') as file:
            magic, size = struct.unpack(">II", file.read(8))
            if magic != 2049:
                raise ValueError('Magic number mismatch, expected 2049, got {}'.format(magic))
            labels = array("B", file.read())        
        
        with open(img_path, 'rb') as file:
            magic, size, rows, cols = struct.unpack(">IIII", file.read(16))
            if magic != 2051:
                raise ValueError('Magic number mismatch, expected 2051, got {}'.format(magic))
            image_data = array("B", file.read())        
        
            images = []
            for i in range(size):
                images.append([0] * rows * cols)
            for i in range(size):
                img = np.array(image_data[i * rows * cols:(i + 1) * rows * cols])
                img = img.reshape(28, 28)
                images[i][:] = img            
        
        return images, labels

    def load_data(self):
        x_train, y_train = self.read_images_labels("train")
        x_test, y_test = self.read_images_labels("test")
        return (x_train, y_train),(x_test, y_test)  
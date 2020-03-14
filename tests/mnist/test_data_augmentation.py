import numpy as np

from src.mnist import data_augmentation as aug
from src.mnist import show_mnist as img


def test_get_augmented_dataset():
    X_train, X_test, y_train, y_test = aug.get_augmented_dataset()

    original_index = 0
    shifted_index = 60000

    datas = np.concatenate(
        [[X_train[original_index]], [X_train[shifted_index]]])
    np.shape(len(datas))
    img.show_multi(datas, (2, 1))

import numpy as np

from .load_mnist import download_mnist
from .shift_mnist import shift_right
from .shift_mnist import shift_left
from .shift_mnist import shift_up
from .shift_mnist import shift_down


def get_augmented_dataset():
    X, y = download_mnist()

    train_X, test_X, train_y, test_y = \
        X[:60000], X[60000:], y[:60000], y[60000:]

    r_X, r_y = shift_right(train_X, train_y)
    l_X, l_y = shift_left(train_X, train_y)
    u_X, u_y = shift_up(train_X, train_y)
    d_X, d_y = shift_down(train_X, train_y)

    new_X = np.concatenate([r_X, l_X, u_X, d_X])
    new_y = np.concatenate([r_y, l_y, u_y, d_y])

    return new_X, test_X, new_y, test_y

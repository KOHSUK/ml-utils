from scipy.ndimage.interpolation import shift


def shift_left(X, y):
    shifted_X = shift(X, [0, -1], cval=0)
    return shifted_X, y


def shift_right(X, y):
    shifted_X = shift(X, [0, 1], cval=0)
    return shifted_X, y


def shift_up(X, y):
    shifted_X = shift(X, [-1, 0], cval=0)
    return shifted_X, y


def shift_down(X, y):
    shifted_X = shift(X, [1, 0], cval=0)
    return shifted_X, y

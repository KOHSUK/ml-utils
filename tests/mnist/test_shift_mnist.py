from src.mnist import load_mnist
from src.mnist import show_mnist


def test():
    X, y = load_mnist.download_mnist()
    some_index = 0
    some_digit = X[some_index]
    show_mnist.show_one(some_digit)

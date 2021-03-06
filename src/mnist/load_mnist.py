from sklearn.datasets import fetch_openml


def download_mnist():
    mnist = fetch_openml('mnist_784', version=1)
    X, y = mnist["data"], mnist["target"]
    return X, y

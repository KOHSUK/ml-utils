import matplotlib.pyplot as plt


def show_one(digit):
    plot_digit(digit)


def show_multi(datas, shape):

    if len(datas) > shape[0] * shape[1]:
        raise ValueError()

    # 描画領域を確保
    fig = plt.figure()

    axes = [fig.add_subplot(shape[0], shape[1], index)
            for index in range(1, len(datas) + 1)]

    index = 0
    for ax in axes:
        image = datas[index].reshape(28, 28)
        ax.imshow(image, cmap="binary")
        ax.axis("off")
        index += 1

    plt.show()


def plot_digit(digit):
    digit_image = digit.reshape(28, 28)
    plt.imshow(digit_image, cmap="binary")
    plt.axis("off")
    plt.show()

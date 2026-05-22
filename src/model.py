import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def compute_loss(y_true, y_pred):

    epsilon = 1e-9

    loss = -np.mean(
        y_true * np.log(y_pred + epsilon)
        +
        (1 - y_true) * np.log(1 - y_pred + epsilon)
    )
    return loss
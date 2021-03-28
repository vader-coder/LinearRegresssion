import numpy as np

ndarray = np.ndarray

def partialDerivaitiveWithRespectToSlope(m: float, b: float, x: ndarray, y: ndarray) -> float:
    return np.sum((-2*y + 2*(m*x + b))*x)


def partialDerivaitiveWithRespectToYIntercept(m: float, b: float, x: ndarray, y: ndarray) -> ndarray:
    return np.sum(-2*y*b + 2*(m*x + b)*x)

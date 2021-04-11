import numpy as np

ndarray = np.ndarray

def partialDerivaitiveWithRespectToSlope(m: float, b: float, x: ndarray, y: ndarray) -> float:
    return np.sum(2*x*(y - (m*x + b)))
#return np.sum((-2*y + 2*(m*x + b))*x)

def partialDerivaitiveWithRespectToYIntercept(m: float, b: float, x: ndarray, y: ndarray) -> ndarray:
    return np.sum(2*(y - (m*x + b)))
#return np.sum(-2*y*b + 2*(m*x + b)*x)

def f(m: float, b: float, x: ndarray) -> ndarray:
    return m*x + b

def error(m: float, b: float, x: ndarray, y: ndarray) -> float:
    diff = y - f(m, b, x)
    return np.sum(diff*diff)

def numericPartialSlope(m: float, b: float, x: ndarray, y: ndarray) -> float:
    return 10000*(error(m+0.0001, b, x, y) - error(m, b, x, y))

def numericPartialYIntercept(m: float, b: float, x: ndarray, y: ndarray) -> float:
    return 10000*(error(m, b+0.0001, x, y) - error(m, b, x, y))

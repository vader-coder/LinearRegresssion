import partialDerivatives as pd

np = pd.np
ndarray = np.ndarray

def gradientOfLeastSquaresError(m: float, b: float, x: ndarray, y: ndarray) -> ndarray:
    #returns [partial w/ respect to m(m, b), partial w/ respect to b(m, b) ]
    return np.array([pd.partialDerivaitiveWithRespectToSlope(m, b, x, y), pd.partialDerivaitiveWithRespectToYIntercept(m, b, x, y)])


def numericGradient(m: float, b: float, x: ndarray, y: ndarray) -> ndarray:
    return np.array([pd.numericPartialSlope(m, b, x, y), pd.numericPartialYIntercept(m, b, x, y)])

def isNotZeroVector(v: ndarray) -> bool:
    #if gradient is near zero vector, we want to stop descending. 
    if np.any(v):
        return False
    return True

def leastSquaresRegressionLine(x: ndarray, y: ndarray) -> ndarray:
	#returns [m, b] representing y = mx + b of line of best fit
    v = np.random.rand(1, 2)#row vector
    stepSize = 0.001
    slope = v[0][0]
    intercept = v[0][1]
    # gradientOfLeastSquaresError(slope, intercept, x, y)
    gradient = numericGradient(slope, intercept, x, y)
    counter = 0
    while (isNotZeroVector(gradient) and counter < 100000):
        slope = v[0][0]
        intercept = v[0][1]
        v = v - stepSize*numericGradient(slope, intercept, x, y)
        counter += 1
    return v








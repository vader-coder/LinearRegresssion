import partialDerivatives as pd

np = pd.np
ndarray = np.ndarray

def gradientOfLeastSquaresError(m: float, b: float, x: ndarray, y: ndarray) -> ndarray:
    #returns [partial w/ respect to m(m, b), partial w/ respect to b(m, b) ]
    return np.array([pd.partialDerivaitiveWithRespectToSlope(m, b, x, y), pd.partialDerivaitiveWithRespectToYIntercept(m, b, x, y)])

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
    gradient = gradientOfLeastSquaresError(slope, intercept, x, y)
    counter = 0
    while (isNotZeroVector(gradient) and counter < 5):
        slope = v[0][0]
        intercept = v[0][1]
        v = v - stepSize*gradientOfLeastSquaresError(slope, intercept, x, y)
        counter += 1
    return v








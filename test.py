import partialDerivatives as pd
import numpy as np
import myRegression as reg

x = np.random.rand(1, 3)
y = np.random.rand(1, 3)
m = 1
b = 1

pSlope = pd.partialDerivaitiveWithRespectToSlope(m, b, x, y)
pIntercept = pd.partialDerivaitiveWithRespectToYIntercept(m, b, x, y)

print([x, y])
print([pSlope, pIntercept])
print([type(pSlope), type(pIntercept)])
print(reg.gradientOfLeastSquaresError(m, b, x, y))
print(reg.leastSquaresRegressionLine(x, y))

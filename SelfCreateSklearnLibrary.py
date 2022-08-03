import numpy as np

class LinearRegression():
	def fit(self, x, y):
		n=len(x)
		xl=[]
		yl=[]
		for i in range(n):
			xl.append([1]+x[i])
			yl.append([y[i]])
		xl=np.matrix(xl)
		yl=np.matrix(yl)
		
		b=np.dot(np.dot(np.dot(xl.T,xl).I,xl.T),yl)
		
		self.coef=b[1:]
		self.intercept=b[0]
			
	def predict(self, xtest):
		return [float(self.intercept[0]+np.sum(np.multiply(self.coef.T,np.matrix([xtest[i]])))) for i in range(len(xtest))]

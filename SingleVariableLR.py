class LinearRegression():
	def init(self):
		self.coef=0
		self.intercept=0
		
	def fit(self, x, y):
		sumxy=0
		sumx=0
		sumy=0
		sumxsq=0
		n=len(x)
		
		for i in range(n):
			sumxy+=(x[i]*y[i])
			sumx+=x[i]
			sumy+=y[i]
			sumxsq+=x[i]**2
			
		self.coef=(sumxy-(sumx*sumy)/n)/(sumxsq-(sumx**2)/n)
		self.intercept=sumy/n-self.coef*(sumx/n)
			
	def predict(self, x):
		return [self.coef*value+self.intercept for value in x]

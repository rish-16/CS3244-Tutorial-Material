import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class LinearRegressionClassifier(object):
    def __init__(self):
        self.alpha = 1e-2
        self.iterations = 1000
        self.losses = []
        self.weights = None
        self.bias = None
        
    def forward(self, x):
        return np.dot(x, self.weights) + self.bias
    
    def backward(self, x, y_hat, y):
        m, d = x.shape
        y_hat = y_hat.reshape([m])
        y = y.reshape([m])
        
        partial_w = (1 / x.shape[0]) * (2 * np.dot(x.T, (y_hat - y)))
        partial_b = (1 / x.shape[0]) * (2 * np.sum(y_hat - y))
        
        return [partial_w, partial_b]

    def MSELoss(self, y_hat, y):
        return (1/y.shape[0]) * np.sum(np.square(y_hat - y))
    
    def update(self, grad):
        self.weights = self.weights - (self.alpha * grad[0])
        self.bias = self.bias - (self.alpha * grad[1])
        
    def fit(self, x, y):
        self.weights = np.random.uniform(0, 1, x.shape[1])
        self.bias = np.random.uniform(0, 1, 1)
        self.losses = []
        
        for i in range(self.iterations):
            y_hat = self.forward(x)
            
            loss = self.MSELoss(y_hat, y)
            self.losses.append(loss)
            
            grad = self.backward(x, y_hat, y)
            
            self.update(grad)
        
    def predict(self, x):
        return x
    
    def plot(self):
        plt.plot(range(self.iterations), self.losses, color="red")
        plt.title("Loss on Iris Dataset for {} iterations".format(self.iterations))
        plt.xlabel("Iteration")
        plt.ylabel("Loss")
        plt.show()

cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = pd.read_csv('./data/iris.csv', skiprows=1, header=0, names=cols)

# replace class strings with integer indices
df['class'] = df['class'].str.replace('Iris-setosa', '0')
df['class'] = df['class'].str.replace('Iris-versicolor', '1')
df['class'] = df['class'].str.replace('Iris-virginica', '2')
df['class'] = df['class'].map(lambda x : int(x))

X = df.iloc[:, :-1].values
Y = df.iloc[:, -1].values.reshape(-1, 1)
X = np.array(X)
Y = np.array(Y)

linreg = LinearRegressionClassifier()
linreg.fit(X, Y)
linreg.plot()
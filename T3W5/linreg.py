import numpy as np
import pandas as pd

class LinearRegressionClassifier(object):
    def __init__(self, dim):
        self.weights = np.random.rand(dim)
        self.bias = np.random.rand(1)
        self.alpha = 1e-2
        
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    def sigmoid_prime(self, z):
        return self.sigmoid(z) * (1 - self.sigmoid(z))
        
    def forward(self, x):
        return np.matmul(self.weights.T, x) + self.bias
    
    def backward(self, x):
        return x

    def MSELoss(self, y_hat, y):
        return np.sum(np.square(y_hat - y)) / y.shape[0]
    
    def update(self, grad):
        self.weights = self.weights - (self.alpha * grad[0])
        self.bias = self.bias - (self.alpha * grad[1])
        
    def fit(self, x, y):
        y_hat = self.forward(x)
        loss = self.MSELoss(y_hat, y)
        grad = self.backward(x, y_hat, y)
        
        self.update(grad)
        
    def predict(self, x):
        return x
    
linreg = LinearRegressionClassifier(6)
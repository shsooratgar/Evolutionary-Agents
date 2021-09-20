import numpy as np
import math


class NeuralNetwork():

    def __init__(self, layer_sizes):
        # TODO
        # layer_sizes example: [4, 10, 2]
        self.layer0 = layer_sizes[0]
        self.layer1 = layer_sizes[1]
        self.layer2 = layer_sizes[2]

        self.w1 = np.random.randn(self.layer1, self.layer0)
        self.w2 = np.random.randn(self.layer2, self.layer1)

        self.b1 = np.zeros((layer_sizes[1], 1))
        self.b2 = np.zeros((layer_sizes[2], 1))
        pass

    def activation(self, x):
        # TODO
        return 1 / (1 + math.exp(-x))
        # return x

    def forward(self, x):
        # TODO
        # x example: np.array([[0.1], [0.2], [0.3]])
        z2 = self.w1.dot(x)
        z2 = np.add(z2, self.b1)
        a2 = np.array([self.activation(xi) for xi in z2]).reshape(self.layer1 , 1)

        z3 = self.w2.dot(a2)
        z3 = np.add(z3, self.b2)
        a3 = np.array([self.activation(xi) for xi in z3]).reshape(self.layer2, 1)
        # pass
        return a3


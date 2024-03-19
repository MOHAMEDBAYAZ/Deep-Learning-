import numpy as np

# Define input data
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Define weights and biases
W = np.array([[1, 1], [1, 1]])
b = np.array([0, 0])

# Calculate net input
net_input = np.dot(X, W) + b

# ReLU activation function
output = np.maximum(0, net_input)

print("Output:")
print(output)


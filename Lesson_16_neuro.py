import numpy as np
import scipy.special
import matplotlib.pyplot as plt

class Neuro:
    def __init__(self, inputNodes, hiddenNodes, outputNodes, learningRate):
        self.iNodes = inputNodes
        self.hNodes = hiddenNodes
        self.oNodes = outputNodes

        self.lr = learningRate

        self.wih = np.random.normal(0.0, pow(self.hNodes, -0.5), (self.hNodes, self.iNodes))
        self.who = np.random.normal(0.0, pow(self.oNodes, -0.5), (self.oNodes, self.hNodes))

        self.activation_function = lambda x: (scipy.special.expit(x))
        self.dev = lambda x: (x*(1.0-x))

    def train(self, inputs_list, target_list):
        inputs = np.array(inputs_list, ndmin=2).T
        targets = np.array(target_list, ndmin=2).T

        hidden_inputs = np.dot(self.wih, inputs)
        hidden_output = self.activation_function(hidden_inputs)
        final_inputs = np.dot(self.who, hidden_output)
        final_output = self.activation_function(final_inputs)

        output_errors = targets - final_output
        hidden_errors = np.dot(self.who.T, output_errors)

        self.who += self.lr * np.dot((output_errors * self.dev(final_output)), np.transpose(hidden_output))
        self.whi += self.lr * np.dot((hidden_errors * self.dev(hidden_output)), np.transpose(inputs))

    def check(self, input_list):
        inputs = np.array(input_list, ndmin=2).T
        hidden_inputs = np.dot(self.wih, inputs)
        hidden_output = self.activation_function(hidden_inputs)
        final_inputs = np.dot(self.who, hidden_output)
        final_output = self.activation_function(final_inputs)

        return final_output

input_nodes = 784
hidden_nodes = 200
outputs_nodes = 10

learning_rate = 0.01

n = Neuro(input_nodes, hidden_nodes, outputs_nodes, learning_rate)

data_file = open('mnist_train_100.csv', 'r')
data_list = data_file.readlines()
data_file.close()
print(data_list[1])
all_values = data_list[59].split(',')
img_array = np.asfarray(all_values[1:]).reshape(28,28)
plt.imshow(img_array, cmap='Greys', interpolation='None')
plt.show()

for record in data_list:
    value = record.split(',')
    input = (np.asfarray(all_values[1:])/255.0*0.99)+0.1
    targets = np.zeros(outputs_nodes)+0.01
    targets[int(value[0])] = 0.99
    n.train(input, target)
    pass

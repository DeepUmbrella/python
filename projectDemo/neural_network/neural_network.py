import numpy

import scipy.special


class Neural_Network:

    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        self.learning_rate = learning_rate

        self.wih = numpy.random.normal(
            0.0, pow(self.hidden_nodes, -0.5), (self.hidden_nodes, self.input_nodes))

        self.who = numpy.random.normal(
            0.0, pow(self.output_nodes, -0.5), (self.output_nodes, self.hidden_nodes))

        # activation_function
        self.activation_function = lambda x: scipy.special.expit(x)

    def train(self, inputs_list, targets_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        hidden_inputs = numpy.dot(self.wih, inputs)

        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = numpy.dot(self.who, hidden_outputs)

        final_outputs = self.activation_function(final_inputs)

        output_errors = targets - final_outputs

        hidden_errors = numpy.dot(self.who.T, output_errors)

        self.who += self.learning_rate * numpy.dot((output_errors * final_outputs *
                                                    (1.0 - final_outputs)), numpy.transpose(hidden_outputs))

        self.wih += self.learning_rate * numpy.dot((hidden_errors * hidden_outputs *
                                                    (1.0 - hidden_outputs)), numpy.transpose(inputs))
        return numpy.array(final_outputs).T.flatten()

    def query(self, inputs_list):

        inputs = numpy.array(inputs_list, ndmin=2).T

        hidden_inputs = numpy.dot(self.wih, inputs)

        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = numpy.dot(self.who, hidden_outputs)

        final_outputs = self.activation_function(final_inputs)

        return numpy.argmax(numpy.array(final_outputs).T.flatten())


if __name__ == "__main__":

    input_nodes = 3
    hidden_nodes = 3
    output_nodes = 3
    learning_rate = 0.1

    targets_list = [0.49622777, 0.51395492, 0.56544434]

    nn = Neural_Network(input_nodes, hidden_nodes,
                        output_nodes, learning_rate)

    print(nn.wih)
    print(numpy.array(nn.who).T)
    print(nn.who)

    test = nn.query([1.0, 3.0, 5.0])
    nn.train([1.0, 3.0, 5.0], [1.0, 0.5, 0.8])
    print(test, "test")

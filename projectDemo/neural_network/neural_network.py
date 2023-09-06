import numpy

import scipy.special


class Neural_Network:

    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        self.learning_rate = learning_rate

        self.wih = [[1, 2], [3, 4]]
        # self.wih = (numpy.random.rand(
        #     self.hidden_nodes, self.input_nodes) - 0.5)
        # self.who = (numpy.random.rand(
        #     self.output_nodes, self.hidden_nodes) - 0.5)
        self.who = [[3, 4], [1, 2]]
        self.wih_pow = numpy.random.normal(
            0.0, pow(self.hidden_nodes, -0.5), (self.hidden_nodes, self.input_nodes))

        self.wio_pow = numpy.random.normal(
            0.0, pow(self.output_nodes, -0.5), (self.output_nodes, self.hidden_nodes))

        # activation_function
        # self.activation_function = lambda x: scipy.special.expit(x)
        self.activation_function = lambda x: numpy.array(x)

    def train(self, inputs_list, targets_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        hidden_inputs = numpy.dot(self.wih, inputs)

        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = numpy.dot(self.who, hidden_outputs)

        final_outputs = self.activation_function(final_inputs)

        output_errors = targets - final_outputs
        print(output_errors, "output_errors")

        pass

    def query(self, inputs_list):

        inputs = numpy.array(inputs_list, ndmin=2).T

        hidden_inputs = numpy.dot(self.wih, inputs)

        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = numpy.dot(self.who, hidden_outputs)

        final_outputs = self.activation_function(final_inputs)

        return final_outputs


if __name__ == "__main__":

    input_nodes = 3
    hidden_nodes = 3
    output_nodes = 3
    learning_rate = 0.1

    targets_list = [0.49622777, 0.51395492, 0.56544434]

    nn = Neural_Network(input_nodes, hidden_nodes,
                        output_nodes, learning_rate)

    # print(nn.wih)
    # print(numpy.array(nn.who).T)
    # print(nn.who)

    # test = nn.query([1.0, 3.0])
    # nn.train([1.0, 3.0], [1.0, 1.0])
    # print(test, "test")

    w = [[1, 4], [2, 1]]

    out = numpy.dot(w, [1, 1])

    print(out)

import unittest

import numpy as np

from NeuralNetwork import NeuralNetwork


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.red = NeuralNetwork(2, (1, 1))
        self.layer1 = self.red.layers[0]
        self.layer2 = self.red.layers[1]
        self.neuron1 = self.layer1.neurons[0]
        self.neuron2 = self.layer2.neurons[0]
        self.neuron1.weights = [0.4, 0.3]
        self.neuron2.weights = [0.3]
        self.neuron1.bias = 0.5
        self.neuron2.bias = 0.4
        self.neuron1.lr = 0.1
        self.neuron2.lr = 0.1

        self.tc2 = NeuralNetwork(2, (2, 2))
        self.tclayer1 = self.tc2.layers[0]
        self.tclayer2 = self.tc2.layers[1]
        self.tcneuron1 = self.tclayer1.neurons[0]
        self.tcneuron2 = self.tclayer1.neurons[1]
        self.tcneuron3 = self.tclayer2.neurons[0]
        self.tcneuron4 = self.tclayer2.neurons[1]
        self.tcneuron1.weights = [0.7, 0.3]
        self.tcneuron2.weights = [0.3, 0.7]
        self.tcneuron3.weights = [0.2, 0.3]
        self.tcneuron4.weights = [0.4, 0.2]
        self.tcneuron1.bias = 0.5
        self.tcneuron2.bias = 0.4
        self.tcneuron3.bias = 0.3
        self.tcneuron4.bias = 0.6
        self.tcneuron1.lr = 0.1
        self.tcneuron2.lr = 0.1
        self.tcneuron3.lr = 0.1
        self.tcneuron4.lr = 0.1


    def testCase1(self):
        self.red.realTraining([[1, 1]], [[1]])
        print(round(self.neuron1.weights[0], 15))
        print(round(self.neuron2.weights[0], 15))
        print(round(self.neuron2.weights[0], 15))
        self.assertEqual(round(self.neuron1.weights[0], 15), 0.402101508999489)
        self.assertEqual(round(self.neuron1.weights[1], 15), 0.302101508999489)
        self.assertEqual(round(self.neuron2.weights[0], 15), 0.330262548639919)

    def testCase2(self):
        self.tc2.realTraining([[1, 1]], [[1, 1]])

        print("neurona 1")
        self.assertEqual(round(self.tcneuron1.weights[0], 17), 0.7025104485493278)
        self.assertEqual(round(self.tcneuron1.weights[1], 17), 0.3025104485493278)
        print("neurona 2")
        self.assertEqual(round(self.tcneuron2.weights[0], 17), 0.30249801135748333)
        self.assertEqual(round(self.tcneuron2.weights[1], 17), 0.7024980113574834)
        print("neurona 3")
        self.assertEqual(round(self.tcneuron3.weights[0], 17), 0.22994737881955657)
        self.assertEqual(round(self.tcneuron3.weights[1], 17), 0.32938362863950127)
        print("neurona 4")

        self.assertEqual(round(self.tcneuron4.weights[0], 17), 0.41943005652646226)
        self.assertEqual(round(self.tcneuron4.weights[1], 17), 0.21906429169838573)

        def goodSetUp(self):
            self.assertIsNotNone(self.red)
            self.assertEqual(len(self.red.layers), 1)

            for layer in self.red.layers:
                self.assertIsNotNone(layer)
                self.assertEqual(layer.neurons, 1)
                for neuron in layer:
                    self.assertIsNotNone(neuron)

        n1_desired_b = 0.5025104485493278
        n2_desired_b = 0.40249801135748337
        n3_desired_b = 0.3366295422515899
        n4_desired_b = 0.6237654881509048

        self.assertEqual(round(self.tcneuron1.bias, 17), n1_desired_b)
        self.assertEqual(round(self.tcneuron2.bias, 17), n2_desired_b)
        self.assertEqual(round(self.tcneuron3.bias, 17), n3_desired_b)
        self.assertEqual(round(self.tcneuron4.bias, 17), n4_desired_b)

    def testgoodSetUp(self):
        self.assertIsNotNone(self.red)
        self.assertEqual(len(self.red.layers), 2)

        for layer in self.red.layers:
            self.assertIsNotNone(layer)
            self.assertEqual(len(layer.neurons), 1)
            for neuron in layer.neurons:
                self.assertIsNotNone(neuron)

if __name__ == '__main__':
    unittest.main()

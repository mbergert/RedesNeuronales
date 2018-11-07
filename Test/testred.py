import unittest

from NeuralNetwork import NeuralNetwork


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.red = NeuralNetwork(2, (1,1))
        self.layer1= self.red.layers[0]
        self.layer2=self.red.layers[1]
        self.neuron1= self.layer1.neurons[0]
        self.neuron2 = self.layer2.neurons[0]
        self.neuron1.weights= [0.4, 0.3]
        self.neuron2.weights= [0.3]
        self.neuron1.bias= 0.5
        self.neuron2.bias= 0.4
        self.neuron1.lr= 0.5
        self.neuron2.lr= 0.5



  
  

    def testCase1(self):

        self.red.realTraining([[1, 1]], [[1]])
        print(round(self.neuron1.weights[0], 15))
        print(round(self.neuron2.weights[0], 15))
        print(round(self.neuron2.weights[0], 15))
        self.assertEqual(round(self.neuron1.weights[0], 15), 0.402101508999489)
        self.assertEqual(round(self.neuron1.weights[1], 15), 0.302101508999489)
        self.assertEqual(round(self.neuron2.weights[0], 15), 0.330262548639919)

if __name__ == '__main__':
    unittest.main()

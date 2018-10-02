import unittest

from Perceptron.Perceptron import NanD, Or, And, Sum


class MyTestCase(unittest.TestCase):
    def test_feed_NAND(self):
        NAND=NanD()
        AND=Or()
        AND= And()
        #Hay que testear todas las compuertas para los casos
        #00,01,10,11
        #Testeo de los nands
        self.assertEqual(NAND.feed([0, 0]), 1)
        self.assertEqual(NAND.feed([0, 1]), 1)
        self.assertEqual(NAND.feed([1, 0]), 1)
        self.assertEqual(NAND.feed([1, 1]), 0)


    def test_feed_OR(self):
        OR = Or()
        # Hay que testear todas las compuertas para los casos
        # 00,01,10,11
        self.assertEqual(OR.feed([0, 0]), 0)
        self.assertEqual(OR.feed([0, 1]), 1)
        self.assertEqual(OR.feed([1, 0]), 1)
        self.assertEqual(OR.feed([1, 1]), 1)

    def test_feed_AND(self):
        AND = And()
        # Hay que testear todas las compuertas para los casos
        # 00,01,10,11
        self.assertEqual(AND.feed([0, 0]), 0)
        self.assertEqual(AND.feed([0, 1]), 0)
        self.assertEqual(AND.feed([1, 0]), 0)
        self.assertEqual(AND.feed([1, 1]), 1)

    def test_sum(self):
        SUM=Sum()
        self.assertEqual(SUM.feed(0, 0), (0,0))
        self.assertEqual(SUM.feed(0, 1), (1,0))
        self.assertEqual(SUM.feed(1, 0), (1,0))
        self.assertEqual(SUM.feed(1, 1),(0,1) )

if __name__ == '__main__':
    unittest.main()

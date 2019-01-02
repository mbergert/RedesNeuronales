from random import randint, random
from copy import deepcopy


# Clase con variables
class FunTree(object):
    # Init crea un arbol al azar dandole valores aleatoriamente respetando una profundidad máxima
    def __init__(self, maxdepth, ops, nterms):
        self.left = None
        self.right = None
        self.data = None
        self.parent = None
        self.ops = ops
        self.terms = []
        # crea los terminales para la creacion
        for i in range(0, nterms):
            self.terms.append(randint(0, 100))
        # Creacion, si es 1 uno añade un nuevo tree, sino, termina.

        gen = random()

        if gen > 0.3 and maxdepth > 0:
            self.data = self.ops[randint(0, len(self.ops) - 1)]
            self.right = FunTree(maxdepth - 1, self.ops, nterms)
            self.right.parent = self
            self.left = FunTree(maxdepth - 1, self.ops, nterms)
            self.left.parent = self
        else:
            if random() > 0.5:
                self.data = str(self.terms[randint(0, len(self.terms) - 1)])
            else:
                self.data="x"


    # Imprime un arbol en forma de operación

    def __str__(self):
        if self.right is None:
            return self.data
        if self.left is None:
            return self.data
        return "(" + self.left.__str__() + " " + self.data + " " + self.right.__str__() + ")"

        # Evalua el resultado de un arbol de operaciones

    def evalTree(self, xval):
        tree= self.__str__()
        tree= tree.replace("x", str(xval))
        return eval(tree)

        # Devuelve la copia de un objeto arbol sin que esté referenciada al objeto orifinal

    def copyTree(self):
        return deepcopy(self)

    def serialize(self):
        if self.right is not None and self.left is not None:
            return self.left.serialize() + [self] + self.right.serialize()
        if self.right is not None:
            return [self] + self.right.serialize()
        if self.left is not None:
            return [self] + self.left.serialize()
        else:
            return [self]

ops = ['*', '+', '-']
terms = ["14", "18", "1", "4", "10", "15", "3", "5"]

a = FunTree(4, ops, 10)
print(a)
print(a.evalTree(5))
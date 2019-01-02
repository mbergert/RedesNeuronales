from random import randint, random
from copy import deepcopy

#Clase creada para tener objetos Tree con los que trabajará el algoritmo genético
class Tree(object):
    #Init crea un arbol al azar dandole valores aleatoriamente respetando una profundidad máxima
    def __init__(self, maxdepth, ops, terms):
        self.left = None
        self.right = None
        self.data = None
        self.parent= None
        self.ops= ops
        self.terms= terms
        # Creacion, si es 1 uno añade un nuevo tree, sino, termina.

        gen = random()

        if gen> 0.3 and maxdepth>0:
            self.data= self.ops[randint(0,len(self.ops)-1)]
            self.right=Tree(maxdepth-1, self.ops, self.terms)
            self.right.parent= self
            self.left=Tree(maxdepth-1, self.ops, self.terms)
            self.left.parent= self
        else:
            self.data = self.terms[randint(0, len(self.terms)-1)]
#Imprime un arbol en forma de operación


    def __str__(self):
        if self.right is None:
            return self.data
        if self.left is None:
            return self.data
        return "(" + self.left.__str__() + " " + self.data + " " + self.right.__str__() + ")"

#Evalua el resultado de un arbol de operaciones
    def evalTree(self):
        return eval(self.__str__())

#Devuelve la copia de un objeto arbol sin que esté referenciada al objeto orifinal
    def copyTree(self):
        return deepcopy(self)

    def serialize(self):
        if self.right is not None and self.left is not None:
            return self.left.serialize() + [self] + self.right.serialize()
        if self.right is not None:
            return  [self] + self.right.serialize()
        if self.left is not None:
            return [self] + self.left.serialize()
        else:
            return [self]





ops=['*', '+','-']
terms= ["14", "18", "1", "4", "10", "15", "3", "5"]

a= Tree(1, ops, terms)
print(a.serialize())
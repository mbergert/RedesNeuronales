from random import randint
from copy import deepcopy

#Clase creada para tener objetos Tree con los que trabajará el algoritmo genético
class Tree(object):
    #Init crea un arbol al azar dandole valores aleatoriamente respetando una profundidad máxima
    def __init__(self, maxdepth):
        self.left = None
        self.right = None
        self.data = None
        self.ops= ['*', '+', '/','-']
        # Creacion, si es 1 uno añade un nuevo tree, sino, termina.

        gen = randint(1, 2)

        if gen==1 and maxdepth>0:
            self.data= self.ops[randint(0,len(self.ops)-1)]
            self.right=Tree(maxdepth-1)
            self.left=Tree(maxdepth-1)
        else:
            self.data = format( randint(0, 100))
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


a= Tree(4)
print(a)
print(a.evalTree())
b=a.copyTree()
a.data= "*"
print(a)
print(b)
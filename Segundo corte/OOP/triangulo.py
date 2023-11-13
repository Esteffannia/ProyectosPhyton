class Triangulo:
    def __init__(self, base, altura, lado):
        self.base=base
        self.altura=altura
        self.lado=lado

    def area(self): 
        print("El area es: ",(self.base*self.altura)/2)

    def perimetro(self):
        print("El perimetro para un triangulo isoceles es:", self.lado*2)
        #print("El perimetro para un triangulo equilatero es:", self.lado*3)
        #print("El perimetro para un triangulo escaleno es: ", self.lado*self.lado*self.lado)

triangulo1=Triangulo(3,5)
area=triangulo1.area()
tri1=Triangulo(2) 
perimetro=tri1.perimetro()

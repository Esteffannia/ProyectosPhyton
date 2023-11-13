class Circulo:
    pi=3.14
    def __init__(self, radio):
        self.radio=radio

    def circunferencia(self):
        print("La circunferencia es: ",2*self.pi*self.radio) 

    def area(self): 
        print("El area es: ",self.pi*(self.radio**2) )
    
    def perimetro(self):
        print("El perimetro es: ", 2*self.pi*self.radio)

circulo=float(input("Escribe el valor del radio: "))
circulo1=Circulo(1) #Se crea el objeto circulo1 de la clase circulo
circulo1.circunferencia()
circulo1.area()
circulo1.perimetro()




    
    
    








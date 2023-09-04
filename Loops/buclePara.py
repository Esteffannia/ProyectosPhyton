import time

cadena = 'Python'

for letra in cadena:
   if letra == 't':
      continue
   print(letra)
   time.sleep(1)

   """ este código recorre cada letra de la cadena 'Python', pero si encuentra la letra 't', 
   la omite y espera 1 segundo antes de continuar con la siguiente letra"""
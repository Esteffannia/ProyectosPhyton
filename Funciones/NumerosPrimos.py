def is_prime(k):
  for i in range(2,k):
    if (k%i) == 0:
      return False
  return True

suma = 0
primos = []
n = int(input('ingrese número => '))
numbers = range(2,n)

if not is_prime(n):
  print('Este número es compuesto')
else:
  for p in numbers:
    if is_prime(p):
      primos.append(p)
      suma += p
  print('el número', n, 'es primo y la suma de todos los primos desde 2 hasta', n, 'es: ', int(suma+n))
  primos.append(n)
  print('la lista de números es: ', primos)
      
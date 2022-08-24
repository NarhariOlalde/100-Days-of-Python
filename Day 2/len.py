print(len("Hola"))

#Conversiones

num_prueba = 123

print(type(num_prueba))

num_prueba_strt = str(num_prueba)

print(type(num_prueba_strt))

#floor division te da el numero entero mas cercano hacia abajo
print(8//3)
print(8/3)

#Y si usamos round, te da el numero entero mas cercano
print(round(8/3))
#Y si le ponemos una coma, te da el numero con decimales hasta donde digas
print(round(8/3,2))

#f string permite usar variables en un string
print(f"Hola {num_prueba}")
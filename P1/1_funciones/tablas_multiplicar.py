'''
    Crear un programa que calcule e imprima cualquier tabla de multiplicar

    Requisitos:
    2.- Sin funciones
'''

def tabla (numero):
    num=numero
    respuesta=""
    for i in range(1, 11):
        multi=num*i
        respuesta+=f"\t{num} X {i} = {multi}\n"
    return respuesta

numero=int(input("Dame el numero de la tabla de multiplicar "))

numero=int(input("Dame el numero de la tabla de multiplicar a calcular: "))
for i in range(1,11):
    multi=numero*i
    print(f"{numero} X {i} = {multi}")

numero=int(input("Dame el numero de la tabla de multiplicar a calcular: "))
p=1
while p <= 10:
    multi=numero*p
    print(f"{numero} X {p} = {multi}")
    p = p + 1

'''
num = int(input("Ingrese la tabla de multiplicar que desee calcular"))
print(f"{num} X 1   =  {num*1 }")
print(f"{num} X 2   =  {num*2 }")
print(f"{num} X 3   =  {num*3 }")
print(f"{num} X 4   =  {num*4 }")
print(f"{num} X 5   =  {num*5 }")
print(f"{num} X 6   =  {num*6 }")
print(f"{num} X 7   =  {num*7 }")
print(f"{num} X 8   =  {num*8 }")
print(f"{num} X 9   =  {num*9 }")
print(f"{num} X 10  =  {num*10}")


print(f"2 X 1  =  {2*1}")
print(f"2 X 2  =  {2*2}")
print(f"2 X 3  =  {2*3}")
print(f"2 X 4  =  {2*4}")
print(f"2 X 5  =  {2*5}")
print(f"2 X 6  =  {2*6}")
print(f"2 X 7  =  {2*7}")
print(f"2 X 8  =  {2*8}")
print(f"2 X 9  =  {2*9}")
print(f"2 X 10 = {2*10}")

dosporuno=2*1
dospordos=2*2
dosportres=2*3
dosporcuatro=2*4
dosporcinco=2*5
dosporseis=2*6
dosporsiete=2*7
dosporocho=2*8
dospornueve=2*9
dospordiez=2*10

print(f"2 X 1  =  {dosporuno}")
print(f"2 X 2  =  {dospordos}")
print(f"2 X 3  =  {dosportres}")
print(f"2 X 4  =  {dosporcuatro}")
print(f"2 X 5  =  {dosporcinco}")
print(f"2 X 6  =  {dosporseis}")
print(f"2 X 7  =  {dosporsiete}")
print(f"2 X 8  =  {dosporocho}")
print(f"2 X 9  =  {dospornueve}")
print(f"2 X 10 =  {dospordiez}")

multi=2*1
print(f"2 X 1 = {multi}")
multi=2*2
print(f"2 X 1 = {multi}")
multi=2*3
print(f"2 X 1 = {multi}")
multi=2*4
print(f"2 X 1 = {multi}")
multi=2*5
print(f"2 X 1 = {multi}")
multi=2*6
print(f"2 X 1 = {multi}")
multi=2*7
print(f"2 X 1 = {multi}")
multi=2*8
print(f"2 X 1 = {multi}")
multi=2*9
print(f"2 X 1 = {multi}")
multi=2*10
print(f"2 X 1 = {multi}")
'''
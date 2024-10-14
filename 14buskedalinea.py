
#______ function para leer vector _______
def leer():
	tam = int(input("Tamanho Vector="))
	return tam
def leerBuscar():
	print("Leer elemento a buscar")
	a = int(input("Valor ="))
	return a
#______ function para generar vector _______
def llenarVector(tamanho):
	V = [0]*n
	for i in range(n):
		x=int(input(f"[{i}]="))
		V[i]=x
	return V
#______ function mostrar vector _______
def mostrar(V, n):
	print("[",end="")
	for i in range(n):
		print(V[i],end=",")
	print("]")
#______ function kparametros ASc. _______
def buscaElemento(V,n):
	data = leerBuscar()
	for j in range(n):
		if  V[j]==data:
			buscar=V[j]
			return buscar,j	
	print("No hay elementos a mostrar")
	return None, -1	
#______ function main _______
n = leer()
print("___________________________________")

vector = llenarVector(n)
print("_____Mostrar Vector Original_____")
mostrar(vector,n)
res, posicion = buscaElemento(vector,n)
print("___________________________________")
print(f" El elemento es = {res}  en la posicion = {posicion}")
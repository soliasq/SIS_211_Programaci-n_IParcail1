
#______ function para leer vector _______
def leer():
	tam = int(input("Tamanho Vector="))
	return tam
def leerParametro():
	print("Leer delimitador del segmento")
	a = int(input("Posicion Inicio ="))
	b = int(input(" Posiion Fonal="))
	return a,b
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
def ordenarParametroAB(V,n):
	inicio, final = leerParametro()
	if  inicio < 0 or final >=n  or inicio >= final:
		print("Índices no válidos.")
		return V
	for i in range(inicio,final+1):
		for j in range(i+1,final+1):
			if V[i] >V[j]:
				aux = V[i]
				V[i] = V[j]
				V[j] = aux
	return V
#______ function main _______
n = leer()
print("___________________________________")
vector = llenarVector(n)
print("_____Mostrar Vector Original_____")
mostrar(vector,n)
res = ordenarParametroAB(vector,n)
print("Ordenar Pares Asc. ")
print("___________________________________")
print(res)
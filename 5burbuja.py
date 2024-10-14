#______ function para leer vector _______
def leer():
    tam = int(input("Tamanho Vector="))
    return tam

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
	


def burbuja(V,n):
	for j in range(n):
		for  i in range(n-1):
			if V[i]>V[i+1]:
				aux = V[i]
				V[i] = V[i+1]
				V[i+1]=aux
	return V


#______ function main _______
n = leer()

vector = llenarVector(n)
print("_____Mostrar Vector Original_____")
mostrar(vector,n)

print("METODO DE BURBUJA: ")
burbuja(vector,n)
mostrar(vector,n)
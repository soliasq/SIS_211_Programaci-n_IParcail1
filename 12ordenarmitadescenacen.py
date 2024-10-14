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
def burbuja(V,n,n1):
	for j in range(n//2):
		for  i in range(n//2-1):
			if V[i]>V[i+1]:
				aux = V[i]
				V[i] = V[i+1]
				V[i+1]=aux
	for y in range(n1,n):
		for  k in range(n1,n-1):
			if V[k]<V[k+1]:
				aux = V[k]
				V[k] = V[k+1]
				V[k+1]=aux
	return V
#______ function main _______
n = leer()
print("___________________________________")
vector = llenarVector(n)
print("_____Mostrar Vector Original_____")
mostrar(vector,n)
n1=n//2
res = burbuja(vector,n,n1)
print("Orden Asc./Desc. ")
print(res)
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
#______ function ordernarPares ASc. _______
def ordernarPares(V,n):
	for i in range(n):
		for  j in range(i+1,n):
			#print(V[j])
			if V[i]%2==0 and V[j]%2==0:
				if V[i]>V[j]:
					aux=V[i]
					V[i] = V[j]
					V[j]=aux
	return V
def ordernarPares2(V,n):
	for i in range(n):
		for  j in range(n-1):
			if V[j]%2==0 :
				for  k in range(j+1,n):
					if V[k]%2==0 :
						#print(V[k])
						if V[j]>V[k]:
							aux=V[j]
							V[j] = V[k]
							V[k]=aux
	return V
#______ function main _______
n = leer()
print("___________________________________")
vector = llenarVector(n)
print("_____Mostrar Vector Original_____")
mostrar(vector,n)
res = ordernar(vector,n)
print("Ordenar Pares Asc. ")
print(res)
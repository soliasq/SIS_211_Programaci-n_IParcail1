
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
#______ function Multiploss de 3 ordenar ASc. _______
def multploTresAsc(V,n):
	for i in range(n):
		for j in range(i+1,n):
			if V[i]%3==0  and V[j]%3==0:
				#print(V[j])
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
res = multploTresAsc(vector,n)
print("Ordenar Pares Asc. ")
print("___________________________________")
print(res)
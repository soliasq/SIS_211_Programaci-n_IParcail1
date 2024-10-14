#______ function para leer vector _______
def leer():
    tam = int(input("Tamanho Vector="))
    return tam

#______ function para generar vector _______
def llenarVector(tamanho):
	V = [0]*n
	for i in range(n):
		x=int(input(f"{[i]}="))
		V[i]=x
	return V
#______ function mostrar vector _______
def mostrar(V, n):
	print("[",end="")
	for i in range(n):
		print(V[i],end=",")
	print("]")
	
def leerDesplazar():
	print("__________cuantos numeros desplzara___________")
	d = int(input("# de Desplazamiento = "))
	return d
			

def mostrarDesplazamiento(V,n):

	d= leerDesplazar()
	  # o se pude escribir aux=V[n-1

	for j in range(d):
		ultimo=V[-1]
		for  i in range(n-1, 0,-1):
			V[i]=V[i-1]
		V[0]=ultimo	
	return V


#______ function main _______
n = leer()
print("Ingrese valores para llenar vector: ")
vector = llenarVector(n)
print("_____Mostrar Original_____")
mostrar(vector,n)
res=mostrarDesplazamiento(vector,n)
print("_____Mostrardesplazamiento_____")
print(res)
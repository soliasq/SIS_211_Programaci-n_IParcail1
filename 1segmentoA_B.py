#______ function para generar vector _______
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


def mostrar(V, n):
	print("[",end="")
	for i in range(n):
		print(V[i],end=",")
	print("]")    
def leerSegemento():
	print("__________Leer Segmento___________")
	a = int(input("índice inicial = "))
	b = int(input("índice final = "))
	return a,b
def mostrarSegmento(V):
	segmento=[]# nuevo vector llenamos  el segemento
	a,b = leerSegemento()
	if a < 0 or b>=len(V) or a>b:
		return "Rango invalido"
	for i in range(len(V)): # puedo usar for i in rage(a,b+1):
		if i >=a and i<=b:
			segmento.append(V[i])
			#print(segmento)
	return segmento		


#______ function main _______
n = leer()
print("Ingrese valores para llenar vector: ")
vector = llenarVector(n)
print("_____Mostrar Original_____")
mostrar(vector,n)
res=mostrarSegmento(vector)
print("_____MostrarSegmento_____")
print(res)
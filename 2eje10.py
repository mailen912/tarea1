imagenes=['im1','im2','im3'] 
coords={}
	
for i in imagenes:
	print('ingrese el valor de x en la coordenada de la',i)
	x=int(input())
	print('ingrese el valor de y en la coordenada de la',i)
	y=int(input())
	while x == y:
		print('Las coordenadas de x e y deben ser distintas, vuelva a intentarlo')
		print('ingrese el valor de x en la coordenada de la',i)
		x=int(input())
		print('ingrese el valor de y en la coordenada de la',i)
		y=int(input())
	tup=(x,y)
	coords[i]=tup
print(coords.items())

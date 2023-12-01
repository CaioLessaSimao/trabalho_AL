import cv2
import matplotlib.pyplot as plt
import numpy as np

def menu():
	print("Escolha uma das opcoes")
	print("1) Converter rgb para tons de cinza")
	print("2) Inverter as cores de uma imagem")
	print("3) Espelhamento vertical")
	print("4) Espelhamento horizontal")
	print("5) Redimensionamento")
	print("0) Sair")
	print()
	return int(input("Digite o numero da sua resposta: "))




def cinza(img):
	temp = channel_first(img)
	return soma_lista(temp[2], soma_lista(temp[0], temp[1]))

def negative(img):
	aux = []
	for i in img:
		aux2 = []
		for j in i:
			aux3 = []
			for k in j:
				aux3.append(255-k)
			aux2.append(aux3)
		aux.append(aux2)
	return aux

def compare(original, manipulated, title_1="Original", title_2="Manipulated"):
    plt.figure(figsize=(15, 25))
    plt.subplot(1, 2, 1)
    plt.title(title_2)
    plt.imshow(manipulated)
    plt.subplot(1, 2, 2)
    plt.title(title_1)
    plt.imshow(original)
    plt.show()
    return

def soma_lista(img1, img2):
	aux = []
	for i in range(len(img1)):
		aux2 = []
		for j in range(len(img1[0])):
			aux2.append(img1[i][j] + img2[i][j])
		aux.append(aux2)
	return aux

def channel_first(img):
	aux = []
	for i in range(len(img[0][0])):
		aux2 = []
		for j in range(len(img)):
			aux3 = []
			for k in range(len(img[0])):
				aux3.append(img[j][k][i])
			aux2.append(aux3)
		aux.append(aux2)
	return aux
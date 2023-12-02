import cv2
import matplotlib.pyplot as plt
import numpy as np

def menu():
	print(" # MANIPULANDO IMAGENS #\nOperações disponíveis:")
	print("( 1 ) Converter RGB para tons de cinza.")
	print("( 2 ) Inverter as cores de uma imagem.")
	print("( 3 ) Espelhamento vertical.")
	print("( 4 ) Espelhamento horizontal.")
	print("( 5 ) Redimensionamento.")
	print("( 0 ) Sair.")
	print()
	return int(input("Digite o número correspondente a operação desejada: "))

# Conversão para escala de cinza
def cinza(img):
	temp = channel_first(img)
	return soma_lista(temp[2], soma_lista(temp[0], temp[1]))

# Conversão para tons negativos
def negativo(img):
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

# Espelhamento Vertical da imagem
def espelho_v(img):
	aux = []
	for i in range(len(img)):
		aux.append(img[-i-1])
	return aux

# Espelhamento Horizontal da imagem
def espelho_h(img):
	aux = []
	for i in range (len(img)):
		aux2 = []
		for j in range(len(img[0])):
			aux2.append(img[i][-j-1])
		aux.append(aux2)
	return aux

# ----------------------------------------- #
def compare(original, manipulada, title_1="Original", title_2="Manipulada"):
    plt.figure(figsize=(15, 25))
    plt.subplot(1, 2, 1)
    plt.title(title_2)
    plt.imshow(manipulada)
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
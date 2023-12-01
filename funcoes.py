import cv2
import matplotlib.pyplot as plt

def add_list(img1, img2):
    return [[img1[i][j] + img2[i][j] for j in range(len(img1[0]))]
            for i in range(len(img1))]

def channel_first(img):
    return [[[img[j][k][i] for k in range(len(img[0]))]
             for j in range(len(img))] for i in range(len(img[0][0]))]

def funcao_lista(img1, img2):
	aux = []
	for i in range(len(img1)):
		aux2 = []
		for j in range(len(img1[0])):
			aux2.append(img1[i][j] + img2[i][j])
		aux.append(aux2)
	return aux

def funcao_canal(img):
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



def negative():


def cinza():
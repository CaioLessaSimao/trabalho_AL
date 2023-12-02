'''Vocês precisam instalar o opencv e o matplotlib na maquina de vocês '''
import cv2 
import matplotlib.pyplot as plt
from funcoes import *

def main():
	imagem = cv2.imread("lenna.jpg")
	img = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
	img = img.tolist()

	m = menu()
	while(m != 0):
		if m == 1:
			plt.imshow(cinza(img), cmap="gray")
			plt.show()
		elif m == 2:
			compare(img, negativo(img))
		elif m == 3:
			compare(img, espelho_v(img))
		elif m == 4:
			compare(img, espelho_h(img))
		elif m==5:
			compare(img,redimensionar(img))
		m = menu()

	return

if __name__ == "__main__":
	main()
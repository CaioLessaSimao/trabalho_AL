import cv2 
import matplotlib.pyplot as plt
from funcoes import *

def main():
	imagem = cv2.imread("original.jpg")
	img = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
	img = img.tolist()

	m = menu()
	while(m != 0):
		if m == 1:
			comparacao(img, espelho_v(img))
		elif m == 2:
			comparacao(img, espelho_h(img))
		elif m == 3:
			comparacao(img,redimensionar(img))
		elif m == 4:
			comparacaoCinza(img, cinza(img))
		elif m==5:
			comparacao(img, negativo(img))
		m = menu()
	return


if __name__ == "__main__":
	main()
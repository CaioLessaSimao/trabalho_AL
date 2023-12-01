'''Vocês precisam instalar o opencv e o matplotlib na maquina de vocês '''
import cv2 
import matplotlib.pyplot as plt

def main():
	image = cv2.imread("lulu.jpg")
	img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	img = img.tolist()

	plt.imshow(img)
	plt.show()

	print("Jorge")
	return

if __name__ == "__main__":
	main()
import numpy as np
import matplotlib.pyplot as plt
import cv2



img1 = cv2.imread('../images/brain2.jpg')
img2 = cv2.imread('../images/fogo.jpg')
img3 = cv2.imread('../images/mao1.jpg')

imgs = [img1, img2, img3]
bright_imgs = []

for img in imgs:
    # se a imagem for colorida, vamos converter para cinza
    if len(img.shape) == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img.copy()
    bright = np.clip(gray + 50, 0, 255).astype(np.uint8)
    bright_imgs.append(bright)

# plotando as imagens originais e as imagens com brilho aumentado
# criando uma figura com 12 linhas (2 para cada imagem) e 6 colunas (2 para cada imagem)
plt.figure(figsize=(12, 6))
for i in range(len(imgs)):
    # 2 é o numero de linhas, len(imgs) é o numero de colunas, i + 1 é a posicao da imagem
    plt.subplot(2, len(imgs), i + 1)
    plt.imshow(cv2.cvtColor(imgs[i], cv2.COLOR_BGR2RGB))
    plt.title('Original')
    plt.axis('off')

    plt.subplot(2, len(imgs), i + 1 + len(imgs))
    plt.imshow(bright_imgs[i], cmap='gray')
    plt.title('Brilho Aumentado')
    plt.axis('off')
plt.tight_layout()
plt.show()
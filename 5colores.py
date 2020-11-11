import cv2
import numpy as np
 
img = cv2.imread("ruleta.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


#VERDE
verde_bajo = np.array([50,100,100])
verde_alto = np.array([80,255, 255])

#MORADO
morado_bajo = np.array([140,255,100])
morado_alto = np.array([170,255, 255])

#AZUL
azul_bajo = np.array([100,50,50])
azul_alto = np.array([130,255, 255])

#AMARILLO
amarillo_bajo = np.array([20,50,50])
amarillo_alto = np.array([40, 255, 255])

#ROJO
redBajo1 = np.array([0, 100, 20])
redAlto1 = np.array([8, 255, 255])
redBajo2=np.array([175, 100, 20])
redAlto2=np.array([179, 255, 255])
maskRed1 = cv2.inRange(hsv, redBajo1, redAlto1)
maskRed2 = cv2.inRange(hsv, redBajo2, redAlto2)



mask_verde = cv2.inRange(hsv, verde_bajo, verde_alto)
mask_morado= cv2.inRange(hsv, morado_bajo,morado_alto)

mask_azul = cv2.inRange(hsv, azul_bajo, azul_alto)
mask_amarillo = cv2.inRange(hsv, amarillo_bajo, amarillo_alto)

mask_unionRojo = cv2.bitwise_or(maskRed1, maskRed2)

mask_unionMV = cv2.bitwise_or(mask_morado, mask_verde)
mask_unionAA = cv2.bitwise_or(mask_amarillo, mask_azul)
mask_unionMVAA = cv2.bitwise_or(mask_unionAA, mask_unionMV)
mask_union= cv2.bitwise_or(mask_unionMVAA,mask_unionRojo )
cv2.imshow("Original", img)
cv2.imshow("copia detectando colores", mask_union)
print("pulsa pa salir \n")
cv2.waitKey(0)
cv2.destroyAllWindows()

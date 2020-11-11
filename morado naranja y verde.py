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

##NARANJA
naranja_bajo = np.array([12,255,200])
naranja_alto = np.array([23,255, 255])



mask_verde = cv2.inRange(hsv, verde_bajo, verde_alto)
mask_naranja = cv2.inRange(hsv, naranja_bajo, naranja_alto)
mask_morado= cv2.inRange(hsv, morado_bajo,morado_alto)
mask_union1 = cv2.bitwise_or(mask_naranja, mask_verde)
mask_union= cv2.bitwise_or(mask_union1, mask_morado)
cv2.imshow("Original", img)
cv2.imshow("copia detectando colores", mask_union)
print("pulsa pa salir \n")
cv2.waitKey(0)
cv2.destroyAllWindows()

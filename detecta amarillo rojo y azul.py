#Algoritmo de deteccion de colores
#Profesor:jesus homero carmona mendoza
#Alumno:Bryan Cuellar Moran
#
#Detecta objetos de colores rojo,azul y amarillo , elimina el ruido y busca su centro
 
import cv2
import numpy as np
 
#Iniciamos la camara
captura = cv2.VideoCapture(0)
 
while(1):
     
    #Capturamos una imagen y la convertimos de RGB -> HSV
    _, imagen = captura.read()
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
 
    #Establecemos el rango de colores que vamos a detectar
    #En este caso de verde oscuro a verde-azulado claro

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

     
    #Crear una mascara con solo los pixeles dentro del rango de los colores
    maskRed1 = cv2.inRange(hsv, redBajo1, redAlto1)
    maskRed2 = cv2.inRange(hsv, redBajo2, redAlto2)
    mask_azul = cv2.inRange(hsv, azul_bajo, azul_alto)
    mask_amarillo = cv2.inRange(hsv, amarillo_bajo, amarillo_alto)
    mask_unionRojo = cv2.bitwise_or(maskRed1, maskRed2)
    mask_unionAA = cv2.bitwise_or(mask_amarillo, mask_azul)
    mask_unionRAA = cv2.bitwise_or(mask_unionRojo, mask_unionAA)


    #Encontrar el area de los objetos que detecta la camara
    moments = cv2.moments(mask_unionRAA)
    area = moments['m00']
 
    #Descomentar para ver el area por pantalla
    #print area
    if(area > 2000000):
         
        #Buscamos el centro x, y del objeto
        x = int(moments['m10']/moments['m00'])
        y = int(moments['m01']/moments['m00'])
         
        #Mostramos sus coordenadas por pantalla
        print ("x = ", x)
        print ("y = ", y)
 
        #Dibujamos una marca en el centro del objeto
        cv2.rectangle(imagen, (x, y), (x+2, y+2),(0,0,255), 2)
     
     
    #Mostramos la imagen original con la marca del centro y
    #la mascara
    cv2.imshow('mask', mask_unionRAA)
    cv2.imshow('Camara', imagen)
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
 
cv2.destroyAllWindows()

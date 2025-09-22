import cv2
import numpy

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("No se puede abrir la cámara")
    exit()
while True:
    ret, frame = cap.read()
    frame_invertido = cv2.flip(frame,1) #Modo espejo
    if not ret:
        print("No se ve nada, dejandando de funcionar")
        exit()
    #colorido = cv2.cvtColor(frame,cv2.COLOR_BAYER_BG2BGR) Si quiero una imagen a color no hace falta convertirla
    #escala_grises_invertido = cv2.cvtColor(frame_invertido,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",frame_invertido) #Nombre de la pestaña que se abre y el video que muestra
    #cv2.imshow("escala de grises",escala_grises_invertido)
    media = numpy.mean(frame_invertido)  #Mira la media de brillo del frame
    print(media)
#    if media < 2: #Si se tapa la camara deja de funcionar
#        break
    if cv2.waitKey(1) == ord("q"): #Si pulso la q deja de funcionar, no funciona con la mayuscula
        break
cap.release()
cv2.destroyAllWindows()
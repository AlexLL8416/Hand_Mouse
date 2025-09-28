import cv2
import numpy
import mediapipe
import detectar_gestos
import mover_raton
import calibracion
import time
import posiciones

mp_hands = mediapipe.solutions.hands
mp_drawing= mediapipe.solutions.drawing_utils

cap = cv2.VideoCapture(0)

umbrales = None

tiempo_inicio = time.time()
tiempo_colocarse_en_posicion = 5
tiempo_calibracion_mano_cerrada = 10
tiempo_cambio_posicion = 13
tiempo_calibracion_mano_abierta = 18

pulgar_estado_anterior = "abierto"  #al inicio
cerrar = False

with mp_hands.Hands(
               max_num_hands=1,
               min_detection_confidence=0.7,
               min_tracking_confidence=0.7) as hands:
    
    #Inicio captura
    while True:

        ret, frame = cap.read()
        frame_invertido = cv2.flip(frame,1) #Modo espejo

        if not ret:
            print("No se ve nada, dejandando de funcionar")
            break

        #Paso de BGR a RGB:
        frame_invertido_rgb = cv2.cvtColor(frame_invertido,cv2.COLOR_BGR2RGB)
        height, width,  _ = frame.shape

        #Proceso las manos que se observe:
        res = hands.process(frame_invertido_rgb)

        #Operar con cada mano
        if res.multi_hand_landmarks:
            for hand_landmarks in res.multi_hand_landmarks:
                lista_posiciones = posiciones.getPosiciones(hand_landmarks,mp_hands,width,height)

                mp_drawing.draw_landmarks(frame_invertido, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                cv2.circle(frame_invertido, lista_posiciones[2],3,(168,88,237),3)

                tiempo = time.time() - tiempo_inicio
                #Calibracion
                if tiempo < tiempo_colocarse_en_posicion:
                    cv2.putText(frame_invertido, "COLOCATE EN POSICION", (50,50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
                    cv2.putText(frame_invertido, "CIERRE LA MANO", (50,100),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)

                elif tiempo_colocarse_en_posicion <= tiempo < tiempo_calibracion_mano_cerrada:
                    cv2.putText(frame_invertido, "CALIBRANDO MANO CERRADA", (50, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
                    calibracion.procesar_calibracion(lista_posiciones, "cerrado")

                elif tiempo_calibracion_mano_cerrada <= tiempo < tiempo_cambio_posicion:
                    cv2.putText(frame_invertido, "PASANDO A MANO ABIERTA", (50, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

                elif tiempo_cambio_posicion <= tiempo < tiempo_calibracion_mano_abierta:
                    cv2.putText(frame_invertido, "CALIBRANDO MANO ABIERA", (50, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
                    calibracion.procesar_calibracion(lista_posiciones, "abierto")

                elif umbrales is None:
                    umbrales = calibracion.finalizar_calibracion()
                #Fin calibración

                else:
                    #Mover ratón
                    mover_raton.moveRaton(lista_posiciones[2][0],lista_posiciones[2][1],width,height)

                    #Comprobar estado actual del pulgar
                    if detectar_gestos.dedoCerrado(lista_posiciones, umbrales, "pulgar"):
                        pulgar_estado_actual = "cerrado"
                    else:
                        pulgar_estado_actual = "abierto"

                    #Transición abierto -> cerrado
                    if pulgar_estado_anterior == "abierto" and pulgar_estado_actual == "cerrado":
                        mover_raton.clickRaton()  

                    pulgar_estado_anterior = pulgar_estado_actual

                    #Detecto cuando estoy haciendo la peineta
                    if detectar_gestos.peineta(lista_posiciones,umbrales):
                        print("Peineta")
                        cerrar = True
        
        cv2.imshow("Detección de manos",frame_invertido) #Nombre de la pestaña que se abre y el video que muestra
        if cerrar:
            break

        if cv2.waitKey(1) == ord("q"): #Si pulso la q deja de funcionar, no funciona con la mayuscula
            break

cap.release()
cv2.destroyAllWindows()
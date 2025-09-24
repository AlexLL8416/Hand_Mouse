import cv2
import numpy
import mediapipe
import math
import detectar_gestos
import mover_raton
import calibracion
import time

mp_hands = mediapipe.solutions.hands
mp_drawing= mediapipe.solutions.drawing_utils

cap = cv2.VideoCapture(0)

umbrales = None
tiempo_inicio = time.time()
pulgar_estado_anterior = "abierto"  # al inicio

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
            exit()
        #Paso de BGR a RGB:
        frame_invertido_rgb = cv2.cvtColor(frame_invertido,cv2.COLOR_BGR2RGB)
        height, width,  _ = frame.shape
        #Proceso la mano que se observe:
        res = hands.process(frame_invertido_rgb)
        #Dibuja las manos:
        if res.multi_hand_landmarks:
            #print(res.multi_hand_landmarks)
            for hand_landmarks in res.multi_hand_landmarks:
                posiciones = []
                #Pulgar
                x4=int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x*width)
                y4=int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y*height)
                posiciones.append((x4,y4))
                x1=int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x*width)
                y1=int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y*height)
                posiciones.append((x1,y1))
                #Indice
                x8=int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x*width)
                y8=int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y*height)
                posiciones.append((x8,y8))
                x5=int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x*width)
                y5=int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y*height)
                posiciones.append((x5,y5))
                #Corazón
                x12=int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x*width)
                y12=int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y*height)
                posiciones.append((x12,y12))
                x9=int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x*width)
                y9=int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y*height)
                posiciones.append((x9,y9))
                #Anular
                x16=int(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x*width)
                y16=int(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y*height)
                posiciones.append((x16,y16))
                x13=int(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].x*width)
                y13=int(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y*height)
                posiciones.append((x13,y13))
                #Meñique
                x20=int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x*width)
                y20=int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y*height)
                posiciones.append((x20,y20))
                x17=int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].x*width)
                y17=int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y*height)
                posiciones.append((x17,y17))
                #print(detectar_gestos.manoCerrada(posiciones))
                #print(detectar_gestos.manoCerrada(posiciones))
                mp_drawing.draw_landmarks(frame_invertido, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                cv2.circle(frame_invertido, (x8,y8),3,(168,88,237),3)
                cv2.circle(frame_invertido, (x5,y5),3,(0,255,0),3)
                tiempo = time.time() - tiempo_inicio
                #Calibracion
                if tiempo < 5:
                    cv2.putText(frame_invertido, "COLOCATE EN POSICION", (50,50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)

                elif 5 <= tiempo < 13:  # 5s texto + 5s recoger
                    cv2.putText(frame_invertido, "CALIBRANDO MANO ABIERTA", (50, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
                    calibracion.procesar_calibracion(posiciones, "abierto")

                elif 13 <= tiempo < 21:
                    cv2.putText(frame_invertido, "CALIBRANDO MANO CERRADA", (50, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
                    calibracion.procesar_calibracion(posiciones, "cerrado")

                elif umbrales is None:
                    umbrales = calibracion.finalizar_calibracion()
                else:
                    mover_raton.moveRaton(x8,y8,width,height)
                    print(x8,",",y8)
                    # comprobar estado actual del pulgar
                    if detectar_gestos.dedoCerrado(posiciones, umbrales, "pulgar"):
                        pulgar_estado_actual = "cerrado"
                    else:
                        pulgar_estado_actual = "abierto"

                    # transición abierto -> cerrado
                    if pulgar_estado_anterior == "abierto" and pulgar_estado_actual == "cerrado":
                        mover_raton.clickRaton()   # nueva función que hace click

                    pulgar_estado_anterior = pulgar_estado_actual
        
        cv2.imshow("Detección de manos",frame_invertido) #Nombre de la pestaña que se abre y el video que muestra
        if cv2.waitKey(1) == ord("q"): #Si pulso la q deja de funcionar, no funciona con la mayuscula
            break
cap.release()
cv2.destroyAllWindows()
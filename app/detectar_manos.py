import cv2
import numpy
import mediapipe
import math

mp_hands = mediapipe.solutions.hands
mp_drawing= mediapipe.solutions.drawing_utils

cap = cv2.VideoCapture(0)

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
                print("Empieza mano")
                print(math.dist((x4,y4),(x1,y1)))
                #Indice
                x8=int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x*width)
                y8=int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y*height)
                posiciones.append((x8,y8))
                x5=int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x*width)
                y5=int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y*height)
                posiciones.append((x5,y5))
                print(math.dist((x8,y8),(x5,y5)))
                #Corazón
                x12=int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x*width)
                y12=int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y*height)
                posiciones.append((x12,y12))
                x9=int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x*width)
                y9=int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y*height)
                posiciones.append((x9,y9))
                print(math.dist((x12,y12),(x9,y9)))
                #Anular
                x16=int(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x*width)
                y16=int(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y*height)
                posiciones.append((x16,y16))
                x13=int(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].x*width)
                y13=int(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y*height)
                posiciones.append((x13,y13))
                print(math.dist((x16,y16),(x13,y13)))
                #Meñique
                x20=int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x*width)
                y20=int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y*height)
                posiciones.append((x20,y20))
                x17=int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].x*width)
                y17=int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y*height)
                posiciones.append((x17,y17))
                print(math.dist((x20,y20),(x17,y17)))
                print("Fin mano")
                #print(posiciones)
                #indice = math.dist((x8,y8),(x5,y5))
                #print(indice)
                #if indice <= 24:
                #    print("índice cerrado")
                mp_drawing.draw_landmarks(frame_invertido, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                cv2.circle(frame_invertido, (x8,y8),3,(255,0,0),3)
                cv2.circle(frame_invertido, (x5,y5),3,(0,255,0),3)
        
        cv2.imshow("Detección de manos",frame_invertido) #Nombre de la pestaña que se abre y el video que muestra
        if cv2.waitKey(1) == ord("q"): #Si pulso la q deja de funcionar, no funciona con la mayuscula
            break
cap.release()
cv2.destroyAllWindows()
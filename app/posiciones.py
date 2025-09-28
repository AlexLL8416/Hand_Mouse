import mediapipe


def getPosiciones (hand_landmarks,mp_hands,width,height):
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
    return posiciones
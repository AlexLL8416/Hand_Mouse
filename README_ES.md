# 🖐️ Hand Mouse – Control del ratón con gestos de la mano

Este proyecto permite controlar el ratón del ordenador utilizando la **cámara web** y **gestos de la mano** detectados con [MediaPipe](https://developers.google.com/mediapipe) y [OpenCV](https://opencv.org/).  
Tras un breve proceso de calibración, podrás mover el cursor y realizar clics con la mano.

## 🚀 Funcionalidades principales

- Mover el cursor siguiendo la posición del dedo índice.  
- Hacer clic cerrando el pulgar.  
- Detectar gestos especiales como la peineta (cierra el programa).  
- Calibración automática de la mano abierta y cerrada para adaptarse a cada usuario.  

## 📦 Requisitos
pip install opencv-python mediapipe pyautogui numpy

## ▶️ Uso
1. Conecta una cámara web y ejecuta el programa principal:

   python main.py

2. Durante los primeros segundos se realiza la calibración:
   - Sitúa la mano en la posición indicada.
   - Cierra la mano cuando se te pida.
   - Ábrela cuando se te pida.

3. Una vez calibrado:
   - Mueve el dedo índice para controlar el cursor.
   - Cierra el pulgar para hacer clic.
   - Haz la peineta para cerrar el programa.
   - También puedes salir pulsando la tecla q.

## 📂 Estructura del proyecto
```
.
├── main.py             # Programa principal: gestiona cámara, calibración y control
├── calibracion.py      # Lógica para calcular umbrales de dedos abiertos/cerrados
├── detectar_gestos.py  # Funciones para detectar dedos abiertos/cerrados y gestos
├── mover_raton.py      # Control del cursor y clics mediante pyautogui
├── posiciones.py       # Obtención de coordenadas (TIP y MCP) de cada dedo
```
## ⚙️ Explicación del flujo
1. main.py abre la cámara y dibuja la mano en pantalla.  
2. Se realiza la calibración para calcular los umbrales entre mano abierta y cerrada.  
3. Una vez calibrado:
   - Se llama a mover_raton.moveRaton() para mover el cursor.  
   - Se detectan gestos con detectar_gestos.  
   - Si el pulgar pasa de abierto → cerrado, se ejecuta un clic (mover_raton.clickRaton()).  
   - Si se detecta la peineta, el programa se cierra.  

## 🔮 Posibles mejoras
- Añadir doble clic o clic derecho con nuevos gestos.  
- Ajustar dinámicamente la sensibilidad del cursor.  
- Soporte para más de una mano.  
- Configuración de gestos personalizados.  

## 👨‍💻 Autor
Proyecto desarrollado por Alejandro Lara Lara, utilizando Python, OpenCV y MediaPipe.

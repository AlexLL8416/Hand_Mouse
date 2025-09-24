import numpy as np

# Cada dedo representado como índice de TIP y MCP en la lista posiciones
dedos = {
    "pulgar": (0, 1),
    "indice": (2, 3),
    "corazon": (4, 5),
    "anular": (6, 7),
    "menique": (8, 9),
}

abierto = {d: [] for d in dedos}
cerrado = {d: [] for d in dedos}
umbrales = {}
calibracion_completa = False


def procesar_calibracion(posiciones, fase):
    """
    Guarda las distancias TIP–MCP de cada dedo según la fase.
    fase: "abierto" o "cerrado"
    """
    global abierto, cerrado

    if posiciones is None or len(posiciones) < 10:
        return

    for nombre, (tip, mcp) in dedos.items():
        (xt, yt) = posiciones[tip]
        (xb, yb) = posiciones[mcp]
        dist = np.linalg.norm(np.array([xt, yt]) - np.array([xb, yb]))

        if fase == "abierto":
            abierto[nombre].append(dist)
        elif fase == "cerrado":
            cerrado[nombre].append(dist)


def finalizar_calibracion():
    """
    Calcula umbrales promedio entre mano abierta y cerrada.
    Devuelve diccionario con umbrales por dedo.
    """
    global abierto, cerrado, umbrales, calibracion_completa
    umbrales = {}

    for d in dedos.keys():
        if abierto[d] and cerrado[d]:
            media_abierto = np.mean(abierto[d])
            media_cerrado = np.mean(cerrado[d])
            umbrales[d] = (media_abierto + media_cerrado) / 2

    calibracion_completa = True
    return umbrales

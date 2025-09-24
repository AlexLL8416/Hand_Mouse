# Parseo los landsmarks de los dedos a listas del tipo [int,int]
#
# Ej. [418,322] y [547,361]
#
# Simplemente calculo su distancia euclidea con el módulo math
import math

def analizarDistancias(lista_posicones):
    res = []
    for i in range(0,len(lista_posicones),2):
        res.append(math.dist(lista_posicones[i],lista_posicones[i+1]))
    ref = math.dist(lista_posicones[3], lista_posicones[9]) # índice_mcp y meñique_mcp
    return [d/ref for d in res]

# Umbrales para considerar cada dedo "cerrado"
UMBRAL_DEDOS = {
    #"pulgar": 0.7,
    "indice": 0.16,
    "corazon": 0.23,
    "anular": 0.23,
    "menique": 0.21,
}

def dedoCerrado(lista_posiciones, dedo):
    """Devuelve True si el dedo indicado está cerrado."""
    distancias = analizarDistancias(lista_posiciones)
    #print(distancias)
    # usamos el orden de UMBRAL_DEDOS.keys() para asignar índices
    dedos = list(UMBRAL_DEDOS.keys())
    idx = dedos.index(dedo)
    return distancias[idx] <= UMBRAL_DEDOS[dedo] #True si dedo está cerrado

def manoAbierta(lista_posiciones):
    """Devuelve True si todos los dedos están abiertos."""
    return all(
        not dedoCerrado(lista_posiciones, dedo)
        for dedo in UMBRAL_DEDOS
    )

def manoCerrada(lista_posiciones):
    """Devuelve True si todos los dedos están cerrados."""
    return all(
        dedoCerrado(lista_posiciones, dedo)
        for dedo in UMBRAL_DEDOS
    )
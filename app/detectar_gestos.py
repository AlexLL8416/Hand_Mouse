import math

def analizarDistancias(lista_posicones):
    res = []
    for i in range(0,len(lista_posicones),2):
        res.append(math.dist(lista_posicones[i],lista_posicones[i+1]))
    ref = math.dist(lista_posicones[3], lista_posicones[9]) # índice_mcp y meñique_mcp
    return [d/ref for d in res]

'''
# Umbrales para considerar cada dedo "cerrado"
UMBRAL_DEDOS = {
    #"pulgar": 0.7,
    "indice": 0.16,
    "corazon": 0.23,
    "anular": 0.23,
    "menique": 0.21,
}
'''

def dedoCerrado(lista_posiciones, umbrales, dedo):
    """Devuelve True si el dedo indicado está cerrado."""
    distancias = analizarDistancias(lista_posiciones)
    #print(distancias)
    # usamos el orden de UMBRAL_DEDOS.keys() para asignar índices
    dedos = list(umbrales.keys())
    idx = dedos.index(dedo)
    ref = math.dist(lista_posiciones[3], lista_posiciones[9])
    return distancias[idx] <= (umbrales[dedo]/ref) #True si dedo está cerrado

def manoAbierta(lista_posiciones,umbrales):
    """Devuelve True si todos los dedos están abiertos."""
    return all(
        not dedoCerrado(lista_posiciones, umbrales, dedo)
        for dedo in umbrales
    )

def manoCerrada(lista_posiciones,umbrales):
    """Devuelve True si todos los dedos están cerrados."""
    return all(
        dedoCerrado(lista_posiciones, umbrales, dedo)
        for dedo in umbrales
    )
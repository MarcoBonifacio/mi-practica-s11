# Constantes de descuento por tipo de cliente
DESCUENTO_VIP = 0.20
DESCUENTO_ESTUDIANTE = 0.15
DESCUENTO_MAYORISTA = 0.30

# Constantes de descuento por distancia
UMBRAL_DISTANCIA_ALTA = 100
DESCUENTO_DISTANCIA_ALTA = 5
UMBRAL_DISTANCIA_MEDIA = 50
DESCUENTO_DISTANCIA_MEDIA = 2

def calcular_subtotal(lista_productos):
    subtotal = 0
    for precio, cantidad in lista_productos:
        subtotal += precio * cantidad
    return subtotal

def aplicar_descuento_cliente(monto, tipo_cliente):
    if tipo_cliente == "vip":
        return monto * (1 - DESCUENTO_VIP)
    elif tipo_cliente == "est":
        return monto * (1 - DESCUENTO_ESTUDIANTE)
    elif tipo_cliente == "may":
        return monto * (1 - DESCUENTO_MAYORISTA)
    return monto

def aplicar_descuento_distancia(monto, distancia_km):
    if distancia_km > UMBRAL_DISTANCIA_ALTA:
        return monto - DESCUENTO_DISTANCIA_ALTA
    elif distancia_km > UMBRAL_DISTANCIA_MEDIA:
        return monto - DESCUENTO_DISTANCIA_MEDIA
    return monto

def procesar_pedido(lista_productos, tipo_cliente, distancia_km):
    total = calcular_subtotal(lista_productos)
    total = aplicar_descuento_cliente(total, tipo_cliente)
    total = aplicar_descuento_distancia(total, distancia_km)
    return max(0, total)
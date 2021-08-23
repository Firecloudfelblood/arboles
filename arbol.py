def ArbolBinario(r):
    return [r, [], []]


def insertar_izq(raiz, rama):
    t = raiz.pop(1)
    if len(t) > 1:
        raiz.insert(1, [rama, t, []])
    else:
        raiz.insert(1, [rama, [], []])
    return raiz


def insertar_der(raiz, rama):
    t = raiz.pop(2)
    if len(t) > 1:
        raiz.insert(2, [rama, [], t])
    else:
        raiz.insert(2, [rama, [], []])


deku = ArbolBinario(0)
insertar_izq(raiz=deku, rama=1)
insertar_izq(raiz=deku, rama=2)
# insertar_izq(raiz=deku, rama=3)
# insertar_izq(raiz=deku, rama=4)

insertar_der(raiz=deku, rama=7)
# insertar_der(raiz=deku, rama=8)
# insertar_der(raiz=deku, rama=9)
# insertar_der(raiz=deku, rama=10)

print(deku)

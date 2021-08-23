class TreeNode(object):
    def __init__(self, x):
        # Valor a guardar
        self.valor = x
        # Nodo izquierdo
        self.izq = None
        # Nodo derecho
        self.der = None


def validar_bst(arbol):
    max = 10
    min = -10
    # TODO: acaba la funcion
    if arbol is None:
        return True
    if arbol.valor < min or arbol.valor > max:
        return False

    return (validar_bst(arbol.izq) and
            validar_bst(arbol.der))


import unittest


class PruebaBST(unittest.TestCase):

    def prueba(self, fun_solucion):
        # Arbol 1
        deku_1 = TreeNode(0)
        deku_1.izq = TreeNode(-1)
        deku_1.der = TreeNode(1)

        # Arbol 2
        deku_2 = TreeNode(0)
        deku_2.izq = TreeNode(-1)
        deku_2.der = TreeNode(-2)

        # Arbol 3
        deku_3 = TreeNode(0)
        deku_3.izq = TreeNode(-1)
        deku_3.der = TreeNode(1)
        deku_3.der.der = TreeNode(2)

        # Arbol 4
        deku_4 = TreeNode(0)
        deku_4.izq = TreeNode(-1)
        deku_4.der = TreeNode(1)
        deku_4.izq.izq = TreeNode(2)

        dict_pruebas = {
            1: (deku_1, True),
            2: (deku_2, False),
            3: (deku_3, True),
            4: (deku_4, False),
        }
        sol = 'Error, tu funcion no regresa nada'
        casos_errados = []
        for p in dict_pruebas.values():
            try:
                sol = fun_solucion(arbol=p[0])
                self.assertEqual(sol, p[1])
                print('PASO')
            except AssertionError as e:
                print(f'Fallo! arbol={p[0]},  output={sol}, esperada={p[1]}')
                casos_errados.append(p)
        return casos_errados


t = PruebaBST()
t.prueba(validar_bst)

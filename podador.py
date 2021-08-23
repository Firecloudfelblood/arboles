class TreeNode(object):
    def __init__(self, x):
        # Valor a guardar
        self.valor = x
        # Nodo izquierdo
        self.izq = None
        # Nodo derecho
        self.der = None


def podar_bst(nodo: TreeNode, min, max) -> TreeNode:
    def auxiliar(bst):
        if not bst:
            return None

        bst.left = auxiliar(bst.izq, min, max)
        bst.right = auxiliar(bst.der, min, max)

        if bst.valor < min:
            return bst.der
        elif bst.valor > max:
            return bst.izq
        else:
            return bst

        return inorder(nodo)

    def inorder(vals):
        if vals.izq is not None:
            vals.izq.inorder(vals)
        if vals.raiz is not None:
            vals.append(vals.valor)
        if vals.der is not None:
            vals.der.inorder(vals)
        return inorder(vals)

    def inorder(vals):
        if vals.izq is not None:
            vals.izq.inorder(vals)
        if vals.value is not None:
            vals.append(vals.valor)
        if vals.der is not None:
            vals.der.inorder(vals)
        return vals

deku = TreeNode(0)
deku.izq = TreeNode(-1)
deku.der = TreeNode(1)
deku.der.der = TreeNode(2)

sol = podar_bst(deku, 0, 2)
print(deku.valor)

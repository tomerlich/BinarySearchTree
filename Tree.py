from Node import Node


def insert(node, key, height):
    if node is None:
        return Node(key, height + 1)
    if key < node.key:
        node.left = insert(node.left, key, height + 2)
    else:
        node.right = insert(node.right, key, height + 2)
    return node


def calcBF(root):
    if root.left is not None and root.right is not None:
        root.balanceFactor = root.left.height - root.right.height


def findPreSuc(root, key):
    if root is None:
        return

    if root.key == key:

        if root.left is not None:
            tmp = root.left
            while tmp.right:
                tmp = tmp.right
            findPreSuc.pre = tmp

        if root.right is not None:
            tmp = root.right
            while tmp.left:
                tmp = tmp.left
            findPreSuc.suc = tmp

    if root.key > key:
        findPreSuc.suc = root
        findPreSuc(root.left, key)

    if root.key < key:
        findPreSuc.pre = root
        findPreSuc(root.right, key)


def printTree(root):
    out = ""
    i = 0

    if root is not None:
        while i < root.height:
            if i == 0:
                out += "|"
            else:
                out += "-"
            i += 1

        out += str(root.key)
        print(out)
        printTree(root.left)
        printTree(root.right)


if __name__ == "__main__":
    root = None
    root = insert(root, 50, -1)
    insert(root, 30, -1)
    insert(root, 20, -1)
    insert(root, 40, -1)
    insert(root, 70, -1)
    insert(root, 60, -1)
    insert(root, 80, -1)
    insert(root, 65, -1)
    insert(root, 63, -1)
    insert(root, 50, -1)
    insert(root, 70, -1)

    printTree(root)
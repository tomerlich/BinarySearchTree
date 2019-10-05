from Node import Node


def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node


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
    pass

if __name__ == "__main__":
    key = 40
    root = None
    root = insert(root, 50)
    insert(root, 30);
    insert(root, 20);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    insert(root, 80);
    findPreSuc.pre = None
    findPreSuc.suc = None

    printTree(root)

    findPreSuc(root, key)

    if findPreSuc.pre is not None:
        print("Predecessor is", findPreSuc.pre.key)

    else:
        print("No Predecessor")

    if findPreSuc.suc is not None:
        print("Successor is", findPreSuc.suc.key)
    else:
        print("No Successor")

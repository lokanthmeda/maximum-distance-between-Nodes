class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def fun(root, d={}, path=""):
    if root:
        d[root.data] = path
        fun(root.left, d, path+"0")
        fun(root.right, d, path+"1")
    return d

root = Node(5)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.left.left = Node(9)
root.right.right = Node(1)
root.right.right.right = Node(6)
root.right.right.left = Node(4)


d = fun(root)

val1, val2 = map(int, input("Enter two nodes separated with space: ").split())


node1 = d.get(val1, None)
node2 = d.get(val2, None)


if node1 is None or node2 is None:
    print("At least one value is invalid or not found")
    exit()


if len(node1) != len(node2):
    print("Nodes are not on the same level")
    exit()


dist = abs(int(node1, 2) - int(node2, 2))
print(dist)

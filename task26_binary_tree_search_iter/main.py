class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def generator(head):
    if head.left is not None:
        yield from generator(head.left)
    yield head
    if head.right is not None:
        yield from generator(head.right)


root = Node(3)

root.left = Node(2)
root.right = Node(4)

for node in generator(root):
    print(node.value)


class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



#
# v1 = Node(1)
# v2 = Node(2, v1)
# v5 = Node(5)
# v4 = Node(4, v2, v5)
# v9 = Node(9)
# v8 = Node(8, right=v9)
# v7 = Node(7, v4, v8)
# head = v7
#
#
# for node in bst_generator(head):
#     print(node.value)
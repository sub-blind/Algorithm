n = int(input())

tree = {}

for _ in range(n):
    parent, left_child, right_child = input().split()
    tree[parent] = (left_child, right_child)


def preorder(node):
    if node == '.':
        return
    
    left, right = tree[node]
    
    print(node, end='')
    preorder(left)
    preorder(right)


def inorder(node):
    if node == '.':
        return
    
    left, right = tree[node]
    
    inorder(left)
    print(node, end='')
    inorder(right)


def postorder(node):
    if node == '.':
        return
    
    left, right = tree[node]
    
    postorder(left)
    postorder(right)
    print(node, end='')


root = 'A'

preorder(root)
print()

inorder(root)
print()

postorder(root)
import sys
input = sys.stdin.readline
N = int(input())
tree = {}

for _ in range(N):
    root, left, right = input().strip().split()
    tree[root] = [left, right]

preorder_result = []
def preorder(root):
    if root != ".":
        preorder_result.append(root)
        preorder(tree[root][0])
        preorder(tree[root][1])

inorder_result = []
def inorder(root):
    if root != ".":
        inorder(tree[root][0])
        inorder_result.append(root)
        inorder(tree[root][1])

postorder_result = []
def postorder(root):
    if root != ".":
        postorder(tree[root][0])
        postorder(tree[root][1])
        postorder_result.append(root)
# 전위 순회
preorder("A")
print("".join(preorder_result))

# 중위 순회
inorder("A")
print("".join(inorder_result))

# 후위 순회
postorder("A")
print("".join(postorder_result))

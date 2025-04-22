class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_valid_bst(root, min_val = float('-inf'), max_val = float('inf')):
    if not root:
        return True
    if not (min_val < root.val < max_val):
        return False
    else:
        return is_valid_bst(root.left, min_val, root.val) and is_valid_bst(root.right, root.val, max_val)
    
root = BinaryTree(10)
root.left = BinaryTree(5)
root.right = BinaryTree(15)
root.right.left = BinaryTree(12)
root.right.right = BinaryTree(20)

print(is_valid_bst(root))
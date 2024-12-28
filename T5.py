class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(preorder_list):
    if not preorder_list:
        return None
    
    value = preorder_list.pop(0)
    if value == '#':
        return None
    
    node = TreeNode(value)
    node.left = build_tree(preorder_list)
    node.right = build_tree(preorder_list)
    return node

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def find_leaves(root):
    leaves = []
    
    def dfs(node):
        if node is None:
            return
        if node.left is None and node.right is None:
            leaves.append(node.value)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return leaves

def tree_depth(root):
    if root is None:
        return 0
    left_depth = tree_depth(root.left)
    right_depth = tree_depth(root.right)
    return 1 + max(left_depth, right_depth)

def main():
    preorder_input = input().strip().split()

    root = build_tree(preorder_input)
    
    total_nodes = count_nodes(root)
    print(total_nodes)
    
    leaves = find_leaves(root)
    print(" ".join(leaves))

    depth = tree_depth(root)
    print(depth)

if __name__ == "__main__":
    main()

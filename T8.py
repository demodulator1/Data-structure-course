class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 交换左右子树的函数
def swap_left_right(root):
    if root is None:
        return None
    root.left, root.right = root.right, root.left
    swap_left_right(root.left)
    swap_left_right(root.right)
    return root

# 层序遍历输出树
def level_order_traversal(root):
    if root is None:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        result.append(str(node.val))
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

# 构建二叉树函数，处理输入字符串
def build_binary_tree(values):
    if not values:
        return None
    # 转换输入的字符串为一个列表
    values = list(values)
    if values[0] == '#':  # 如果根节点就是空节点
        return None
    
    # 创建根节点
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        current = queue.pop(0)
        
        # 处理左子节点
        if i < len(values) and values[i] != '#':
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        
        # 处理右子节点
        if i < len(values) and values[i] != '#':
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

def main():
    # 读取输入
    input_str = input().strip()
    # 构建二叉树
    root = build_binary_tree(input_str)
    # 交换左右子树
    swapped_root = swap_left_right(root)
    # 按层遍历输出结果
    result = level_order_traversal(swapped_root)
    print("".join(result))

if __name__ == "__main__":
    main()

# 중앙을 기준으로 이진 트리를 반전시켜라


def invertTree(self, root):
    if root:
        root.left, root.right = \
            self.invertTree(root.right), self.invertTree(root.left)
        return root
    return None
    
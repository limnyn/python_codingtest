


class Node(object):
    def __init__(self, item):
        self.item = item
        self.left = self.right = self.root = None

    def inorder(self):
        def _inorder(node):
            if node.left:
                _inorder(node.left)
            print(node.item,end='')
            if node.right:
                _inorder(node.right)
        _inorder(self.root)

for t_c in range(1, 11):
    n = int(input())
    

    node_list = [ Node(x) for x in range(n)]
    
    for i in range(n):
        line = list(input().split())
        num = int(line[0])-1
        node_list[i].item = line[1]
        if len(line) >= 3:
            node_list[i].root = node_list[int(line[0])-1]
            node_list[i].left = node_list[int(line[2])-1]
        if len(line) == 4:
            node_list[i].right = node_list[int(line[3])-1]
    print(f'#{t_c} ',end='')
    node_list[0].inorder()
    print()
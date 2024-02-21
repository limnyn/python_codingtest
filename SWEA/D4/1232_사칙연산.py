
opers = ['+', '-', '*', '/']

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

    def calc(self):
        def _calc(node):
            if node.item in opers:
                if node.item == '+':
                    node.item = _calc(node.left) + _calc(node.right)
                elif node.item == '-':
                    node.item = _calc(node.left) - _calc(node.right)
                elif node.item == '*':
                    node.item = _calc(node.left) * _calc(node.right)
                elif node.item == '/':
                    node.item = _calc(node.left) / _calc(node.right)
            
            return node.item

        return _calc(self)

for t_c in range(1, 11):
    n = int(input())
    

    node_list = [ Node(x) for x in range(n)]
    
    for i in range(n):
        line = list(input().split())
        num = int(line[0])-1

        if line[1].isdigit():
            node_list[num].item = int(line[1])
        else:
            root_node_idx = int(line[0])-1
            left_node_idx = int(line[2])-1
            right_node_idx = int(line[3])-1
            node_list[root_node_idx].item = line[1]

            node_list[root_node_idx].left = node_list[left_node_idx]
            node_list[root_node_idx].right = node_list[right_node_idx]
            
            node_list[left_node_idx].root = node_list[root_node_idx]
            node_list[right_node_idx].root = node_list[root_node_idx]
    print(f'#{t_c} {int(node_list[0].calc())}')
    
'''
5
1 - 2 3
2 - 4 5
3 10
4 88
5 65
'''
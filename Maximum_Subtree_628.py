import sys

def findSubtree(self, root):
    self.max_sum = -sys.maxsize
    self.result = root
    self.dfs(root)

    return self.result    

def dfs(self, node):
    left = self.dfs(node.left)
    right = self.dfs(node.right)

    current_sum = node.val + left + right

    if current_sum > self.max_sum:
        self.max_sum = current_sum
        self.result = node
    
    return current_sum
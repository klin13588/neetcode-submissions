# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        use bfs and append each level to the res

        res = []
        q = collections.deque()
        append root to q

        while q:
            grab the len of the current q this is the level we are on
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.right)
                    queue.append(node.left)
            if level:
                res.append(level)

        '''

        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            level = []
            lenQ = len(queue)

            for i in range(lenQ):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
        

            if level:
                res.append(level)
        
        return res
        


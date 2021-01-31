class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        order = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            order.append(cur.val)
            cur = cur.right
        print(order)
        
        for i in range(1, len(order)):
            if order[i] <= order[i-1]:
                return False
        return True

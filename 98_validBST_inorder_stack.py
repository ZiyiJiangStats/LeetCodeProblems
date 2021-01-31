class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # using inorder - binary search tree will be ascending order
        stack = []
        cur = root
        pre = None
        while len(stack) or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                p = stack.pop()
                if pre and p.val <= pre.val:
                    return False
                pre = p
                cur = p.right
        return True

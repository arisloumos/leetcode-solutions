class Solution(object):
    def dfs(self, node):
        if node is None:
            return 0, 0, 0

        left_sum, left_count, left_matches = self.dfs(node.left)
        right_sum, right_count, right_matches = self.dfs(node.right)

        total_sum = node.val + left_sum + right_sum
        total_count = 1 + left_count + right_count
        matches = left_matches + right_matches

        average = total_sum // total_count
        if node.val == average:
            matches += 1

        return total_sum, total_count, matches
        
    def averageOfSubtree(self, root):
        total_sum, total_count, matches = self.dfs(root)
        return matches
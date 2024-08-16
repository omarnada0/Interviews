#

# Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]

        #     3
        #    / \
        #   9   20
        #       /\
        #     15  7 

############################################

# Thinking process is to start from the root node and assign it as a level 0:
#     - Anything that will be left of the root will have a negative Value 
#     - Anything on the right of the root will have a positive value 
# BFS / DFS --> Essentially we can use either as we are storing the level for each node so it wont matter which node is visited first
# I will use BFS 

def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    # Test case, what if the tree is empty
    if not root:
        return []
    
    # Creating a queue to store the node value and the level it is in
    q = collections.deque()
    q.append((root,0))

    # Applying BFS
    levels = {}

    while q:
        node, level = q.popleft()
        if level not in levels:
            levels[level] = []
        levels[level].append(node.val)

        # Check if the node has a left child and decrement level by 1
        if node.left:
            q.append((node.left, level - 1))
        # Check if the node has a right child and increment level by 1
        if node.right:
            q.append((node.right, level + 1))
        
    return [levels[x] for x in sorted (levels.keys())]
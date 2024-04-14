# 98. Validate Binary Search Tree
My solution for this problem is just a very intuitive but slow solution; I use a recursive algorithm which checks if both left and right are valid first and if either is invalid return false with the base case being a null node. From there, in each recursive step we traverse the left and right subtree with helper functions to check if they contain a larger or smaller value than the root respectively.
This is very slow because after going through the entire tree, the algorithm then goes back up and checks from each node down again.

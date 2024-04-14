# 2. Add Two Numbers
Here I went with my first intuition which is essentially long addition. Just go through the lists at the same time, add the 2 elements and insert them as a new list node. For overflow, I have a single number which is 0 by default and set to 1 if overflow happens and is then added on the next iteration. The loop breaks when both nodes are null and there is no overflow left.

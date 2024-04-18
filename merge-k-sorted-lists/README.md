# 23. Merge k Sorted Lists
## First solution
My basic approach for this problem mirrors the merging process I learned for 2 lists for the merging in merge sort; that is, iterate over all lists and look only at the first entry since this is guaranteed to be the smallest due to the sorted property of all lists. From there remove the smallest entry from that list and add it to the result. Keep repeating this until all lists are empty and the result is a sorted list.

## Fast solution
To improve performance, we can sort the entries by their first entry, then when taking it, we only need to sort this one again and the take the first one. For this implementation, a min-heap is ideal due to fast adding and removing of single elements. 
A small nuissance with python is that the heapq methods do not work with a custom cmp function, therefore we need to extract each value from the node with value as a tuple. However, if the first element of the tuple is the same it falls trough to comparing the second one. In that case, we add a unique ID to prevent comparison between listnodes which doesn't work. Would be much easier if we could add a \_\_lt\_\_() function to ListNode it would be much easier and the tuple would not be needed. 

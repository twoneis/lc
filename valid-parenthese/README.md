# 20. Valid Parentheses
Pretty simple problem; I create a stack and for each opening parentheses I push the closing one to the stack. When we get a closing parentheses I pop from the stack and compare to the current one. If they are not equal or the stack is empty, we encountered mismatching brackets. After looping over the entire string, it is valid iff the stack is empty.
For better extendability and readablitiy, a dictionary from opening to closing parentheses could be used to combine all the opening cases at the cost of performance (dict initialization overhead and lookups).

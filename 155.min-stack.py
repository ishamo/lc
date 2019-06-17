class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.small_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.small_stack or self.small_stack[-1] >= x:
            self.small_stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.small_stack[-1] == self.stack[-1]:
            self.small_stack.pop(-1)
        self.stack.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.small_stack[-1]



# Your MinStack object will be instantiated and called as such:
# ["MinStack","push","push","push","getMin","pop","getMin"]
# [[],[0],[1],[0],[],[],[]]
# obj = MinStack()
# obj.push(0)
# obj.push(1)
# obj.push(0)
# param_1 = obj.getMin()
# obj.pop()
# param_2 = obj.getMin()

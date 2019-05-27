# coding: utf-8
# 队列一定是先进先出的. right in, left out
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue1.append(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if not self.queue1:
            self.queue1, self.queue2 = self.queue2, self.queue1

        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))

        return self.queue1.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if not self.queue1:
            self.queue1, self.queue2 = self.queue2, self.queue1

        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))

        return self.queue1[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.queue1 and not self.queue2


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# print obj.empty()
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# Input data:
# ["MyStack","push","push","top","pop","empty"]
# [[],[1],[2],[],[],[]]
#
# Actual
#   ? runtime: 20 ms
#   ? answer: [null,null,null,1,1,true]
#   ? stdout: ''
#
# Expected
#   ? runtime: 4 ms
#   ? answer: [null,null,null,2,2,false]
#   ? stdout: ''
#

class MinStack:

    def __init__(self):
        import queue
        self.stack = queue.LifoQueue()
        self.minstack = queue.LifoQueue()
        

    def push(self, val: int) -> None:
        self.stack.put(val)
        if not self.minstack.empty():
            cur_min = self.minstack.get()
            self.minstack.put(cur_min)
            if val < cur_min:
                self.minstack.put(val)
            else:
                self.minstack.put(cur_min)
        else:
            self.minstack.put(val)

    def pop(self) -> None:
        self.stack.get()
        self.minstack.get()

    def top(self) -> int:
        t = self.stack.get()
        self.stack.put(t)
        return t
        
    def getMin(self) -> int:
        m = self.minstack.get()
        self.minstack.put(m)
        return m
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
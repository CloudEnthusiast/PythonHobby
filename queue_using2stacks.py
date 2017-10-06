#!/usr/bin/python

# AUTHOR: PRAVEEN N

class myStack():
    '''Stack is implemented using list.

    Operations like pop,push,isempty,size are defined.
    '''

    def __init__(self):
        self.bucket = []

    def push(self, item):
        self.bucket.append(item)

    def pop(self):
        return self.bucket.pop()

    def size(self):
        return len(self.bucket)

    def isEmpty(self):
        return self.size() == 0

    def print_mystack(self):
        for i in range(0, len(self.bucket)):
            print (self.bucket[i],)
        print ('\n')


class myQueue():
    ''' Queue implemented using 2 stacks.

    All related operations are defined.
    '''

    def __init__(self):
        self.instack = myStack() # instack
        self.outstack = myStack() # outstack

    def enqueue(self, item):
        self.instack.push(item)

    def dequeue(self):
        for i in range(0, self.instack.size()):
            self.outstack.push(self.instack.pop())
        return self.outstack.pop()
        for i in range(0, self.outstack.size()):
            self.instack.push(self.outstack.pop())
        #if not self.instack.isEmpty():
        #    while self.instack.size() > 0:
        #        self.outstack.push(self.instack.pop())
        #    res = self.outstack.pop()
        #    while self.outstack.size() > 0:
        #        self.instack.push(self.outstack.pop())
        #    return res


    def isEmpty(self):
        return self.instack.isEmpty()


q1 = myQueue()
print ('Is Queue Empty ?',q1.isEmpty())
q1.enqueue('hi')
q1.enqueue('world')
print ('Items inserted to Queue')
print ('Is Queue Empty ?',q1.isEmpty())

a=q1.dequeue()
print (a)

b=q1.dequeue()
print (b)

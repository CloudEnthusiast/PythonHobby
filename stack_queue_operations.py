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

    #def remove_item(self, item):
    #    self.bucket.remove(item)


class myQueue():
    '''Queue is implemented using list.

    Operations like enqueue,dequeue,isempty,size are defined.
    '''

    def __init__(self):
        self.pipe = []

    def size(self):
        return len(self.pipe)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.pipe.append(item)
        #self.pipe.insert(-1, item)

    def dequeue(self):
        if self.size() == 0:
            print ("There are No elements to remove")
        else:
            return self.pipe.pop(0)

    def print_myqueue(self):
        for i in range(0, len(self.pipe)):
            print (self.pipe[i],)
        print ('\n')

# stack examples
print('\n{0:*^16}\n'.format('STACK'))
s1 = myStack()
print ('Is stack Empty ?',s1.isEmpty())
s1.push('hi')
s1.push('world')
print ('Items inserted to Stack')
print ('Is stack Empty ?',s1.isEmpty())
s1.push('oct')
s1.push(4)
s1.print_mystack()
print ('Stack size:',s1.size())
s1.pop()
print ('\nAfter pop, stack contains:')
s1.print_mystack()
print ('Stack size:',s1.size())
s1.push(2017)
s1.print_mystack()
#s1.remove_item('oct')
#s1.print_mystack()
print ('Size of stack:',s1.size())


# queue examples
print('\n{0:*^16}\n'.format('QUEUE'))
q1 = myQueue()
print ('Is Queue Empty ?',q1.isEmpty())
q1.enqueue('hi')
q1.enqueue('world')
print ('Items inserted to Queue')
print ('Is Queue Empty ?',q1.isEmpty())
q1.enqueue('oct')
q1.enqueue(4)
q1.print_myqueue()
print ('Queue size:',q1.size())
q1.dequeue()
print ('\nAfter dequeue,Queue contains:')
q1.print_myqueue()
print ('Queue size:',q1.size())
q1.enqueue(2017)
q1.print_myqueue()
print ('Size of Queue:',q1.size())

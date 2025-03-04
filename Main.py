from threading import Thread

from Node import DecoratedNode, QueueDecoratedNode

from LinkedList import LinkedList, SafeLinkedList
from Hashtable import UnsafeHashTable, FastSafeHashTable, SafeHashTable
from Stack import Stack, SafeStack
from UnsafeQueue import UnsafeQueue

stack = SafeStack()

def PushItemsToStack(stack : SafeStack):
    i = 0
    for arf in range(10):
    #while True:
        i += 1
        stack.push(i, i)
        print("Stack pushed: ", stack.__str__())

def PopStack(stack : SafeStack):
    while stack.NodeCount > 0:
        stack.pop()
        print("Stack poped: ", stack.__str__())


if __name__ == "__main__":

    #testing Stack with multitrading
    #t1 = Thread(target=PushItemsToStack, args = (stack, ))
    #t2 = Thread(target=PopStack, args = (stack, ))

    #t1.start()
    #t2.start()

    queue = UnsafeQueue()

    queue.enqueue(1, 1)
    queue.enqueue(2, 2)
    queue.enqueue(3, 3)
    queue.enqueue(4, 4)
    queue.enqueue(5, 5)
    queue.enqueue(6, 6)

    print(queue.__str__())

    print("Dequeue has been started")

    for arg in range(queue.NodeCount):
        queue.dequeue()
        print(queue.__str__())
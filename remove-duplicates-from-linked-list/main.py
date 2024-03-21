class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # index
    currentNode = linkedList
    while currentNode is not None:
        nextDistinct = getNextDistinctValue(currentNode)
        currentNode.next = nextDistinct
        currentNode = nextDistinct

    return linkedList


def getNextDistinctValue(node):
    if node.next is None:
        return None
    if node.next.value != node.value:
        return node.next
    else:
        return getNextDistinctValue(node.next)

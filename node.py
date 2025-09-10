# Implement your Node class here
class Node:
    '''
    A class representing a node in a stack or queue.
    Attributes:
        value (str): Name of item in stack or customer in queue.
        next (str): A reference to the next node in the stack or queue.
    '''

    def __init__(self, value):
        self.value = value
        self.next = None
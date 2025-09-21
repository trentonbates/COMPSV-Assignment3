# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    # Delete the following line and implement your Queue class
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, value):
        new_Node = Node(value)
        if not self.front:
            self.front = new_Node
            self.rear = new_Node
        else:
            self.rear.next = new_Node
            self.rear = new_Node
    
    def dequeue(self):
        if not self.front:
            return None
        removed_Node = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return removed_Node.value

    def peek(self):
        if self.front:
            return self.front.value
        else:
            return None

    def print_queue(self):
        current = self.front
        if not current:
            print('\nQueue is empty.')
        while current:
            print(f'- {current.value}')
            current = current.next

def run_help_desk():
    # Create an instance of the Queue class
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("\nEnter customer name: ")
            # Add the customer to the queue
            queue.enqueue(name)
            print(f"\n{name} added to the queue.")

        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            print(f'\n{queue.dequeue()} has been helped')

        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            print(f'\nNext customer in the queue: {queue.peek()}')

        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            queue.print_queue()

        elif choice == "5":
            print("\nExiting Help Desk System.")
            break
        else:
            print("\nInvalid option.")

if __name__ == "__main__":
    run_help_desk()
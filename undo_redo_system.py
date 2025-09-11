# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here
class Stack:

    def __init__(self):
        self.top = None

    def push(self, value):
        new_Node = Node(value)
        new_Node.next = self.top
        self.top = new_Node
    
    def pop(self):
        if not self.top:
            return None
        removed_Node = self.top
        self.top = self.top.next
        return removed_Node.value

    def peek(self):
        if self.top:
            return self.top.value
        else:
            return None

    def print_stack(self):
        current = self.top
        if not current:
            print('Stack is empty.')
            return
        while current:
            print(f'- {current.value}')
            current = current.next

def run_undo_redo():
    # Create instances of the Stack class for undo and redo
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("\nDescribe the action (e.g., Insert 'a'): ")
            # Push the action onto the undo stack and clear the redo stack
            undo_stack.push(action)
            redo_stack = Stack()

            print(f"Action performed: {action}")
        elif choice == "2":
            # Pop an action from the undo stack and push it onto the redo stack
            if not undo_stack.peek():
                print('\nNo actions to undo.')
            else:
                redo_stack.push(undo_stack.pop())

        elif choice == "3":
            # Pop an action from the redo stack and push it onto the undo stack
            if not redo_stack.peek():
                print('\nNo actions to redo.')
            else:
                undo_stack.push(redo_stack.pop())

        elif choice == "4":
            # Print the undo stack
            print("\nUndo Stack:")
            undo_stack.print_stack()

        elif choice == "5":
            # Print the redo stack
            print("\nRedo Stack:")
            redo_stack.print_stack()
            
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()
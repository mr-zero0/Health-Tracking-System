from setup_logging import logger
 
class Node:
    def __init__(self, name, email, location):
        self.name = name
        self.email = email
        self.location = location
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
 
    def insert(self, name, email, location):
        try:
            new_node = Node(name, email, location)
            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = new_node
            logger.info(f"Node inserted: {name}, {email}, {location}")
        except Exception as e:
            logger.error(f"Error inserting node: {e}")
            raise
 
 
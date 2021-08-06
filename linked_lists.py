class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        current = self.head
        while position > 1:
            if current.next:
                current = current.next
                position -= 1
            else:
                break
        if position == 1:
            return current

        return None

    def insert(self, new_element, position):
        current = self.head
        if position == 1:
            new_element.next = current
            self.head = new_element
            return
        while position > 2:
            if current.next:
                current = current.next
                position -= 1
            else:
                break
        new_element.next = current.next
        current.next = new_element

    def delete(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
            return
        while current.next:
            if current.next.value == value:
                break
            else:
                current = current.next

        current.next = current.next.next

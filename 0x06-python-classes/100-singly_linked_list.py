#!/usr/bin/python3
"""class to represent node of a singly linked list"""


class Node:
    """class to represent node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """class instantiation
        Args:
            data (int): node contents
            next_node (Node): pointer to next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieves node data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """setter for data attribute
        Args:
            value (int): node contents
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """retrieves the next_node attribute"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """setter for next_node attribute
        Args:
            value (Node):
        """
        if (not isinstance(value, Node) and value is not None):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """class to represent a singlylinked list"""
    def __init__(self):
        """Initialization of class SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the list.
            must be in correct sorted position
            in the list (increasing order)
            Args:
                value (Node): node to be inserted
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """Implements how the list is to be printed"""
        output = []
        temp = self.__head
        while temp is not None:
            output.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(output))

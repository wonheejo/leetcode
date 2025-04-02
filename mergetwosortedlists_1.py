
# Defines a node in a singly linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        # val holds the value of the node that it holds
        self.val = val
        # next points to the next node of the linked list (None, if it is the end)
        self.next = next

class Solution(object):
    # Takes to parameters list1 and list2, which are the heads of two linked lists
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # dummy is placeholder node of the empty linked list
        dummy = ListNode()
        # merged is the new linked list with the dummy node at the start 
        merged = dummy

        # keeps the loop going as long as list1 and list2 have nodes within
        while list1 and list2:
            # if the value of the head of list1 is smaller than the value of the head of list2
            if list1.val < list2.val:
                # append the node of list1 to merged list
                merged.next = list1
                # point list1 to the next node
                list1 = list1.next
            else:
                # since list2's value at head is smaller, it will be appended to merged list
                merged.next = list2
                # move list2 node to the next
                list2 = list2.next
            # since new node has been appended, move node to the next(or last) node 
            merged = merged.next
        # after the while loop ends, there still may be a node left, if so, append that node to the next node of the merged list
        merged.next = list1 if list1 else list2

        # return the head of the merged list which dummy.next, not the dummy node itself. 
        return dummy.next

        
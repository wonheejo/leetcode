
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # base case for if list1 or list2 does not have any nodes, return the other node
        if not list1:
            return list2
        if not list2:
            return list1
        
        # if the value at heads of list1 is smaller than list2
        if list1.val < list2.val:
            # recursively merge the list1.next and list2 back to list1.next
            list1.next = self.mergeTwoLists(list1.next, list2)
            # return the head node of list1
            return list1
        else:
            # recursively merge the list2.next and list1 back to list2.next
            list2.next = self.mergeTwoLists(list1, list2.next)
            # return the head node of list2
            return list2
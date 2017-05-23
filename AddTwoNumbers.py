# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers( l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    current1 = l1.next
    current2 = l2.next
        
    head = ListNode(l1.val+l2.val)
    head.next = None
    currentNode = head
        
        
    while current1:
        result = ListNode(current1.val+current2.val)
        result.next = None
        currentNode.next = result
        currentNode = currentNode.next
        current1 = current1.next
        current2 = current2.next
        
    return head

l1Head = ListNode(2)
l1Head.next = ListNode(3)
l1Head.next.next =None
l2Head = ListNode(3)
l2Head.next = ListNode(5)
l2Head.next.next =None
resultHead = addTwoNumbers(l1Head,l2Head)
print(resultHead.val)
            
        
         
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [item for item in lists if item != None]
        if not lists:
            return None
        
        dummy = ListNode()
        cur = dummy

        min_index, min_node = min(enumerate(lists), key=lambda x: x[1].val)

        while lists:
            min_index, min_node = min(enumerate(lists), key=lambda x: x[1].val)

            cur.next = min_node
            if not min_node.next:
                lists.pop(min_index)
            else:
                lists[min_index] = lists[min_index].next

            cur = cur.next
            cur.next = None
        
        return dummy.next
            
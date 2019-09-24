"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

"""


class ListNode:
    """
    definition for a singly-linked list
    """

    def __init__(self, item=None):
        self.item = item
        self.next = None


class Solution:

    def get_intersection_node(self, a_head: ListNode, b_head: ListNode) -> ListNode:
        """
        双指针法，链表拼接:
        1.创建两个指针 pApA 和 pBpB，分别初始化为链表 A 和 B 的头结点。然后让它们向后逐结点遍历。
        2.当 pApA 到达链表的尾部时，将它重定位到链表 B 的头结点 (你没看错，就是链表 B); 类似的，当 pBpB 到达链表的尾部时，
            将它重定位到链表 A 的头结点。
        3.若在某一时刻 pApA 和 pBpB 相遇，则 pApA/pBpB 为相交结点。
        4.想弄清楚为什么这样可行, 可以考虑以下两个链表: A={1,3,5,7,9,11} 和 B={2,4,9,11}，相交于结点 9。
            由于 B.length (=4) < A.length (=6)，pBpB 比 pApA 少经过 22 个结点，会先到达尾部。
            将 pBpB 重定向到 A 的头结点，pApA 重定向到 B 的头结点后，pBpB 要比 pApA 多走 2 个结点。因此，它们会同时到达交点。
        5.如果两个链表存在相交，它们末尾的结点必然相同。因此当 pApA/pBpB 到达链表结尾时，记录下链表 A/B 对应的元素。
            若最后元素不相同,则两个链表不相交。

        :param a_head:
        :param b_head:
        :return:
        """
        if a_head and b_head:
            cur1, cur2 = a_head, b_head
            while cur1 != cur2:
                cur1 = cur1.next if cur1 is not None else b_head
                cur2 = cur2.next if cur2 is not None else a_head
            return cur1

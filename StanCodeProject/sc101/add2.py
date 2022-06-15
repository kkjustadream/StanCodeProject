"""
File: add2.py
Name: 黃勝弘
------------------------
TODO:
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    # ListNode -> string
    s1 = []
    s2 = []
    cur1 = l1
    cur2 = l2
    while cur1 is not None:
        s1.append(cur1.val)
        cur1 = cur1.next
    while cur2 is not None:
        s2.append(cur2.val)
        cur2 = cur2.next
    # s1 = [a1, b1, c1], s2 = [a2, b2, c2]
    # reverse
    x = ''
    y = ''
    for i in range(len(s1)):
        x += str(s1[len(s1)-1-i])
    for i in range(len(s2)):
        y += str(s2[len(s2)-1-i])
    # get total: int, need to reverse back and ListNode
    total = int(x) + int(y)
    total2 = str(total)     # change to string from int

    # turn into ListNode
    node_old = ListNode(int(total2[0]), None)       # first node
    link_list = node_old
    for i in range(len(total2)):
        val = total2[i]
        # first node, but last in link-list
        if i == 0:
            node_old = ListNode(int(val), None)
        else:
            node_new = ListNode(int(val), node_old)     # 往前接
            node_old = node_new
            link_list = node_old
    return link_list


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()

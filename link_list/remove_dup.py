#!/bin/python3

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def remove_duplicates(self,head):
        if head.next == None:
            return head
        h = head
        while h.next != None:
            if h.next.data == h.data:
                h.next = h.next.next
            else:
                h = h.next
        return head


if __name__ == "__main__":
    mylist= Solution()
    T=int(input())
    head=None
    for i in range(T):
        data=int(input())
        head=mylist.insert(head,data)    
    head=mylist.remove_duplicates(head)
    mylist.display(head); 
#!/usr/bin/env python
# coding: utf-8

# In[8]:


class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class LinkedList_Set:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def Create_Set(self,x):
        n=Node(x)
        h=self.head
        if self.head==None:
            self.tail=n
        self.head=n
        self.head.next=h

    def Find_Set(self,x):
        h=self.head
        if x == h.value:
            return h.value
        while h.value != x:
            h=h.next
        return h.value
    
    def GetPrev_Node(self,ref_node):
        curr = self.head
        while (curr and curr.next != ref_node):
            curr = curr.next
        return curr

    def Remove(self,new_node):
        prev_node = self.GetPrev_Node(new_node)
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = new_node.next
    
    def RemoveDuplicates(self,llist):
        curr1 = llist.head
        while curr1:
            curr2 = curr1.next
            value = curr1.value
            while curr2:
                temp = curr2
                curr2 = curr2.next
                if temp.value == value:
                    llist.Remove(temp)
            curr1 = curr1.next

    def Union_Set(self,llist1, llist2):
        if llist1.head is None:
            self.RemoveDuplicates(llist1)
        if llist2.head is None:
            self.RemoveDuplicates(llist2)
        union = llist1
        last_node = union.head
        while last_node.next is not None:
            last_node = last_node.next
        llist2_copy = llist2
        last_node.next = llist2_copy.head
        self.RemoveDuplicates(union)
        return union
     
    def Print_Union(self,llist1,llist2):
        unionset=self.Union_Set(llist1,llist2)
        h=unionset.head
        while h != None:
            print(h.value)
            h=h.next

list1=LinkedList_Set()
list1.Create_Set(15)
list1.Create_Set(14)
list1.Create_Set(14)
list1.Create_Set(13)

list2=LinkedList_Set()
list2.Create_Set(16)
list2.Create_Set(17)
list2.Create_Set(17)
list2.Create_Set(19)

list1.Print_Union(list1,list2)







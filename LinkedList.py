class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class List:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.val)
            printval = printval.next

class Solution:

    def addTwoNumbers(self, l1, l2):
        #dummy = List()
        L = []
        while l1.headval or l2.headval:
            L.append(l1.headval.val + l2.headval.val)
            #dummy.headval.val=l1.headval.val + l2.headval.val
            l1.headval=l1.headval.next
            l2.headval=l2.headval.next
        return L


        #how to change this part into a loop???
        #dummy.headval = ListNode(l1.headval.val + l2.headval.val)
        #dummy.headval.next = ListNode(l1.headval.next.val + l2.headval.next.val)
        #dummy.headval.next.next = ListNode(l1.headval.next.next.val + l2.headval.next.next.val)

        #return dummy


l1= List()
l1.headval=ListNode(2)
l1.headval.next=ListNode(4)
l1.headval.next.next=ListNode(3)
l1.listprint()

l2= List()
l2.headval=ListNode(5)
l2.headval.next=ListNode(6)
l2.headval.next.next=ListNode(4)
l2.listprint()

dummy = List()
dummy.headval= ListNode(l1.headval.val+l2.headval.val)
dummy.headval.next=ListNode(l1.headval.next.val+l2.headval.next.val)
dummy.headval.next.next=ListNode(l1.headval.next.next.val+l2.headval.next.next.val)
dummy.listprint()

print("******************")
#sol = addTwoNumbers(l1,l2)
#sol.listprint()

sol = Solution()
result = sol.addTwoNumbers(l1,l2)
#result.listprint()
print(result)








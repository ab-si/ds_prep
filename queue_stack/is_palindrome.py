import sys

class Solution:
    def __init__(self):
        self.mystack = list()
        self.myqueue = list()

    def push_character(self, char):
        self.mystack.append(char)

    def pop_character(self):
        return(self.myqueue.pop(-1))

    def enqueue_character(self, char):
        self.myqueue.append(char)
    
    def dequeue_character(self):
        return(self.myqueue.pop(0))


if __name__ == "__main__":
    # read the string s
    s=input()
    #Create the Solution class object
    obj=Solution()   

    l=len(s)
    # push/enqueue all the characters of string s to stack
    for i in range(l):
        obj.push_character(s[i])
        obj.enqueue_character(s[i])
    
    isPalindrome=True
    '''
    pop the top character from stack
    dequeue the first character from queue
    compare both the characters
    ''' 
    for i in range(l // 2):
        if obj.pop_character()!=obj.dequeue_character():
            isPalindrome=False
            break
    #finally print whether string s is palindrome or not.
    if isPalindrome:
        print("The word, "+s+", is a palindrome.")
    else:
        print("The word, "+s+", is not a palindrome.")    
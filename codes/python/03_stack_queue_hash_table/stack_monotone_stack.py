import random

def monotoneStack(nums):
    print(str(nums))
    stack = []
    for num in nums:
        while stack and num <= stack[-1]:
            top = stack[-1]
            stack.pop()
            print(str(top) + " 出栈 " + str(stack))
        stack.append(num)
        print(str(num) + " 入栈 " + str(stack))
        
def monotoneIncreasingStack(nums):
    stack = []
    for num in nums:
        while stack and num >= stack[-1]:
            top = stack[-1]
            stack.pop()
            print(str(top) + " 出栈 " + str(stack))
        stack.append(num)
        print(str(num) + " 入栈 " + str(stack))
        
def monotoneDecreasingStack(nums):
    stack = []
    for num in nums:
        while stack and num <= stack[-1]:
            top = stack[-1]
            stack.pop()
            print(str(top) + " 出栈 " + str(stack))
        stack.append(num)
        print(str(num) + " 入栈 " + str(stack))
        

nums = []
for i in range(8):
    nums.append(random.randint(1, 9))
print(nums)
#nums = [4, 3, 2, 5, 7, 4, 6, 8]
monotoneIncreasingStack(nums)
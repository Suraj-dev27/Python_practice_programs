def eval_expression(arr):
    stack=[]
    operator=['+','-','*','/','%']
    for item in arr:
        if item not in operator:
            stack.append(item)
        else:
            first=int(stack.pop())
            second=int(stack.pop())
            if item=='+':
                stack.append(second+first)
            elif item=='-':
                stack.append(second-first)
            elif item=='*':
                stack.append(second*first)
            elif item=='/':
                stack.append(second/first)
            elif item=='%':
                stack.append(second%first)
    return stack[-1]

arr=['2','5','+','3','%']
print('top of stack after postfix:',eval_expression(arr))
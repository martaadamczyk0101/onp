def to_ONP (equation):

    priority={')':4,'^':3, '*':2, '/':2, '+':1, '-':1, '(':0}
    list=equation.split(" ")
    output=[]
    stack=[]

    for char in list:
        if char.isnumeric():
            output.append(char)
        elif char=="(":
            stack.append(char)
        elif char==")":
            while stack[-1]!="(" and not stack == []:
                output.append(stack.pop())
            stack.pop()
        else:
            while len(stack)>0 and priority[char]<=priority[stack[-1]]:
                output.append(stack.pop())
            stack.append(char)

    while len(stack)>0:
        output.append(stack.pop())

    print("".join(output))


def from_ONP(equation):

    list = equation.split(" ")
    stack=[]

    for char in list:
        if char.isnumeric():
            stack.append(char)
        else:
            x=stack.pop()
            y=stack.pop()

            stack.append("("+y + char + x+")" )

    print("".join(stack))

to_ONP("4 * ( 5 - 6 / 3 + 1 ) ^ 2")
from_ONP("1 3 4 2 3 * + * +")

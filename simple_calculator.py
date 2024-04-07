# %% Homework #2

def arithmetic_ops(op):
    num1 = int(input("input 1st number:"))
    num2 = int(input("input 2nd number:"))
    return num1, num2, op(num1, num2)

def add(num1, num2) :
    res = num1 + num2
    return res

def sub(num1, num2) :
    res = num1 - num2
    return res

while True:
    op = input("input operation:")
    if op == "end":
        break   # "반복을 종료"
    elif op == "+":
        num1, num2, ret = arithmetic_ops(add)
    elif op == "-" :
        num1, num2, ret = arithmetic_ops(sub)
    elif op == "*":
        num1, num2, ret = arithmetic_ops(lambda num1, num2: num1 * num2) # 익명함수(lambda) 사용
    elif op == "/":
        num1, num2, ret = arithmetic_ops(lambda num1, num2: num1 / num2)
    elif op == "%" :
        num1, num2, ret = arithmetic_ops(lambda num1, num2: num1 % num2)
    else:
        print("Invalid operation")
        continue
    print(f"{num1}{op}{num2} = {ret}")  # 연산 결과를 출력

print("Exit program")

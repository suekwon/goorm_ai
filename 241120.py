# %%
def is_even(num):
    print("입력값은 ", num, "입니다.")
    if num % 2 == 0:
        return True
    else:
        return False


# result = is_even(10)
# print("is_even 함수로부터 받은 결과값은 ", result, " 입니다.")
# %%
for idx in range(100, 130):
    result = is_even(idx)
    print(idx, ": is_even 함수로부터 받은 결과값은 ", result, " 입니다.")

# %%

# 계산기


def calculator(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    else:
        return "연산자를 잘못 입력하셨습니다."


# %%

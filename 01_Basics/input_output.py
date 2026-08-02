"""input_output.py"""

Num = int(input("Enter a number: ".strip()))
list = []
list1 = []

for i in range(1, Num):
    if i % 2 == 0:
       list.append(i)
    else:
        list1.append(i)

print(f"Even numbers: {list}")
print(f"Odd numbers: {list1}")

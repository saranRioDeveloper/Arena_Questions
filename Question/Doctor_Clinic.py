number = int(input())
result = []

for i in range(1,number + 1):
    if i % 2 == 0:
        result.append("Even")
    else:
        result.append("Odd")

print(" ".join(result))
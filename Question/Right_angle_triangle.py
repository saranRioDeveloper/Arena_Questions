def pattern_printing(N):
    for i in range(N):
        for j in range(i+1):
            print(j+1,end=" ")
        print()

N = int(input("Enter the number :"))
pattern_printing(N)
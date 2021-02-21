def prime_first(num):
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True

def prime_second(num1):
    for i in range(2, num1):
        if (num1 % i == 0):
            return False
    return True

j = 0
for i in range (0,1000):
    if i == 0 :
        continue

    if i < 500 :
        if prime_first(i+1):
            print((i+1), end= ",")
            j += 1
            if (j % 10) == 0:
                print("\n")

    if i > 500:
        if prime_second(i+1):
            print((i+1), end= ",")
            j+=1
            if (j % 10) == 0:
                print("\n")




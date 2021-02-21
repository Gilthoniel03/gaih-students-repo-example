import random
prime_list = []
def prime_number(num):
    for i in range (2,num):
        if num %i ==0 :
            return False
    return True

for i in range(1,100):
    if prime_number(1+i):
         prime_list.append(1+i)


for i in range(3):
    print(random.sample(prime_list,3))




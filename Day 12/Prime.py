def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            print (f"{num} % {i} = {num % i }")
            return False
        print(f"{num} % {i} = {num % i}")
    return True


print(is_prime(14))
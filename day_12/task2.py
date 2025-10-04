def is_prime(num):
    prime_status = False
    for value in range(2,10):
        if num == value:
            continue
        if num % value == 0:
            prime_status = False
            return prime_status
        else:
            prime_status = True
    return prime_status 

print(is_prime(2))

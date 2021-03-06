# Uses python3
import math
fib_dict = {}

def get_fibonacci(n):
    global fib_dict

    if n <= 1:
        return n

    elif(n in fib_dict):
        # print("called")
        return fib_dict[n]

    elif n <= 70:
        # print("less than 70 called", n)
        phi = ((1+math.sqrt(5))/2)**n
        fib_dict[n] = int(round(phi/math.sqrt(5)))
        return fib_dict[n]

    elif(n%2 == 0):
        k = n//2
        fib_dict[n] = (2*get_fibonacci(k-1) + get_fibonacci(k))*get_fibonacci(k)
        return fib_dict[n]

    else:
        k = (n+1)//2
        fib_dict[n] = get_fibonacci(k)*get_fibonacci(k) + get_fibonacci(k-1)*get_fibonacci(k-1)
        return fib_dict[n]

def get_Pisano_period(m):
    a = 0
    b = 1
    for i in range(0,m**2):
        c = (a+b)%m
        a = b
        b = c
        if(a==0 and b==1):
            return i+1

if __name__ == '__main__':

    m, n = map(int, input().split())
    divisor = get_Pisano_period(10)
    remainder_m = (m+1) % divisor
    remainder_n = (n+2) % divisor

    sum_last = (get_fibonacci(remainder_n) - get_fibonacci(remainder_m))
    # print(get_fibonacci(n+2))
    print(sum)

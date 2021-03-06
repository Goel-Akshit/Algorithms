# Fn mod m is periodic. The period always starts with 01 and is known as Pisano period.
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

    n, m = map(int, input().split())
    remainder = n % get_Pisano_period(m)
    print(get_fibonacci(remainder) % m)

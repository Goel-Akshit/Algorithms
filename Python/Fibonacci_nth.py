# Uses python3
import math
fib_dict = {}

def get_fibonacci_last_digit(n):
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
        fib_dict[n] = (2*get_fibonacci_last_digit(k-1) + get_fibonacci_last_digit(k))*get_fibonacci_last_digit(k)
        return fib_dict[n]

    else:
        k = (n+1)//2
        fib_dict[n] = get_fibonacci_last_digit(k)*get_fibonacci_last_digit(k) + get_fibonacci_last_digit(k-1)*get_fibonacci_last_digit(k-1)
        return fib_dict[n]

if __name__ == '__main__':

    n = int(input())
    print(get_fibonacci_last_digit(n)%10)

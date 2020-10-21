#Rabin- karps's imporved hash function calculation technique
# idea: polunomial hashes of two consecutive substring are very similar.
# p and x can be selected at random and  helps in avoiding collision.

def hashFunction(string, p=1000000007, x=263):
    hashCode = 0
    for i in range(len(string)-1, -1, -1):
        hashCode = (hashCode * x + ord(string[i])) % p
    return hashCode

def preProcessing(string, T, P, p=1000000007):
    x = 263
    hIndex = (T-P+1)
    H = [0]*hIndex
    s = string[T-P:]
    hIndex -= 1
    H[hIndex] = hashFunction(s, p, x)
    powerValue = 1
    for i in range(P):
        powerValue = (powerValue*263)%p
    for i in range(T-P-1, -1, -1):
        H[hIndex-1] = (x*H[hIndex] + ord(string[i]) - powerValue*(ord(string[i+P])))%p
        hIndex -= 1
    return H

if __name__ == "__main__":
    string = 'abcabd'
    pattern = 'ab'
    patternHashCode = hashFunction(pattern)
    print(patternHashCode)
    H = preProcessing(string, len(string), len(pattern))




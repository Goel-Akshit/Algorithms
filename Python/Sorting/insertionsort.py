def insertionsort(a):
    array = a[:]

    for i in range(1,len(array)):
        j = i-1
        checker = a[i]
        while(j >=0 and array[j] > checker):
            array[j + 1] = array[j]
            j -= 1

        array[j+1] = checker

    return(array)


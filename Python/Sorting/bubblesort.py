def bubblesort(a):
    array = a[:]

    for i in range(len(array)):
        for j in range(0,len(array) - i -1):
            if(array[j] > array[j+1]):
                array[j],array[j+1] = array[j+1],array[j]

    return(array)


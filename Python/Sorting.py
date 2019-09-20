def mergesort(array):
    if(len(array) > 1):
        mid = len(array)//2
        temp_left = array[:mid]
        temp_right = array[mid:]

        mergesort(temp_left)
        mergesort(temp_right)

        i=j=k=0

        while(i < len(temp_left) and j < len(temp_right)):
            if(temp_left[i] < temp_right[j]):
                array[k] = temp_left[i]
                i += 1

            else:
                array[k] = temp_right[j]
                j += 1

            k += 1

        while(i < len(temp_left)):
            array[k] = temp_left[i]
            i += 1
            k += 1

        while(j < len(temp_right)):
            array[k] = temp_right[j]
            j += 1
            k += 1

        return(array)


print(mergesort([5,4,3,9,7]))

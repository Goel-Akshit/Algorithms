def BinarySearch(arr, l, r, value):

    if(r >=l):
        mid = (l+r)//2

        if(arr[mid] == value):
            return mid
        elif(arr[mid] > value):
            return BinarySearch(arr, l, mid-1, value)
        else:
            return BinarySearch(arr, mid+1, r, value)

    else:
        return -1


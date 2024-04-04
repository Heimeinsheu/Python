def insertion_sort(array_):
    for i in range(1, len(array_)):
        j = i-1
        key = array_[i]
        print("Key: ",key)
        print("j value: ",array_[j],"| j index:",j)
        print("before: ",array_)
        while(key<array_[j] and j>=0):
            array_[j+1] = array_[j]
            j = j-1

        
        array_[j+1]=key
        
        print("after: ",array_)
        print(" ")

array_ = [989,78,67,544,342,1,12,43]
insertion_sort(array_)
print("Insertion Sort: ", array_)



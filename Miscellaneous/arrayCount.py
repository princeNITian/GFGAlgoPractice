# By making elements negative.
# Time-Complexity = O(n) , Space-Complexity = O(1)
def frequency1(arr,n):

    i = 0
    while i<n:
        if arr[i]<=0:
            i += 1
            continue
    
        elIndex = arr[i] - 1

        if arr[elIndex]>0:
            arr[i] = arr[elIndex]
            arr[elIndex] = -1

        else:
            arr[elIndex] -= 1
            arr[i] = 0
            i += 1

    print('Frequencies are as follows: ')
    for i in range(0,n):
        print(i+1,'->',abs(arr[i]))


# By adding n to keep track of counts
# Time-Complexity = O(n) and Space-Complexity = O(1)
def frequency2(arr,n):

    for i in range(n):
        arr[i] = arr[i] - 1

    for i in range(n):
        arr[arr[i]%n] = arr[arr[i]%n] + n

    for i in range(n):
        print(i+1,"->",arr[i]//n)
    

if __name__=="__main__":
    n = 7
    arr = [4,5,2,1,3,4,7]
    frequency1(arr,n)
    # print('Frequency2 method invoked: ')
    # frequency2(arr,n)
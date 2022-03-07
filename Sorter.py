# A simple recursive sorting algorithm
arr = [645,4654,654,654,65,4234,5484,56412,464,65,4894,942,1354,65484,153124345,4564]

def sort():
    i=0
    while i<len(arr)-1:
        if arr[i]>arr[i+1]:
            a= arr.pop(i)
            arr.insert(i+1,a)
            sort()
        i+=1
sort()
print(arr)

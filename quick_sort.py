def quick_sort(x):
    pivot = x[-1]
    print(f"pivot: {pivot}")
    left = [x for x in arr [: -1] if x <= pivot]
    right = [x for x in arr[: - 1]if x> pivot]
    print(f"left; {left}, right: {right}")
    return quick_sort(left) + pivot + quick_sort(right)
def search_element(x,element):
    found = False
    for i in range(len(x)):
        for j in range(len(x)):
            if arr[i][j] == element:
                print(f"Element found at position {i} ")
                found = True
                return
    if not found:
        print("Element not found is the given array")
    remove_data = x
    if remove_data in x:
        x.remove(remove_data)
        del x.arr[remove_data]
        print("Array Available", x)
    else:
        print("Number Not Found")

x=print(input("Enter the array elements seperated by spaces: "))
y = list(x)
print(f"Array: {y}")
quick_sort(x)
search= ("Enter the element to search: ")
search_element(x,search)






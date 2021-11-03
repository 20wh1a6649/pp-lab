def taking_input():
    size = int(input())
    print("Enter Elements in sorted order")
    l = []
    for i in range(size):
        ele = int(input())
        l.append(ele)
    return l
def binary_search(lst, low, high, key):
    while(low <= high):
        mid = (low + high) // 2
        if(lst[mid] == key):
            return mid
        elif(lst[mid] < key):
            return binary_search(lst, mid + 1, high, key)
        elif(lst[mid] > key):
            return binary_search(lst, low, mid - 1, key)
    return -1
def main():
    l = taking_input()
    key = int(input("Enter element to be searched : "))
    low = 0
    high = len(l) - 1
    pos = binary_search(l,low, high, key)
    if pos == -1:
        return "element not found"
    else:
        return f"element found at {pos + 1}"
print(main())




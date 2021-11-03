def taking_input():
    size = int(input())
    print("Enter elements in sorted order : ")
    l = []
    for i in range(size):
        ele = int(input())
        l.append(ele)
    return l 

def binary_search(lst, key):
    low = 0
    high = len(lst) - 1
    while(low <= high):
        mid = (low + high) // 2
        if(lst[mid] == key):
            return mid
        elif(lst[mid] < key):
            low = mid + 1
        elif(lst[mid] > key):
            high = mid - 1
    return -1
def main():
    l = taking_input()
    key = int(input("Element to be searched : "))
    pos = binary_search(l, key)
    if pos == -1:
        return "element not found"
    else:
        return f"element found at {pos + 1}"
print(main())




def taking_input():
    size = int(input())
    l = []
    for i in range(size):
        ele = int(input())
        l.append(ele)
    return l


def linear_search_recursion(lst, index, key):
    

    if lst[index] == key:
        return index 
    else:
        
        return linear_search_recursion(lst,index + 1, key)
    return -1
    
def main():
    l = taking_input()
    key = int(input("Element to be searched : "))
    index = 0
    pos = linear_search_recursion(l, index, key)
    if pos == -1:
        return "element not found"
    else:
        return f"element found at {pos + 1}"
print(main())




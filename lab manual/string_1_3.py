str1 = input("Enter string 1 : ")
str2 = input("Enter string 2 : ")
print(f"concatinating {str1} and {str2} = {str1 + str2}")
print(f"printing str1 multiple times = ", str1 * 10)
print(f"{str1} - str[0] : ", str1[0])
print(f"{str1} - str[:] : ", str1[:])
print(f"{str1} - str[::-1] : ", str1[::-1])
print(f"{str1} - str[2:] : ", str1[2:])

'''
INPUT:
Enter string 1 : 
Good
Enter string 2 : 
Morning

OUTPUT:
concatinating Good and Morning = GoodMorning
printing str1 multiple times =  GoodGoodGoodGoodGoodGoodGoodGoodGoodGood
Good - str[0] :  G
Good - str[:] :  Good
Good - str[::-1] :  dooG
Good - str[2:] :  od


'''

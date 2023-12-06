def countChar(inputString):
    count={}
    for char in inputString:
        if char in count:
            count[char]+=1
        else:
            count[char]=1
        return count
str2=input("Enter a string:")
result = countchar(str2)
print(result)

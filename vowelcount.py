def vowel_count(x):
    count =0
    vowel= set("aeiouAEIOU")
    for i in x:
        if i in vowel:
            count=count+1
    return count

x = input("Input:")
k = vowel_count(x)
print(k)

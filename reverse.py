def reverse(str):
    s = ""
    for ch in str:
        s = ch + s
    return s

n=input("enter your string:")
print("Given String: ", n)

print("Reversed String: ", reverse(n))
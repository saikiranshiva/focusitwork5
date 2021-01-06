def sum_count_reverse(n):

    sum=0
    for i in str(n):
        sum=sum+int(i) 
    print(sum)


    
    count=0
    while (n > 0):

        count=count+1
        n=n//10
    print(count)

n=int(input("enter your number"))
sum_count_reverse(n)

        
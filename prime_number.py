def prime(ending):
    
    for i in range(2,ending+1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            print(i,"prime number")
        else:
            print(i,"not a prime number ")
    
    


end=int(input("enter your end range number  "))

prime(end)
def MagicM(n):  
    M = [[0 for x in range(n)]  for y in range(n)] 
    a = n / 2
    b = n - 1
    num = 1
    while num <= (n * n): 
        if a == -1 and b == n:  
            b = n - 2
            a = 0
        else:          
            if b == n: 
                b = 0    
              
            if a < 0:
                a = n - 1
        if M[int(a)][int(b)]:
            b = b - 2
            a = a + 1
            continue
        else: 
            M[int(a)][int(b)] = num 
            num = num + 1
            b = b + 1
            a = a - 1

        
    print ("Number of Values for n: ", n) 
    print ("Sum of each row or column: ",n * (n * n + 1) / 2, "\n") 
    for i in range(0, n): 
        for j in range(0, n): 
            print('%2d ' % (M[i][j]),end = '') 
             
            if j == n - 1:  
                print()



n=int(input("Number of rows of the Magic Matrix: "))
MagicM(n)

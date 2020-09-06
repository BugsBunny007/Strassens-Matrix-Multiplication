#Matrix multiplication using Strassens Algorithm 

while(True):
        print("----Enter first matrix details--------")
        size = int(input("Enter the number of rows & columns :"))#as we know strassen algo. will be applicable only to matrix's of size n*n
    #if (size%2!=0):
     #   print (size,"is not valid please enter the correct size Note only even no. are allowed")
      #  break
            
    #else:
        # Initialize matrix 
        #row = int(input("Enter the number of rows :"))
        #col = int(input("Enter the number of columns :"))    
        a= [] 
        print("Enter the entries row-wise:") 

        # For user input 
        for i in range(size):          # x for loop for row entries 
            x =[] 
            for j in range(size):      # x for loop for column entries 
                 x.append(int(input())) 
            a.append(x) 
          
        # For printing the matrix 
        print("First matrix is :-")    
        for i in range(size): 
            print("Row:",i+1)
            for j in range(size): 
                print(a[i][j]) 
        

        print("----Enter Second matrix details--------")
        # Initialize matrix 
        #row = int(input("Enter the number of rows :"))
        #col = int(input("Enter the number of columns :"))    
               
        b= [] 
        print("Enter the entries row wise:") 

        # For user input 
        for i in range(size):          # y for loop for row entries 
            y=[] 
            for j in range(size):      # y for loop for column entries 
                 y.append(int(input())) 
            b.append(y) 
        print("Second matrix is :-")    
        for i in range(size): 
            print("Row:",i+1)
            for j in range(size): 
                print(b[i][j])


        def new_m(p, q): # create a matrix filled with 0s
            matrix = [[0 for size in range(p)] for size in range(q)]
            return matrix

        def straight(a, b): # multiply the two matrices
            if len(a[0]) != len(b): # if # of col != # of rows:
                return "Matrices are not m*n and n*p"
            else:
                p_matrix = new_m(len(a), len(b[0]))
                for i in range(len(a)):
                    for j in range(len(b[0])):
                        for k in range(len(b)):
                            p_matrix[i][j] += a[i][k]*b[k][j]
            return p_matrix

        def split(matrix): # split matrix into quarters 
            a = matrix
            b = matrix
            c = matrix
            d = matrix
            while(len(a) > len(matrix)/2):
                a = a[:len(a)/2]
                b = b[:len(b)/2]
                c = c[len(c)/2:]
                d = d[len(d)/2:]
            while(len(a[0]) > len(matrix[0])/2):
                for i in range(len(a[0])/2):
                    a[i] = a[i][:len(a[i])/2]
                    b[i] = b[i][len(b[i])/2:]
                    c[i] = c[i][:len(c[i])/2]
                    d[i] = d[i][len(d[i])/2:]
            return a,b,c,d
                    
        def add_m(a, b):
            if type(a) == int:
                d = a + b
            else:
                d = []
                for i in range(len(a)):
                    c = []
                    for j in range(len(a[0])):
                        c.append(a[i][j] + b[i][j])
                    d.append(c)
            return d

        def sub_m(a, b):
            if type(a) == int:
                d = a - b
            else:
                d = []
                for i in range(len(a)):
                    c = []
                    for j in range(len(a[0])):
                        c.append(a[i][j] - b[i][j])
                    d.append(c)
            return d


        def strassen(a, b, q):
            # base case: 1x1 matrix
            if q == 1:
                d = [[0]]
                d[0][0] = a[0][0] * b[0][0]
                return d
            else:
                #split matrices into quarters
                a11, a12, a21, a22 = split(a)
                b11, b12, b21, b22 = split(b)
            
                # p1 = (a11+a22) * (b11+b22)
                p1 = strassen(add_m(a11,a22), add_m(b11,b22), q/2)
                
                # p2 = (a21+a22) * b11
                p2 = strassen(add_m(a21,a22), b11, q/2)

                # p3 = a11 * (b12-b22)
                p3 = strassen(a11, sub_m(b12,b22), q/2)

                # p4 = a22 * (b12-b11)
                p4 = strassen(a22, sub_m(b12,b11), q/2)

                # p5 = (a11+a12) * b22
                p5 = strassen(add_m(a11,a12), b22, q/2)

                # p6 = (a21-a11) * (b11+b12)
                p6 = strassen(sub_m(a21,a11), add_m(b11,b12), q/2)

                # p7 = (a12-a22) * (b21+b22)
                p7 = strassen(sub_m(a12,a22), add_m(b21,b22), q/2)


                # c11 = p1 + p4 - p5 + p7
                c11 = add_m(sub_m(add_m(p1, p4), p5), p7)

                # c12 = p3 + p5
                c12 = add_m(p3, p5)

                # c21 = p2 + p4
                c21 = add_m(p2, p4)

                # c22 = p1 + p3 - p2 + p6
                c22 = add_m(sub_m(add_m(p1, p3), p2), p6)

                c = new_m(len(c11)*2,len(c11)*2)
                for i in range(len(c11)):
                    for j in range(len(c11)):
                        c[i][j]                   = c11[i][j]
                        c[i][j+len(c11)]          = c12[i][j]
                        c[i+len(c11)][j]          = c21[i][j]
                        c[i+len(c11)][j+len(c11)] = c22[i][j]
            
                return c

        #print "Strassen Outputs:"
       # print strassen(a, b, 4)
        print "Should be:"
        print straight(a,b)

#OUTPUT:-
#python SMM.py 
#----Enter first matrix details--------
#Enter the number of rows & columns :3
#Enter the entries row-wise:
#1
#2
#3
#4
#5
#6
#7
#8
#9
#First matrix is :-
#('Row:', 1)
#1
#2
#3
#('Row:', 2)
#4
#5
#6
#('Row:', 3)
#7
#8
#9
#----Enter Second matrix details--------
#Enter the entries row wise:
#1
#2
#3
#4
#5
#6
#7
#8
#9
#Second matrix is :-
#('Row:', 1)
#1
#2
#3
#('Row:', 2)
#4
#5
#6
#('Row:', 3)
#7
#8
#9
#Should be:
[[30, 36, 42], [66, 81, 96], [102, 126, 150]]
#----Enter first matrix details--------
#Enter the number of rows & columns :


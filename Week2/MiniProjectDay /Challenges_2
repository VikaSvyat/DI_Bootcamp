n = 5 #int(input("Enter number of rows: "))

# row =""
# for j in range (n):
#     for i in range (0+j,n*2-1-j):
#         row+='*'
#     print (row) 
#     row = " "*(j+1)
    
row1=''
for j in range (n):
    row1 = ' '*(n-(j+1))
    for i in range(2*j+1):
        row1+='*'
    print(row1)
    
row2=''
for j in range(n):
    row2 = ' '*(n-(j+1))
    for i in range(j+1):
        row2+='*'
    print(row2)
    
row3=''
for i in range(n+1):
    row3 +=' '      #create row, length n
for j in range(n):
    for i in list(range(j)):   
        row3 =row3[:i] +'*' +row3[i+1:]
    print (row3)    
for j in range(n):
    for i in list(range(j)):
        # print(i)
        row3 =row3[:i] +' ' +row3[i+1:]
    print (row3)     
    
#bubble sort
my_list = [2, 24, 12, 354, 233]     #creating list of numbers
for i in range(len(my_list) - 1):   #iterating by index of list
    minimum = i                     # fixing previos element for second loop
    for j in range( i + 1, len(my_list)):   #iterating from next index
        if(my_list[j] < my_list[minimum]):  #comparing current with previous
            minimum = j                     #if current less then move minimum
            if(minimum != i):               #if was changing, swop elements
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
print(my_list)  
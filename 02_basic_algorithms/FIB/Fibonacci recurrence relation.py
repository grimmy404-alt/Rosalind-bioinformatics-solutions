#Opening the dataset

file= input('Enter file name:')
with open(file,"r") as f:               #with automatically closes the file
    data=f.read().split()

#Storing the integer data in n and k

n= int(data[0])
k= int(data[1])

#Validating constraints

if not(1<=n<=40 and 1<=k<=5):
    print('Data too large or Invalid!')
    exit()              #Stopping script

#Base cases; month 1= 1 pair and month 2= 1 pair as well

if n==1 or n==2:
    print (1)

#Initialising PM1(previous month) and PM2 to store the numbers

else:
    PM1=1
    PM2=1

#Calculating population (CM= current month) upto n months

for month in range(3,n+1):
    CM= PM1 + k * PM2               #Applying fibonacci recurrence relation 
    PM2= PM1                        #Updating values
    PM1= CM

#Printing result after loop is complete

print (PM1)

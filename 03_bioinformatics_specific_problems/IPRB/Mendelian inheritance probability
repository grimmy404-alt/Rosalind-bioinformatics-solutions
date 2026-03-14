# parsing data
file= input('Enter file name:')
with open(file,"r") as f:
    data= f.read().split()

# k- homozygous dominant; m- heterozygous; n- homozygous recessive
k= int(data[0])
m= int(data[1])
n= int(data[2])

# N- toatal population
N=k+m+n 

# probability of both parents being heterozygous
p1= (m/N) * ((m-1)/(N-1)) * 0.25

# probability of parents being heterozygous and homozygous recessive
p2= (m/N) * (n/(N-1))* 0.5

# probability of parents being homozygous recessive and heterozygous
p3= (n/N) * (m/(N-1)) * 0.5

# probability of parents being homozygous recessive
p4= (n/N) * ((n-1)/(N-1)) * 1

# probability of dominant offspring=1−Probability of recessive offspring
p_rec= p1+p2+p3+p4

p_dom= 1-(p_rec)

print (f"{p_dom:5f}")

x = int(input())
y = int(input())
z = int(input())
n = int(input())

permutations = []
x_values = range(0, x+1)
y_values = range(0, y+1)
z_values = range(0, z+1)
    
    
    
for i in x_values:
    for j in y_values:
        for k in z_values:
            sum = i+j+k
            if sum != n and i<= x and j<=y and k<=z:
                each = [i,j,k]
                permutations.append(each)
print(permutations)
                    
                    
import numpy as np
#1. Using Neville’s method, find the 2nd degree interpolating value for f(3.7) for the following set of data 
#x f(x) 
#3.6 1.675 
#3.8 1.436 
#3.9 1.318 

#creating a 3x3 matrix
def nevilles(x_points, y_points, x):
    nevilles_matrix = np.zeros((3,3))
    for counter, row in enumerate(nevilles_matrix):
        row[0] = y_points[counter]
    num_of_points = len (x_points)
    for i in range(1, num_of_points):
        for j in range(1,i+1):
            first_multiplication = (x - x_points[i-j]) * nevilles_matrix[i][j-1]
            second_multiplication = (x - x_points[i]) * nevilles_matrix[i-1][j-1]
            denominator = x_points[i] - x_points[i-j]
            coefficient = (first_multiplication - second_multiplication)/denominator
            nevilles_matrix[i][j] = coefficient
    print(nevilles_matrix[len(x_points)-1][len(x_points)-1])
    return nevilles_matrix

    
#4.  Using the divided difference method, print out the Hermite polynomial approximation matrix 
#x f(x) f’(x) 
#3.6 1.675 -1.195 
#3.8 1.436 -1.188 
#3.9 1.318 -1.182 

np.set_printoptions(precision=7, suppress=True, linewidth=100)
def div_difference(matrix: np.array):
    size = len(matrix)
    for i in range(2, size):
        for j in range(2, i+2):
            if j >= len(matrix[i]) or matrix[i][j] != 0:
                continue
            left: float = matrix[i][j-1]
            diagonal_left: float = matrix[i-1][j-1]
            numerator: float = ( left - diagonal_left )
            denominator = matrix[i][0]- matrix[i-j+1][0]
            operation = numerator / denominator
            matrix[i][j] = operation
    
    return matrix
def hermite():
#plugging in given values
    x_points = [3.6, 3.8, 3.9]
    y_points = [1.675, 1.436, 1.318]
    slopes = [-1.195, -1.188, -1.182] 
    num_of_points = 2*len(x_points)
    matrix = np.zeros((num_of_points, num_of_points))
    counter = 0
    for x in range(0, num_of_points,2):
        matrix[x][0] = x_points[counter]
        matrix[x+1][0] = x_points[counter]
        counter +=1
        
    counter = 0
    for x in range(0,num_of_points, 2):
        matrix[x][1] = y_points[counter]
        matrix[x+1][1] = y_points[counter]
        counter +=1

    counter = 0
    for x in range(1,num_of_points,2):
        matrix[x][2] = slopes[counter]
        counter +=1

    filled_matrix = div_difference(matrix)
    print(filled_matrix)
    
#2. Using Newton’s forward method, print out the polynomial approximations for degrees 1, 2, and 3 using the following set of data 
#a.  Hint, create the table first 
#b.  
#x f(x) 
#7.2 23.5492 
#7.4 25.3913 
#7.5 26.8224 
#7.6 27.4589 
#creating a 4x4 matrix
def div_dif(x_points, y_points):
    size: int = len(x_points)
    dd_matrix: np.array = np.zeros((4,4))
#plugging in given values
    for index, row in enumerate(dd_matrix):
        row[0] = y_points[index]
    for i in range(1, size):
        for j in range(1, i+1):
            numerator = dd_matrix[i][j-1] - dd_matrix[i-1][j-1]
            denominator = x_points[i] - x_points[i-j]
            operation = numerator / denominator
            dd_matrix[i][j] = (operation)
    return dd_matrix
#getting the polynomial approximations for df =1,2,3
def approx_result(dd_matrix, x_points, value):
    reoc_x_span = 1
    reoc_px_result = dd_matrix[0][0]
    for index in range(1, len(x_points)):
        polynomial_coefficient = dd_matrix[index][index]
        reoc_x_span *= (value - x_points[index-1])
        mult_operation = polynomial_coefficient * reoc_x_span
        reoc_px_result += mult_operation
    return reoc_px_result

if __name__ == "__main__":
#plugging in given values
    x_points = [7.2, 7.4, 7.5, 7.6]
    y_points = [23.5492, 25.3913, 26.8224, 27.4589]
    div_table = div_dif(x_points, y_points)
    
    Array = [] 
    for i in range(1, len(x_points)):
        Array.append(div_table[i][i])
    #print(Array)
    #hermite()
 
#3.  Using the results from 3, approximate f(7.3)? 
    approximating_x = 7.3
    approx = approx_result(div_table, x_points, approximating_x)
    #print(approx)
    #print()

#plugging in the given values    
    x_points = [3.6, 3.8, 3.9]
    y_points = [1.675, 1.436, 1.318]
    approx_value = 3.7
    nevilles(x_points, y_points, approx_value)
    print()
    

 
#5. Using cubic spline interpolation, solve for the following using this set of data: 
  
#x f(x) 
#2 3 
#5 5 
#8 7 
#10 9 
 
  
#plugging in the given values
x_data = np.array([2, 5, 8, 10])
y_data = np.array([3, 5, 7, 9])
# a)Find matrix A
n = len(x_data)
a = np.zeros((n, n))
a[0, 0] = 1
a[n-1, n-1] = 1
for i in range(1, n-1):
    a[i, i-1] = x_data[i] - x_data[i-1]
    a[i, i] = 2 * (x_data[i+1] - x_data[i-1])
    a[i, i+1] = x_data[i+1] - x_data[i]
#print(a)
#print()
    
# b) Vector b
b = np.zeros(n)
for i in range(1, n-1):
    b[i] = 3 * (y_data[i+1] - y_data[i]) / (x_data[i+1] - x_data[i]) - \
           3 * (y_data[i] - y_data[i-1]) / (x_data[i] - x_data[i-1])
#print(b)
#print()

# c) Vector x
x = np.linalg.solve(a, b)
#print(x)


#printing results
#1

#2
print(Array)
print()

#3
print(approx)
print()

#4
hermite()
print()

#5
print(a)
print()

print(b)
print()

print(x)


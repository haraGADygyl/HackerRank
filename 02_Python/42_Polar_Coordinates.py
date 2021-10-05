import cmath

complex_number = complex(input())
result = cmath.polar(complex_number)

print(f'{result[0]:.3f}\n{result[1]:.3f}')

import math as m

class point:
    def __init__(self, x_val, y_val):
        self.x = x_val
        self.y = y_val

def n_deriv(p1, p2):
    return (p2.y - p1.y) / (p2.x - p1.x)
    
def get_mid(x,y):
    return .5 * x + .5 * y

def get_d_point(p1, p2):
    x_val = get_mid(p1.x, p2.x)
    y_val = n_deriv(p1, p2)
    return point(x_val, y_val)

def getPstring(p):
    return "[" + str(p.x) + ", " + str(p.y) + "]"

def printAll(lop):
    for p in lop:
        print(getPstring(p))

def get_zero(p1, p2):
    m = n_deriv(p1, p2)
    b = p1.y - m * p1.x
    return -1 * b / m

def gen_derivs(lop):
    ds = []
    for ind in range(0, len(lop) - 1):
        ds.append(get_d_point(lop[ind], lop[ind + 1]))
    return ds
        
phs = [4.47, 4.72, 5.04, 5.22, 5.38, 5.62, 5.86, 5.98, 6.09, 6.36, 7.36, 10.29, 11, 11.27, 11.46, 11.59, 11.81]
volumes = [2.01, 4.35, 8.74, 11.44, 13.93, 16.96, 18.95, 19.85, 20.42, 21.44, 23.07, 23.32, 24.43, 25.73, 27.2, 29, 34.03]

n = len(phs)

points = []
for ind in range(0, n):
    points.append(point(volumes[ind], phs[ind]))


deriv_points = gen_derivs(points)
second_deriv_points = gen_derivs(deriv_points)

print("\n Points \n")
printAll(points)

print("\n Derivs \n")
printAll(deriv_points)

print("\n Second Derivs \n")
printAll(second_deriv_points)

print("\n")


i = 0
while second_deriv_points[i].y > 0 or m.fabs(second_deriv_points[i].y - second_deriv_points[i-1].y) < 1:
    i += 1
    
print("Positive Point: " + getPstring(second_deriv_points[i - 1]))
print("Negative Point: " + getPstring(second_deriv_points[i]))

eq_pt = get_zero(second_deriv_points[i - 1], second_deriv_points[i])

print("Computed Equivalence Point: " + str(eq_pt))


    
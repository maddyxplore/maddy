"""
You are required to write the code. You can click on compile & run anytime to check the compilation/ execution status of the program. The submitted code should be logically/syntactically correct and pass all the test cases.

Ques: The program is supposed to calculate the distance between three points.

For
x1 = 1 y1 = 1
x2 = 2 y2 = 4
x3 = 3 y3 = 6

Distance is calculated as : sqrt(x2-x1)2 + (y2-y1)2

ans:
"""
x1,y1 = 1,1
x2,y2 = 2,4
x3,y3 = 3,6

def sqrt(x,y,x1,y1):
    res = (((y-x)**2) + ((y1-x1)**2))**0.5
    return int(res)

print(sqrt(x1,y1,x2,y2),sqrt(x2,y2,x3,y3),sqrt(x3,y3,x1,y1))

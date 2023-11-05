class point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

p = int(input("x: "))
p1 = int(input("y: "))
p = point(p, p1)

print(f"the value of point x:{p.x} &y:{p.y}")
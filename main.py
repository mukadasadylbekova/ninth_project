import random
from shapes.sphere import Sphere
from shapes.cylinder import Cylinder
from shapes.cube import Cube

shapes = []

for _ in range(10):
    shape_type = random.choice(['Sphere', 'Cylinder', 'Cube'])
    if shape_type == 'Sphere':
        r = random.randint(1, 10)
        shape = Sphere(r)
    elif shape_type == 'Cylinder':
        r = random.randint(1, 10)
        h = random.randint(5, 20)
        shape = Cylinder(r, h)
    else:
        a = random.randint(1, 10)
        shape = Cube(a)
    shapes.append((shape_type, shape))

print(f"{'Shape':<10} {'Surface Area':<20} {'Volume':<20}")
print("=" * 50)
for name, shape in shapes:
    print(f"{name:<10} {shape.surface_area():<20.2f} {shape.volume():<20.2f}")


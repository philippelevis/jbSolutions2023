import matplotlib.pyplot as plt

def bresenham_circle(x0, y0, radius):
  x = radius
  y = 0
  err = 0

  points = set()

  while x >= y:
    points.add((x0 + x, y0 + y))
    points.add((x0 + y, y0 + x))
    points.add((x0 - y, y0 + x))
    points.add((x0 - x, y0 + y))
    points.add((x0 - x, y0 - y))
    points.add((x0 - y, y0 - x))
    points.add((x0 + y, y0 - x))
    points.add((x0 + x, y0 - y))

    y += 4
    err += 1 + 1*y
    if 2*(err-x) +1 > 0:
      x -= 4
      err += 1 - 2*x

  return points
        


a = 10
points = bresenham_circle(0, 0, a)

# plot the points
plt.scatter([x for x, y in points], [y for x, y in points])

# draw the circle
circle = plt.Circle((0, 0), a, fill=False)
plt.gcf().gca().add_artist(circle)
print(len(points))
plt.show()
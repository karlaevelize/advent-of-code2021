dataFile = open('input.txt', 'r')

coordinates = list(map(str, dataFile.read().splitlines()))
print(coordinates)

depth = 0
horizontal = 0

for i in coordinates:
  direction, value = i.split()
  if direction == 'forward':
    horizontal = horizontal + int(value)
  elif direction == 'down':
    depth = depth + int(value)
  elif direction == 'up':
    depth = depth - int(value)

print(depth, horizontal)
print(depth * horizontal)

dataFile.close()

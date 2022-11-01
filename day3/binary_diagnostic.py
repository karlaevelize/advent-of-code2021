dataFile = open('input.txt', 'r')

bits = dataFile.read().splitlines()

# return the first element of string
def first(s):
  return s[0]

# most frequent number in a list
def most_frequent(list):
  return max(set(list))

# first bit of gamma rate
first_bits = list(map(first, bits))
print(most_frequent(first_bits))

dataFile.close()

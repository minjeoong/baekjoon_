
i = int(input())
line = 0
max = 0

while i > max :
  line += 1
  max += line

gap = max - i
if line % 2 == 0:
  top = line - gap
  bott = gap + 1
else:
  top = gap + 1
  bott = line - gap

print(top, '/', bott, sep="")

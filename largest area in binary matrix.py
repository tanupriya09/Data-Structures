a = [[0, 0, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 0, 0]]
for row in range(1, len(a)):
    for column in range(len(a[0])):
        if a[row][column] == 1:
            a[row][column] = a[row][column] + a[row - 1][column]
largest = 0
for row in a:
    i = 0
    max_area = 0
    stack = []
    while i < len(row):
        if len(stack) == 0:
            stack.append(i)
            i += 1
        elif len(stack) != 0 and row[stack[-1]] <= row[i]:
            stack.append(i)
            i += 1
        elif row[stack[-1]] > row[i]:
            highest_value = row[stack.pop()]
            if len(stack) != 0:
                area = highest_value * (i - stack[-1] - 1)
            else:
                area = highest_value * (i)
            max_area = max(area, max_area)
    while len(stack) != 0:
        highest_value = row[stack.pop()]
        if len(stack) != 0:
            area = highest_value * (i - stack[-1] - 1)
        else:
            area = highest_value * (i)
        max_area = max(area, max_area)
    if max_area>largest:
        largest = max_area
print(largest)




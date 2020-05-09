grocery = ["mug", "fan", "tea", "rice", "pen", "5"]
print(grocery[4])
numbers = [1, 3, 7, 5, 9]
print(numbers[2])
numbers.sort()
numbers.reverse()
print(numbers)
print(numbers[1:4])
print(max(numbers))
print(min(numbers))
numbers.append(4)
print(numbers)
numbers = []
numbers.append(54)
numbers.append(64)
numbers.append(74)
print(numbers)
numbers.insert(3, 40)
print(numbers)
#numbers.remove(64)
#print(numbers)
#numbers.pop()
#print(numbers)
numbers[1] = 30
print(numbers)
# Mutable = can change
# Immutable = cannot change
tp = (1, 2, 3)
print(tp)
a = 5
b = 10
temp = a
a = b
b = temp
print(a,b)
a = 4
b = 8
a,b = b,a
print(a,b)

C = "Hello, my name is Hiep and these are my sheep sizes"
sizes = [5, 7, 300, 90, 24, 50, 75]
# print(C, sizes)
#
# print("Now my biggest sheep has size", max(sizes), "let's shear it")
#
# print("After shearing here is my flock")
# sizes.remove(300)
# print(sizes)
#
# print("One month has passed, now here is my flock")
# new_sizes = [x + 50 for x in sizes]
# print(new_sizes)

print("Month 1:")
print("One month has passed, now here is my flock:")
new_sizes_month1 = [x + 50 for x in sizes]
print(new_sizes_month1)
print("Now my biggest sheep has size", max(new_sizes_month1), "let's shear it")
print("After shearing, here is my flock")
new_sizes_month1[3 - 1] = 8
print(new_sizes_month1)

print("Month 2:")
print("One month has passed, now here is my flock:")
new_sizes_month2 = [x + 50 for x in new_sizes_month1]
print(new_sizes_month2)
print("Now my biggest sheep has size", max(new_sizes_month2), "let's shear it")
print("After shearing, here is my flock")
new_sizes_month2[4 - 1] = 8
print(new_sizes_month2)

print("Month 3:")
print("One month has passed, now here is my flock:")
new_sizes_month3 = [x + 50 for x in new_sizes_month2]
print(new_sizes_month3)
print("Now my biggest sheep has size", max(new_sizes_month3), "let's shear it")
print("After shearing, here is my flock")
new_sizes_month3[7 - 1] = 8
print(new_sizes_month3)

print("Month 4:")
print("One month has passed, now here is my flock:")
new_sizes_month4 = [x + 50 for x in new_sizes_month3]
print(new_sizes_month4)
print("Now my biggest sheep has size", max(new_sizes_month4), "let's shear it")
print("After shearing, here is my flock")
new_sizes_month4[6 - 1] = 8
print(new_sizes_month4)

total_size = sum(new_sizes_month4)
print("My flock has size in total:", total_size)
print("I would get", total_size * 2, "$")

import numpy as np

print("=====================================")
print("=====Number statictics Analyzer ======")
print("=====================================")

numbers = np.random.randint(1,101,20)

print("\nNumbers :")
print(numbers)

print("\n=========== STATISTICS ===========")

print("Sum               :",np.sum(numbers))
print("Mean              :",np.mean(numbers))
print("Meadian           :",np.median(numbers))
print("Minimum           :",np.min(numbers))
print("Maximum           :",np.max(numbers))
print("Variance          :",np.var(numbers))
print("Standard Division :",np.std(numbers))

print("\n Sorted Array")
print(np.sort(numbers))

even_numbers = numbers[numbers % 2 == 0 ]
odd_numbers = numbers[numbers % 2  != 0]

print("\n Even numbers :")
print(even_numbers)

print("\n Odd numbers :")
print(odd_numbers)

print("\nNumbers of even numbers :",len(even_numbers))
print("Numbers of odd numbers :",len(odd_numbers))

avearage = np.mean(numbers)
above_avg = numbers[numbers > avearage]

print("\n Average :",avearage)

print("\n Above average :")
print(above_avg)



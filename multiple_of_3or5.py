# List of numbers from 1 to 1000
numbers = list(range(1,1000))
# List with numbers to calculate multiples
div = [3,5]
# Calculate sum of multiples and
# convert the list to set to get unique values and calculate the sum
sum_multiples = sum(set([n for m in div for n in numbers if n%m == 0]))
print('The sum of all the multiples of 3 or 5 below 1000 is {}'.format(sum_multiples))



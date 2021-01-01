# Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):
    for i in range(len(nums)-2):
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
            return True
    return False

# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))

# Write a function that returns the number of prime numbers that exist up to and including a given number
# 0 and 1 are not primes

def count_primes(num):
    counter = 0 
    for number in range(0, num):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                counter = counter + 1
    return f'Total number of prime numbers between 0 and {num}: {counter}'
print(count_primes(10))
print(count_primes(50))
print(count_primes(100))

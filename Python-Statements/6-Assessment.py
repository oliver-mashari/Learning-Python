# Use for, .split(), and if to create a Statement that will print out words that start with 's'
st = 'Print only the words that start with s in this sentence'
# Answer
for word in st.split():
    if word[0] == 's' or word[0] == 'S':
        print(word)
    else:
        pass

# Use range() to print all the even numbers from 0 to 10.
# Answer
for number in range(0,11,2):
    print(f"Even numbers: {number}")

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
# Answer
my_list = [number for number in range(1,50,1) if number%3==0]
print(my_list)

# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
# Answer
for word in st.split():
    if len(word) % 2 == 0:
        print(f"{word} - even!")

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, 
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"
# Answer
for number in range(1,101,1):
    if number % 3 == 0 and number % 5 == 0 :
        number = "FizzBuzz"
    elif number % 3 == 0:
        number = "Fizz"
    elif number % 5 == 0:
        number = "Buzz"
    print(number)

# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
# Answer
my_list = [letter[0] for letter in st.split()]
print(my_list)





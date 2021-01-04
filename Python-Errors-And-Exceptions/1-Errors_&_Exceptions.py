def add(n1,n2):
    print(n1+n2)

add(10,20)

# number1 = 10
# number2 = input("Please enter a number: ")

"""
# This will result in an error 
add(number1,number2)
# this code won't be executed because of the above error
print(number1)
"""

# try, except, else code 
try:
    # Want to attempt this
    # may have error 
    result = 10 + 10
except:
    # This will execute if the above fails
    print("It looks like you haven't added correctly")
else: 
    print("Add went well")
    print(result)


try:
    file = open('testfile', 'r')
    file.write("Write to file")
except TypeError:
    print("There was a type error")
# except OSError:
#     print("You have an OSError")
except:
    print("All other exceptions")
finally:
    print("I always run")


# try, except and finally in a function
"""
def ask_for_int():
    try:
        result = int(input("Please provide a number: "))
    except:
        print("Woops that is not a number")
    finally:
        print("End of try except finally")

ask_for_int()
"""

# add while loop to above function
def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a number: "))
        except:
            print("Woops that is not a number")
            continue
        else:
            print("Yes thank you")
            break 
        finally:
            print("End of try except finally")

ask_for_int()
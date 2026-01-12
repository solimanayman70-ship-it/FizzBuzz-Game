import random

print("Welcome to FizzBuzz game")
number = int(input("Select a number: "))
print("Yous selection is: ", number)
# for number in range(1, 101):
# human selection
if number %3 ==0 and number %5 == 0:
    print("Your score is: FizzBuzz")
elif number %3 == 0:
    print("Your score is: Fizz")
elif number %5 == 0:
    print("Your score is: Buzz")
else:
    print("No value")

# computed selection
computer_score = random.randint(1,100)
print("Computer selection is: ", computer_score)
if computer_score % 3 == 0 and computer_score % 5 == 0:
    print("computer score is: FizzBuzz")
elif computer_score % 3 == 0:
    print("computer score is: Fizz")
elif computer_score % 5 == 0:
    print("computer score is: Buzz")
else:
    print("No value")

if computer_score == "FizzBuzz" and number == "Fizz" or "Buzz":
    print("Your Lost")
elif number== "Fizz" or "Buzz" and computer_score == "FizzBuzz":
    print("Your Lost")
elif number == "Fizz" and computer_score == "Buzz":
    print("Your win")
elif number and computer_score == "Fizz":
    print("Draw")
elif number and computer_score == "Buzz":
    print("Draw")
else:
    print("no value")
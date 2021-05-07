"""
This project is inspired by TokyoEdTech aka Christian Thompson's video https://www.youtube.com/watch?v=E6K7fc0nP8U
Watch the video if you need more info about what this project is and leave a sub if you can, will ya :)
"""

for i in range(1, 101):

    found = False

    if i % 3 == 0:
        print("Fizz", end="")
        found = True
    
    if i % 5 == 0:
        print("Buzz", end="")
        found = True

    if not found:
        print(i, end="")

    print()
        

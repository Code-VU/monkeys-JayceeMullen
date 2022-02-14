def calculateTime():
    
    # This first line is provided for you

    boolDict = {
        "y":True,
        "n":False
    }
    monkey_one = boolDict[input("Is the first monkey smiling?:  ")]
    monkey_two = boolDict[input("Is the second monkey smiling?: ")]

    isGoodDay = monkey_one ^ monkey_two

    if isGoodDay:
        print("Yay! We're going to have a good day!")
    else:
        print("Uh Oh! We're in trouble!")

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateTime() and run > python monkeyCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
if __name__ == "__main__":
    calculateTime()
task = input("What homework do you have? ")

if "math" in task.lower():
    print("Open your math book")
    print("Solve the given problems")
    print("Check your answers")

elif "english" in task.lower():
    print("Read the lesson")
    print("Write the answers")
    print("Check spelling and grammar")

elif "science" in task.lower():
    print("Read the topic")
    print("Draw diagrams if needed")
    print("Revise key points")

else:
    print("Start by reading the question carefully")
    print("Break the homework into small steps")
    print("Complete one step at a time")
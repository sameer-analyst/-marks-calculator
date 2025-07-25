import sys
if len(sys.argv) < 3:
    print("Please enter the arguments otherwise i will exit this program")
    sys.exit()

print("Arguments received:", sys.argv)
name = sys.argv[1]
marks = sys.argv[2:]
print(type(marks))
marks = [int(m) for m in marks]
print(marks)
total = sum(marks)
average = total / len(marks)
percentage = average
print(f"Hello {name}, your total marks {total} average is {average:.2f} and percentage is {percentage:.2f}%")
input("Press Enter to exit.----")
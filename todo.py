import os
import sys


def TodoAdd(task):
    with open("todo.txt", 'w+') as todoFile:
        try:
            todoFile.write(task)
            print("Added Task : ", task)
        except:
            print("An Error Occured")
        

if len(sys.argv) > 3:
    print("You have specified too many arguments")
    exit()

arg = sys.argv[1]
task = ""
if arg=="add":
    try:
        task = sys.argv[2]
    except:
        print("You didn't specified task")
        exit()


if(arg=="add"):
    TodoAdd(task)
# elif (arg =="ls"):
#     ReadFile("todo.txt")
# elif (arg=="help" or arg is None):
#     ReadFile("help.txt")
# elif (arg == "report"):
#     Report()
# elif (arg=="done"):
#     MarkTodo()

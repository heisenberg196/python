import os
import sys


def TodoAdd(task):
    with open("todo.txt", 'a+') as todoFile:
        try:
            todoFile.write(task+'\r')
            print("Added Task : ", task)
        except:
            print("An Error Occured")
        
def ReadFile(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        Length = len(lines)
        for idx, line in enumerate(reversed(lines)):
            print('[{0}] : {1}'.format(Length-idx, line), end='')


if len(sys.argv) > 3:
    print("You have specified too many arguments")
    exit()
arg = sys.argv[1]

if(arg=="add"):
    task = ""
    try:
        task = sys.argv[2]
    except:
        print("You didn't specified task")
        exit()
    TodoAdd(task)
elif (arg =="ls"):
    ReadFile("todo.txt")
# elif (arg=="help" or arg is None):
#     ReadFile("help.txt")
# elif (arg == "report"):
#     Report()
# elif (arg=="done"):
#     MarkTodo()

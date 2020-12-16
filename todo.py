import os
import sys


def TodoAdd(task):
    with open("todo.txt", 'a+') as todoFile:
        try:
            todoFile.write(task+'\r')
            print("Added Task : ", task)
        except:
            print("An Error Occured")
        
def ReadTodo():
    with open("todo.txt", 'r') as f:
        lines = f.readlines()
        Length = len(lines)
        for idx, line in enumerate(reversed(lines)):
            print('[{0}] : {1}'.format(Length-idx, line), end='')

def ReadHelp():
    with open("help.txt", 'r') as h:
        for line in h:
            print(line, end='')

def DelTask(num):
        num = int(num)
        with open("todo.txt", 'r') as f:
            lines = f.readlines()
            print("lines before deleting ", lines)
            Length = len(lines)
            try:
                TaskToDel = lines[num-1]
                lines.remove(TaskToDel)
                print("lines after deleting ", lines)

                print('[{0}] {1} deleted'.format(num, TaskToDel))
                with open("todo.txt", 'a+') as todoFile:
                    todoFile.truncate(0)
                    for task in lines:
                        try:
                            todoFile.write(task)
                        except:
                            print("An Error Occured")
                return TaskToDel
            except:
                print("Task Don't exist")




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
    ReadTodo()
elif (arg=="help" or arg is None):
    ReadHelp()
elif (arg=="del"):
    try:
        taskNum = sys.argv[2]
    except:
        print("You didn't specified task number to delete")
        exit()
    DelTask(taskNum)
# elif (arg == "report"):
#     Report()
# elif (arg=="done"):
#     MarkTodo()

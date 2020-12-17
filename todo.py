import sys
from datetime import date

def TodoAdd(task):
    with open("todo.txt", 'a+') as todoFile:
        try:
            todoFile.write(task+'\r')
            print('Added todo: "{0}"'.format(task), end=' ')
        except:
            print("An Error Occured")
        
def ReadTodo():

    try:
        with open("todo.txt", 'r') as f:
            lines = f.readlines()
            Length = len(lines)
            # if Length==0:
                
            for idx, line in enumerate(reversed(lines)):
                print('[{0}] {1}'.format(Length-idx, line), end='')
    except:
        print("There are no pending todos!")
        exit()

def ReadHelp():
    with open("help.txt", 'r') as h:
        for line in h:
            print(line, end='')


def DelTask(num):
    num = int(num)
    lines=[]

    with open("todo.txt", 'r') as f:
        lines = f.readlines()
        Length = len(lines)
        if Length<num or num<=0:
            print("Error: todo #{0} does not exist. Nothing deleted.".format(num))
            exit()
        TaskToDel = lines[num-1]
        lines.remove(TaskToDel)
        print('Deleted todo #{0}'.format(num))

    with open("todo.txt", 'a') as f:
        f.truncate(0)
        for task in lines:
            try:
                f.write(task)
            except:
                print("An Error Occured")
        
        

def MarkTodo(num):
    num = int(num)
    TaskDone = ""
    with open("todo.txt", 'r') as f:
        lines = f.readlines()
        Length = len(lines)
        if Length<num or num<=0:
            print("Error: todo #{0} does not exist.".format(num))
            exit()
        TaskDone = lines[num-1]
        lines.remove(TaskDone)
        print('Marked todo #{0} as done.'.format(num))

    with open("todo.txt", 'a') as f:
        f.truncate(0)
        for task in lines:
            try:
                f.write(task)
            except:
                print("An Error Occured")       
                exit()

    with open("done.txt", 'a+') as DoneFIle:
        try:
            DoneFIle.write(TaskDone)
        except:
            print("An Error Occured")

def Report():
    TodoLen=0
    DoneLen=0
    with open("todo.txt", 'r') as f:
        lines = f.readlines()
        TodoLen = len(lines)
    with open("done.txt", 'r') as f:
        lines = f.readlines()
        DoneLen = len(lines)
    print("{0} Pending : {1} Completed : {2}".format(date.today().strftime("%Y-%m-%d"), TodoLen, DoneLen))


if len(sys.argv) > 3:
    print("You have specified too many arguments")
    exit()

arg = ""
try:
    arg=sys.argv[1]
except:
    ReadHelp()

if (arg=="add"):
    task = ""
    try:
        task = sys.argv[2]
    except:
        print("Error: Missing todo string. Nothing added!")
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
        print("Error: Missing NUMBER for deleting todo.")
        exit()
    DelTask(taskNum)

elif (arg=="done"):
    try:
        taskNum = sys.argv[2]
    except:
        print("Error: Missing NUMBER for marking todo as done.")
        exit()
    MarkTodo(taskNum)

elif (arg=="report"):
    Report()
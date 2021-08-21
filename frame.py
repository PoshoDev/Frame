import os, math
from colorama import Fore, Back, Style

size = 48

def DrawTable():
    return

def DrawBorder():
    str = ""
    for i in range(size-2):
        str += "─"
    print("┼"+str+"┼")

def DrawBorderTop():
    str = ""
    for i in range(size-2):
        str += "═"
    print('╔'+str+'╗')

def DrawBorderMid(string):
    str = StringFit(string, size-4)
    print("║ "+str+" ║")

def DrawBorderBot():
    str = ""
    for i in range(size-2):
        str += "═"
    print('╚'+str+'╝')

def DrawInner(string):
    str = StringFit(string, size-4)
    print("│ "+str+" │")

def DrawIndex(i, string):
    str1 = StringFit(str(i), 2)
    str2 = StringFit(string, size-9)
    print("│ "+str1+" │ "+str2+" │")

def DrawIndexBorder():
    str = ""
    for i in range(size-7):
        str += "─"
    print("┼────┼"+str+"┼")

def DrawFrame(string):
    DrawBorderTop()
    DrawBorderMid(string)
    DrawBorderBot()

def DrawTop(string):
    DrawBorder()
    DrawInner(string)

def DrawBottom(string):
    DrawInner(string)
    DrawBorder()

def DrawHeader(string):
    ConsoleClear()
    DrawFrame(string)

def DrawError(string):
    DrawHeader("/!\\ "+ string)

def DrawWarning(string):
    DrawInner("/!\\ "+ string)

def Input():
    return input("│ <<< ")

def Wait():
    input("Press RETURN to continue...")
    ConsoleClear()

# Fits a string in a given range.
def StringFit(string, size):
    #print(string+" ST: "+str(len(string)))
    if len(string) > size:
        return string[:size-3] + "..."
    else:
        total = size - len(string)
        for i in range(total):
            string += " "
        return string

# Color formats a given string with background and contrasting text.
def StringColorBG(string):
    return Back.RED + string + Style.RESET_ALL

# Clears the console's text.
def ConsoleClear():
	clear = lambda: os.system('cls')
	clear()

# Changes the width and height of the console.
def ConsoleSizeSet(width, height):
    cmd = "mode "+str(width)+","+str(height)
    os.system(cmd)

def DrawProgress(current, maximum):
    barsize = size - 15

    # Border
    string = ""
    for i in range(barsize+2):
        string += "─"
    print("┌"+string+"┬─────────┐")

    # Inner
    if (current < maximum):
        prog = math.floor(current / maximum * barsize)
    else:
        prog = barsize

    bar = ""
    for i in range(prog):
        bar += "█"
    back = ""
    for i in range(barsize-prog):
        back += "░"

    perc = math.floor(current / maximum * 100)
    perc = f'{perc:03}'

    print("│ "+bar+back+" │  "+perc+" %  │")

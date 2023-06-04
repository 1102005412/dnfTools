#####################################################
#    DNF 迷你大乱斗站 x 脚本，只能站 x 
#  安装依赖：
#    pip install pyautogui
#    pip install pywin32
#  注意: 脚本运行需要管理员权限，否则按键对游戏无效。建议
#            先以管理员方式打开cmd.exe，然后以“python 本文件名”
#       的命令启动本脚本。 
#####################################################

import pyautogui
import time
import win32api
import win32con
from tkinter import *

root = Tk()
clickedx = 2354
clickedy = 855

def attack():
    count = 50
    while count > 0:
        win32api.keybd_event(0x58,0,0,0)
        time.sleep(0.1)
        win32api.keybd_event(0x58,0,win32con.KEYEVENTF_KEYUP,0)
        time.sleep(0.1)
        count -= 1

def start_work():
    while(True):
        print("click position is (%d,%d)" % (clickedx,clickedy))
        pyautogui.moveTo(clickedx,clickedy)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        time.sleep(0.1)
        
        attack()

        pyautogui.hotkey('altleft','tab')
        time.sleep(0.1)
        pyautogui.hotkey('altleft','tab')
        time.sleep(0.1)

def left_click(e):
    print("leiang debug:left clicked!")
    global clickedx,clickedy
    clickedx,clickedy = pyautogui.position()
    print("click position is (%d,%d)" % (clickedx,clickedy))
    root.destroy()

def init_window():
    width,height = pyautogui.size()
    print("screem size is %d x %d" % (width,height))
    geo = str(width) + 'x' + str(height) + '+0+0'
    root.geometry(geo)
    root.attributes('-alpha',0.1)
    text = '请点击游戏界面中的”开始匹配“！'
    btn = Button(root,text = text,
        width = width,height = height,
        fg = "red",
        font = ('楷体',50,'bold'))
    btn.place(x=0, y=0)
    btn.pack()
    btn.bind('<Button-1>',left_click)
    root.mainloop()

if __name__ == '__main__':
    init_window()
    start_work()
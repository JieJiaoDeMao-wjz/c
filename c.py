import os
import time
import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

#
sys_err_buf=""
for i in os.listdir("C:\\Windows\\System32\\"):
    sys_err_buf+=("找不到C:\\Windows\\System32\\"+i+"。\n")
#
def on_closing():
    showerror(message="Windows找不到dwm.exe。请从安装程序驱动介质中拷贝或还原该程序。",title="")
def _b():
    root = Tk()
    root.overrideredirect(True)
    root.state('zoomed')
    root.attributes("-topmost", 1)
    root.protocol('WM_DELETE_WINDOW', on_closing)
    lb=Label(root)
    lb.pack()
    lb["text"]=sys_err_buf
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
            _dl.append(os.path.join(a,i))
    return(dl)

#
def _f():
    _fw=Tk()
    _fw.protocol('WM_DELETE_WINDOW', on_closing)
    _fw.attributes("-topmost", 1)
    __dl=_d()
    _l=Label(_fw)
    _l.pack()
    _l["text"]="Windows正在格式化 本地磁盘（C:\\） 。\n此主机上的条件不支持快速格式化，因此将逐个粉碎文件。"
    _t=Text(_fw)
    font1 = font.Font(family='微软雅黑')
    _t.config(font=font1)
    _p=Progressbar(_fw)
    _p.pack()
    _p["max"]=len(__dl)
    _p["value"]=0
    _i=0
    for i in __dl:
        _i+=1
        _t.insert(END,"删除文件 - "+i+"\n")
        _p["value"]=_i
    _fw.mainloop()
    
    
#
if __name__=="__main__":
    _fwtdr=Tk()
    _fwtdr.withdraw()
    showerror(message="Windows预体验版本出现严重问题，需要立即格式化一切本地磁盘以保护您的计算机免受进一步伤害。\n当前已进入安全保护模式，无法读取任何外接驱动器。若要备份您的重要用户数据（仅限256MB以内），请在下一个窗口选择“是”。\n单击“确定”以开始计算机保护进程。",title="Windows严重错误警告")
    if askquestion(message="是否将此计算机上的用户数据备份到Windows云端？\n警告：备份空间只有256MB，Windows将自动上传大小最大的文件。其余文件已被冻结，请勿使用。",title="用户数据保护提示")==True:
        _x()
    else:
        pass
    showwarning(message="计算机保护程序即将启动。请关闭其他正在运行的程序，以防止数据进一步损坏。",title="")
    _f()
    showinfo(title="",message="格式化完毕。\n请不要操作计算机，否则系统将会被挂起。\n\n系统状态代码：NTSTATUS 0xC0000001\n若要获取有关计算机系统重新安装的方法，请访问https://windows.com/stopcode/，并搜索此状态代码。")
    _b()
           
    


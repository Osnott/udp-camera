import tkinter as tk
import tkinter.ttk as ttk

serverData = {}
ready = False
exited = False
m = tk.Tk()
m.title('UDP Client')
ip = ttk.Label(m, background="#282f38", foreground="#eaeaea", text='IP').grid(row=0)
port = ttk.Label(m, text='Port', background="#282f38", foreground="#eaeaea").grid(row=1)
e1 = tk.Entry(m, background="#474c56", foreground="#eaeaea")
e2 = tk.Entry(m, background="#474c56", foreground="#eaeaea")
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e1.insert(0, '192.168.1.7')
e2.insert(0, '9999')
var1 = tk.IntVar()
checkbox = tk.Checkbutton(m, background="#282f38", foreground="#a8acb5", text='Debug', variable=var1).grid(row=2, column=1)


def startServer():
    global serverData, e1, e2, var1, ready, m
    serverData = {
        'ip': e1.get(),
        'port': int(e2.get()),
        'debug': var1.get() == 1
    }
    ready = True
    m.destroy()


def exit_me():
    global exited, m
    exited = True
    m.destroy()


startButton = tk.Button(m, background="#474c56", foreground="#eaeaea", text='Start Server', width=25, command=startServer).grid(row=3, column=1)
exitButton = tk.Button(m, background="#474c56", foreground="#eaeaea", text='Exit', width=25, command=exit_me).grid(row=3, column=0)

m.configure(bg='#282f38')

m.mainloop()

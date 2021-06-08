
import subprocess
from tkinter import *

class Apache_services():
    def __init__(self,window,dimensions='500x500'):
        self.window = Tk()
        self.dimensions = dimensions 

    def Apache_root_services(self):
        self.window.title('@Apache KronOS ~zackonit')
        self.window.geometry(self.dimensions) 
        self.window.resizable(0,0) 
        self.fonty = ("Verdana",24) 

        self.INSERT = Label(text="Apache Service 127.0.0.1",
        fg="yellow" ,bg="black",font=self.fonty).pack()

        self.window.configure(background='black')
        '''Recovery buttons'''
        self.service = Label(self.window,text="Open Linux local server",
                             fg='red', bg="black").place(x=25,y=65)

        self.info = Button(self.window,text="Open",bg="green",fg="white",command=self.openLinux_service).place(x=228,y=55)
        self.down = Button(self.window,text="Down" ,bg="red" ,fg="white",command=self.downLinux_service).place(x=328,y=55)

        self.footer =  Label(self.window, text='Development @zackonit',bg="yellow" ,fg="black",width=65, height=3).place(x=1,y=440)

    def openLinux_service(self,unlock='sudo /opt/lampp/lampp start',fail='sudo /etc/init.d/apache2 stop'):
        self.main = subprocess.check_output(fail,subprocess.STDOUT,shell=True) 
        self.opt_command = subprocess.check_output(unlock,subprocess.STDOUT,shell=True)
        self.output = Label(text=self.opt_command,fg="blue" ,bg="black",width="50").place(x=15,y=125) 

        #Fernando Zacatenco ~zackonit :)) 
        
    def downLinux_service(self,down_track='sudo /opt/lampp/lampp stop'):
        self.stoplinux = subprocess.check_output(down_track ,subprocess.STDOUT,shell=True)
        self.out = Label(text=self.stoplinux,fg="violet",bg="black",width="50").place(x=5,y=123)

        self.config = subprocess.check_output('figlet ImHackerEnterMyW0rld',subprocess.STDOUT,shell=True)
        self.ifconfig = Label(text=self.config ,fg="white" ,bg="black").place(x=5,y=210)
        

if __name__ == "__main__":
    apache_services = Apache_services(None)
    apache_services.Apache_root_services()

    apache_services.openLinux_service()
    apache_services.downLinux_service()

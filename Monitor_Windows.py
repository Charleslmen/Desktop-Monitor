# -*- coding=utf-8 -*-

import paramiko
import os
import json
import pandas as pd
import threading
import time

class ComputerWin(object):
    def __init__(self,port,IP,username,password,local_path,
                    remote_path,name,local_name,remote_name):
        self.port=port
        self.IP=IP
        self.username=username
        self.password=password
        self.local_path=local_path
        self.remote_path=remote_path
        self.name=name
        self.local_name=local_name
        self.remote_name=remote_name


    def printInfoWin(self):
        width=40
        try:
            transport = paramiko.Transport((self.IP,22))
            transport.connect(username=self.username,password=self.password)
            sftp = paramiko.SFTPClient.from_transport(transport)

            sftp.put(self.local_name,self.remote_name)

            transport.close()

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.IP,self.port,self.username, self.password)

            cmd = '{0}python.exe {1}'.format(self.remote_path,self.remote_name)
            stdin, stdout, stderr = ssh.exec_command(cmd)

            line_list = stdout.readlines()

            ssh.close()

            data = json.loads(line_list[0])
            result_df = pd.Series(data).to_frame('Monitoring Information')
            print (result_df)
            print("-"*width)

        except Exception as e:
            print("  "+self.username.title()+" is not running on Windows!")
            print("-"*width)

class ComputerLinux(object):
    def __init__(self,port,IP,username,password,local_path,
                    remote_path,name,local_name,remote_name):
        self.port=port
        self.IP=IP
        self.username=username
        self.password=password
        self.local_path=local_path
        self.remote_path=remote_path
        self.name=name
        self.local_name=local_name
        self.remote_name=remote_name

    def printInfoLinux(self):
        width=40
        try:
            transport = paramiko.Transport((self.IP,22))
            transport.connect(username=self.username,password=self.password)
            sftp = paramiko.SFTPClient.from_transport(transport)

            sftp.put(self.local_name,self.remote_name)

            transport.close()

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.IP,self.port,self.username, self.password)
            cmd = 'python {0}{1}'.format(self.remote_path,self.name)
            stdin, stdout, stderr = ssh.exec_command(cmd)

            line_list = stdout.readlines()

            ssh.close()

            data = json.loads(line_list[0])
            result_df = pd.Series(data).to_frame('Monitoring Information')
            print (result_df)
            print("-"*width)

        except Exception as e:
            print("  "+self.username.title()+" is not running on linux!")
            print("-"*width)

"""
Create computers here
"""
Limo=ComputerWin(22,"192.168.1.143","limo","liokmengb7m2",os.getcwd(),
                "C:/Users/limo/Miniconda3/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Users/limo/Miniconda3/", "monitor.txt"))

def Info():
    os.system('cls')
    print (time.strftime('%Y-%m-%d %X',time.localtime()))

    threading.Thread(target=Limo.printInfoWin).start()
    t=threading.Timer(120.0,Info)
    t.start()
if __name__=="__main__":
    Info()

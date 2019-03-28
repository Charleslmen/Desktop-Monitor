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
Tessa=ComputerWin(22,"192.168.1.121","Tessa","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))
Abigail=ComputerWin(22,"192.168.1.124","Abigail","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))
Bailey=ComputerWin(22,"192.168.1.125","Bailey","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))
Charisma=ComputerWin(22,"192.168.1.126","Charisma","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))
Dreama=ComputerWin(22,"192.168.1.127","Dreama","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))
Fleta=ComputerWin(22,"192.168.1.128","Fleta","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))
Goofy=ComputerWin(22,"192.168.1.129","Goofy","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

# Vicki=ComputerWin(22,"192.168.1.123","Vicki","astros",os.getcwd(),
#                 "C:/Python27/","monitor.txt",
#                 os.path.join(os.getcwd(), "monitor.txt"),
#                 os.path.join("C:/Python27/", "monitor.txt"))

# Rose=ComputerWin(22,"192.168.1.120","Rose","astros",os.getcwd(),
#                 "C:/Python27/","monitor.txt",
#                 os.path.join(os.getcwd(), "monitor.txt"),
#                 os.path.join("C:/Python27/", "monitor.txt"))

NeoLinux=ComputerLinux(22,"192.168.1.113","neo","astros",os.getcwd(),
                    "/home/neo/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/neo/","monitor.py"))
NeoWindows=ComputerWin(22,"192.168.1.113","Neo","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

MaiaLinux=ComputerLinux(22,"192.168.1.112","maia","astros",os.getcwd(),
                    "/home/maia/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/maia/","monitor.py"))
MaiaWindows=ComputerWin(22,"192.168.1.112","Maia","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

LeelooLinux=ComputerLinux(22,"192.168.1.111","leeloo","astros",os.getcwd(),
                    "/home/leeloo/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/leeloo/","monitor.py"))
LeelooWindows=ComputerWin(22,"192.168.1.111","Leeloo","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

HerculesLinux=ComputerLinux(22,"192.168.1.130","hercules","astros",os.getcwd(),
                    "/home/hercules/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/hercules/","monitor.py"))
HerculesWindows=ComputerWin(22,"192.168.1.218","Hercules","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

BigDaddyLinux=ComputerLinux(22,"192.168.1.131","big-daddy","astros",os.getcwd(),
                    "/home/big-daddy/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/big-daddy/","monitor.py"))
BigDaddyWindows=ComputerWin(22,"192.168.1.131","Big-Daddy","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

# R2D2Linux=ComputerLinux(22,"192.168.1.132","r2d2","astros",os.getcwd(),
#                     "/home/r2d2/","monitor.py",
#                     os.path.join(os.getcwd(), "monitor.py"),
#                     os.path.join("/home/r2d2/","monitor.py"))
# R2D2Windows=ComputerWin(22,"192.168.1.132","R2D2","astros",os.getcwd(),
#                 "C:/Python27/","monitor.txt",
#                 os.path.join(os.getcwd(), "monitor.txt"),
#                 os.path.join("C:/Python27/", "monitor.txt"))

# C3POLinux=ComputerLinux(22,"192.168.1.133","c3po","astros",os.getcwd(),
#                     "/home/c3po/","monitor.py",
#                     os.path.join(os.getcwd(), "monitor.py"),
#                     os.path.join("/home/c3po/","monitor.py"))
# C3POWindows=ComputerWin(22,"192.168.1.133","C3PO","astros",os.getcwd(),
#                 "C:/Python27/","monitor.txt",
#                 os.path.join(os.getcwd(), "monitor.txt"),
#                 os.path.join("C:/Python27/", "monitor.txt"))

# Jordan7Linux=ComputerLinux(22,"192.168.1.141","jordan7","astros",os.getcwd(),
#                     "/home/jordan7/","monitor.py",
#                     os.path.join(os.getcwd(), "monitor.py"),
#                     os.path.join("/home/jordan7/","monitor.py"))
# Jordan7Windows=ComputerWin(22,"192.168.1.141","Jordan7","astros",os.getcwd(),
#                 "C:/Python27/","monitor.txt",
#                 os.path.join(os.getcwd(), "monitor.txt"),
#                 os.path.join("C:/Python27/", "monitor.txt"))
#
# DobbyLinux=ComputerLinux(22,"192.168.1.149","dobby","astros",os.getcwd(),
#                     "/home/dobby/","monitor.py",
#                     os.path.join(os.getcwd(), "monitor.py"),
#                     os.path.join("/home/dobby/","monitor.py"))
# DobbyWindows=ComputerWin(22,"192.168.1.149","Dobby","astros",os.getcwd(),
#                 "C:/Python27/","monitor.txt",
#                 os.path.join(os.getcwd(), "monitor.txt"),
#                 os.path.join("C:/Python27/", "monitor.txt"))

FleurLinux=ComputerLinux(22,"192.168.1.150","fleur","astros",os.getcwd(),
                    "/home/fleur/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/fleur/","monitor.py"))
FleurWindows=ComputerWin(22,"192.168.1.150","Fleur","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

IgorLinux=ComputerLinux(22,"192.168.1.151","igor","astros",os.getcwd(),
                    "/home/igor/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/igor/","monitor.py"))
IgorWindows=ComputerWin(22,"192.168.1.151","Igor","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

PotterLinux=ComputerLinux(22,"192.168.1.152","potter","astros",os.getcwd(),
                    "/home/potter/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/potter/","monitor.py"))
PotterWindows=ComputerWin(22,"192.168.1.152","Potter","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

ViktorLinux=ComputerLinux(22,"192.168.1.153","viktor","astros",os.getcwd(),
                    "/home/viktor/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/viktor/","monitor.py"))
ViktorWindows=ComputerWin(22,"192.168.1.153","Viktor","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

HaggridLinux=ComputerLinux(22,"192.168.1.154","haggrid","astros",os.getcwd(),
                    "/home/haggrid/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/haggrid/","monitor.py"))
HaggridWindows=ComputerWin(22,"192.168.1.154","Haggrid","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

AndromedaLinux=ComputerLinux(22,"192.168.1.155","andromeda","astros",os.getcwd(),
                    "/home/andromeda/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/andromeda/","monitor.py"))
AndromedaWindows=ComputerWin(22,"192.168.1.155","Andromeda","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

PegasusLinux=ComputerLinux(22,"192.168.1.156","pegasus","astros",os.getcwd(),
                    "/home/pegasus/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/pegasus/","monitor.py"))
PegasusWindows=ComputerWin(22,"192.168.1.156","Pegasus","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

FrodoLinux=ComputerLinux(22,"192.168.1.160","frodo","astros",os.getcwd(),
                    "/home/frodo/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/frodo/","monitor.py"))
FrodoWindows=ComputerWin(22,"192.168.1.160","Frodo","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

SamLinux=ComputerLinux(22,"192.168.1.161","sam","astros",os.getcwd(),
                    "/home/sam/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/sam/","monitor.py"))
SamWindows=ComputerWin(22,"192.168.1.161","Sam","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

PippinLinux=ComputerLinux(22,"192.168.1.162","pippin","astros",os.getcwd(),
                    "/home/pippin/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/pippin/","monitor.py"))
PippinWindows=ComputerWin(22,"192.168.1.162","Pippin","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

MerryLinux=ComputerLinux(22,"192.168.1.163","merry","astros",os.getcwd(),
                    "/home/merry/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/merry/","monitor.py"))
MerryWindows=ComputerWin(22,"192.168.1.163","Merry","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

LegolasLinux=ComputerLinux(22,"192.168.1.164","legolas","astros",os.getcwd(),
                    "/home/legolas/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/legolas/","monitor.py"))
LegolasWindows=ComputerWin(22,"192.168.1.164","Legolas","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

BilboLinux=ComputerLinux(22,"192.168.1.165","bilbo","astros",os.getcwd(),
                    "/home/bilbo/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/bilbo/","monitor.py"))
BilboWindows=ComputerWin(22,"192.168.1.165","Bilbo","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

GrandalfLinux=ComputerLinux(22,"192.168.1.166","grandalf","astros",os.getcwd(),
                    "/home/grandalf/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/grandalf/","monitor.py"))
GrandalfWindows=ComputerWin(22,"192.168.1.166","Grandalf","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

GimliLinux=ComputerLinux(22,"192.168.1.167","gimli","astros",os.getcwd(),
                    "/home/gimli/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/gimli/","monitor.py"))
GimliWindows=ComputerWin(22,"192.168.1.167","Gimli","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

ArwenLinux=ComputerLinux(22,"192.168.1.168","arwen","astros",os.getcwd(),
                    "/home/arwen/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/arwen/","monitor.py"))
ArwenWindows=ComputerWin(22,"192.168.1.168","Arwen","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

StriderLinux=ComputerLinux(22,"192.168.1.169","strider","astros",os.getcwd(),
                    "/home/strider/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/strider/","monitor.py"))
StriderWindows=ComputerWin(22,"192.168.1.169","Strider","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

SnowLinux=ComputerLinux(22,"192.168.1.170","snow","astros",os.getcwd(),
                    "/home/snow/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/snow/","monitor.py"))
SnowWindows=ComputerWin(22,"192.168.1.170","Snow","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

BronnLinux=ComputerLinux(22,"192.168.1.171","bronn","astros",os.getcwd(),
                    "/home/bronn/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/bronn/","monitor.py"))
BronnWindows=ComputerWin(22,"192.168.1.171","Bronn","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

TheoLinux=ComputerLinux(22,"192.168.1.172","theo","astros",os.getcwd(),
                    "/home/theo/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/theo/","monitor.py"))
TheoWindows=ComputerWin(22,"192.168.1.172","Theo","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

XuxaLinux=ComputerLinux(22,"192.168.1.253","xuxa","astros",os.getcwd(),
                    "/home/xuxa/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/xuxa/","monitor.py"))
XuxaWindows=ComputerWin(22,"192.168.1.253","Xuxa","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))

YolandaLinux=ComputerLinux(22,"192.168.1.254","yolanda","astros",os.getcwd(),
                    "/home/yolanda/","monitor.py",
                    os.path.join(os.getcwd(), "monitor.py"),
                    os.path.join("/home/yolanda/","monitor.py"))
YolandaWindows=ComputerWin(22,"192.168.1.254","Yolanda","astros",os.getcwd(),
                "C:/Python27/","monitor.txt",
                os.path.join(os.getcwd(), "monitor.txt"),
                os.path.join("C:/Python27/", "monitor.txt"))




def Info():
    os.system('clear')
    print (time.strftime('%Y-%m-%d %X',time.localtime()))

    threading.Thread(target=Abigail.printInfoWin).start()

    threading.Thread(target=Tessa.printInfoWin).start()

    threading.Thread(target=Bailey.printInfoWin).start()

    threading.Thread(target=Charisma.printInfoWin).start()

    threading.Thread(target=Dreama.printInfoWin).start()

    threading.Thread(target=Fleta.printInfoWin).start()

    threading.Thread(target=Goofy.printInfoWin).start()

    # threading.Thread(target=Vicki.printInfoWin).start()

    # threading.Thread(target=Rose.printInfoWin).start()

    threading.Thread(target=LeelooLinux.printInfoLinux).start()
    threading.Thread(target=LeelooWindows.printInfoWin).start()

    threading.Thread(target=MaiaLinux.printInfoLinux).start()
    threading.Thread(target=MaiaWindows.printInfoWin).start()

    threading.Thread(target=NeoLinux.printInfoLinux).start()
    threading.Thread(target=NeoWindows.printInfoWin).start()

    threading.Thread(target=HerculesLinux.printInfoLinux).start()
    threading.Thread(target=HerculesWindows.printInfoWin).start()

    threading.Thread(target=BigDaddyLinux.printInfoLinux).start()
    threading.Thread(target=BigDaddyWindows.printInfoWin).start()

    # threading.Thread(target=R2D2Linux.printInfoLinux).start()
    # threading.Thread(target=R2D2Windows.printInfoWin).start()

    # threading.Thread(target=C3POLinux.printInfoLinux).start()
    # threading.Thread(target=C3POWindows.printInfoWin).start()

    # threading.Thread(target=Jordan7Linux.printInfoLinux).start()
    # threading.Thread(target=Jordan7Windows.printInfoWin).start()

    # threading.Thread(target=DobbyLinux.printInfoLinux).start()
    # threading.Thread(target=DobbyWindows.printInfoWin).start()

    threading.Thread(target=FleurLinux.printInfoLinux).start()
    threading.Thread(target=FleurWindows.printInfoWin).start()

    threading.Thread(target=IgorLinux.printInfoLinux).start()
    threading.Thread(target=IgorWindows.printInfoWin).start()
    #
    # threading.Thread(target=PotterLinux.printInfoLinux).start()
    # threading.Thread(target=PotterWindows.printInfoWin).start()
    #
    threading.Thread(target=ViktorLinux.printInfoLinux).start()
    threading.Thread(target=ViktorWindows.printInfoWin).start()

    threading.Thread(target=HaggridLinux.printInfoLinux).start()
    threading.Thread(target=HaggridWindows.printInfoWin).start()
    #
    # threading.Thread(target=AndromedaLinux.printInfoLinux).start()
    # threading.Thread(target=AndromedaWindows.printInfoWin).start()
    #
    threading.Thread(target=PegasusLinux.printInfoLinux).start()
    # threading.Thread(target=PegasusWindows.printInfoWin).start()
    #
    threading.Thread(target=FrodoLinux.printInfoLinux).start()
    threading.Thread(target=FrodoWindows.printInfoWin).start()
    #
    # threading.Thread(target=SamLinux.printInfoLinux).start()
    # threading.Thread(target=SamWindows.printInfoWin).start()
    #
    threading.Thread(target=PippinLinux.printInfoLinux).start()
    threading.Thread(target=PippinWindows.printInfoWin).start()
    #
    # threading.Thread(target=MerryLinux.printInfoLinux).start()
    # threading.Thread(target=MerryWindows.printInfoWin).start()
    #
    threading.Thread(target=LegolasLinux.printInfoLinux).start()
    # threading.Thread(target=LegolasWindows.printInfoWin).start()
    #
    threading.Thread(target=BilboLinux.printInfoLinux).start()
    threading.Thread(target=BilboWindows.printInfoWin).start()
    #
    # threading.Thread(target=GrandalfLinux.printInfoLinux).start()
    # threading.Thread(target=GrandalfWindows.printInfoWin).start()
    #
    # threading.Thread(target=GimliLinux.printInfoLinux).start()
    # threading.Thread(target=GimliWindows.printInfoWin).start()
    #
    # threading.Thread(target=ArwenLinux.printInfoLinux).start()
    # threading.Thread(target=ArwenWindows.printInfoWin).start()
    #
    # threading.Thread(target=StriderLinux.printInfoLinux).start()
    # threading.Thread(target=StriderWindows.printInfoWin).start()
    #
    threading.Thread(target=SnowLinux.printInfoLinux).start()
    threading.Thread(target=SnowWindows.printInfoWin).start()
    #
    threading.Thread(target=BronnLinux.printInfoLinux).start()
    threading.Thread(target=BronnWindows.printInfoWin).start()
    #
    threading.Thread(target=TheoLinux.printInfoLinux).start()
    threading.Thread(target=TheoWindows.printInfoWin).start()
    #
    threading.Thread(target=XuxaLinux.printInfoLinux).start()
    threading.Thread(target=XuxaWindows.printInfoWin).start()
    #
    threading.Thread(target=YolandaLinux.printInfoLinux).start()
    threading.Thread(target=YolandaWindows.printInfoWin).start()

    t=threading.Timer(120.0,Info)
    t.start()
if __name__=="__main__":
    Info()

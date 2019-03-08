import os

binary_path = '/home/ivanatora/pcd8544_rpi/nokia'

def sendcmd(cmd):
    os.system(binary_path + ' ' + cmd)
    # print(binary_path + ' ' + cmd)


def show_lines(lines):
    sendcmd('r')
    sendcmd('c 60')
    for i in range(len(lines)):
        line_letter = chr(97 + i % 7)
        sendcmd('+' + line_letter + ' "' + lines[i] + '"')
    sendcmd('s')

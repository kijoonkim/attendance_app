import os
import win32com.client


def create_shortcut(target_path, shortcut_path):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = target_path
    shortcut.WorkingDirectory = os.path.dirname(target_path)
    shortcut.save()

# 경로설정
BASE_DIR = os.getcwd()
HOME_DIR = os.path.expanduser('~')
print(f'BASE_DIR = {BASE_DIR}, HOME_DIR = {HOME_DIR}')
path = os.path.join(HOME_DIR+"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup", "attendance_app.lnk")
target = os.path.join(BASE_DIR, "attendance_app.exe")
print(f'path = {path}, target = {target}')

create_shortcut(target, path)
import time 
import pyautogui 
import webbrowser 
import os

from random_word import RandomWords
#funtion for testing os 
print("         Hello to FreeTree.py       ")
print("                                    ")
print("            mayd by zulaa           ")
print("https://github.com/zulaaaaa/freetree")
print("                                    ")
print("                                    ")
print("                                    ")
input("")
print("you need to restart your pc to stop the script ")


input("press any key to start ")
def test1():
    platform = os.name
    if platform == 'posix':
        webbrowser.Mozilla("/usr/lib/firefox-esr/firefox-esr").open("ecosia.org")
        return
    elif platform == 'nt':
        webbrowser.Mozilla("").open("ecosia.org")
        return
      
def randominput():
    print("hear you can define how often the script should run ")
    counter = int(input())
    print("1..")
    time.sleep(1)
    print("2..")
    time.sleep(1)
    print("3.. start")
    a = True
    while a:
        counter = counter - 1 
        r = RandomWords()
        random1 = r.get_random_word()
        pyautogui.write(random1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.moveTo(404, 187)
        pyautogui.click()
        pyautogui.click()
        pyautogui.press("del")
        if counter == 0: 
            a = False
            print("the script has sucseful endet ")
            os._exit(200)            
test1()
time.sleep(1)
randominput()
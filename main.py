import pyautogui, time
time.sleep(5)
text = open("datafile", "r")
for word in text:
    pyautogui.typewrite(word)
    pyautogui.press("enter")

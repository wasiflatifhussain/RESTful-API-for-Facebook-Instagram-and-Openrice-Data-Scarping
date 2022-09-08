import os

os.chdir('C:/LiTRO/Web_Scrap/sns_scrapper/ultimate_scraper/')
os.system('start cmd /k "python3 run.py"')
os.system('start cmd /k "python3 taskqueueFB.py"')
os.system('start cmd /k "python3 taskqueueOPR.py"')
os.system('start cmd /k "python3 taskqueueIG.py"')

#special note- here the command after /k, use the python form you use to run python programs in your system
#              if you used like "py run.py" then change python3 above to py
#              if you used like "python run.py" then change python3 above to python
# print(os.getcwd())
# os.system("start cmd")
# os.system("start cmd")
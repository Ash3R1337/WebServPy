import os
import time

print("Открытие HTTP сервера...")
os.startfile(r'E:/Sublime Text 3/Projects/Web_Serv/flaskr/HTTP_ServerPy.py')
print("Создание сервера ngrok...")
time.sleep(10) #Подождать чтобы HTTP сервер успел запуститься
print("Открывается...")
os.system('/./ngrok http 4567')
print("\nНеобходимо установить ngrok. pip install ngrok или https://ngrok.com")
input()
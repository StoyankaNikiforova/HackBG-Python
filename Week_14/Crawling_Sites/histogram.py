import requests
import re
import matplotlib 


data = requests.get('http://register.start.bg/').text

re_pattern = '(http(s)*:\/\/.[^"]*)(")'

links = re.findall(re_pattern, data)

craw_session = requests.session()
craw_session.keep_alive = False

set_links = {}

for link in links:
    try:
        r = requests.get(link[0])
        h = r.headers['Server']
    except Exception:
        'Hiden server name'
    else:
        if h in set_links:
            set_links[h] += 1
        else:
            set_links[h] = 1
if set_links:
    for k, v in set_links.items():
        print((k, v))
else:
    print("Noooo!")

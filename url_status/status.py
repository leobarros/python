import httpx

urls = ['google.com', 'globo.com', 'picpay.com', 'uol.com.br']


for site in urls:
    r = httpx.get('https://' + site)
    print("{}".format(r.status_code) + '\t' + site)
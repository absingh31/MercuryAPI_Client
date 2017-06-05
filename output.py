import client

def result(key, url):
    initiate_call = client.MercuryAPICall(private_api_key=key)
    smart_article = initiate_call.parse_article(url)

    json_output = smart_article.json()

    return json_output

a=result('zEbEqMY846voNjx8urJPNdDW99amKrRnjbLXkZz0', 'http://www.hackersnewsbulletin.com/2017/06/billboard-hacked-by-neighbourhood.html')

print(a)
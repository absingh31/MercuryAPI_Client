import client
import pprint

def result(key, url):
    initiate_call = client.MercuryAPICall(private_api_key=key)
    smart_article = initiate_call.parse_article(url)

    json_output = smart_article.json()

    return json_output

    '''Can see the example by uncommenting the lines below'''
# a=result('zEbEqMY846voNjx8urJPNdDW99amKrRnjbLXkZz0', 'http://www.hackersnewsbulletin.com/2017/06/billboard-hacked-by-neighbourhood.html')
# print(a)

#Better way to print the result
if __name__=='__main__':
    api_key = input('Enter the api key')
    article_url = input("Enter the article's url")

    response = result(api_key, article_url)
    pprint.pprint(response)

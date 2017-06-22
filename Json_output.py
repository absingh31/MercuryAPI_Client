import client
import pprint
import html_text
def result(key, url):
    initiate_call = client.MercuryAPICall(private_api_key=key)
    smart_article = initiate_call.parse_article(url)

    json_output = smart_article.json()

    return json_output

    '''Can see the example output in json format by uncommenting the lines below'''
#a=result('zEbEqMY846voNjx8urJPNdDW99amKrRnjbLXkZz0', 'http://timesofindia.indiatimes.com/nri/other-news/uk-gets-its-first-female-sikh-mp-in-general-election/articleshow/59064564.cms')
#pprint.pprint(a)

'''Uncomment these 3 lines to get only th text of main content'''
# tree = html_text.parse_html(a['content'])
# text = html_text.extract_text(tree)
# print(text)

#Better way to print the result
if __name__=='__main__':
     api_key = 'zEbEqMY846voNjx8urJPNdDW99amKrRnjbLXkZz0' #input('Enter the api key')
     article_url = input("Enter the article's url")

     response = result('zEbEqMY846voNjx8urJPNdDW99amKrRnjbLXkZz0', article_url)
     pprint.pprint(response)

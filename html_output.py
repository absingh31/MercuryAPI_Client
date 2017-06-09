import Json_output
import webbrowser
import html_text

if __name__=='__main__':
    api_key = input('Enter the private api key')
    url = input('Enter the article url')

    content = Json_output.result(api_key, url)

    f=open("output_html.html", 'w')

    html_open = """<html> """
    f.write(html_open)

    if (len(content['title'])!=0):
        html_heading = """<h1 align="center">%s</h1>"""%(content['title'])
        f.write(html_heading)

    if len(content['author'])!=0:
        html_author = """<h4 align = "right">by %s</h4>"""%((content['author']))
        f.write(html_author)

    if (len(str(content['date_published']))>=9):
        html_date = """<h4 align = "right">%s</h4>""" % ((str(content['date_published']))[:10])
        f.write(html_date)

    if (len(content['content'])!=0):
        tree = html_text.parse_html(content['content'])
        text = html_text.extract_text(tree)
        html_body = """%s"""%(text)
        f.write(html_body)
    html_close = """</html>"""
    f.write(html_close)

    f.close()
    webbrowser.open_new_tab('output_html.html')



import Json_output
import webbrowser

if __name__=='__main__':
    api_key = input('Enter the private api key')
    url = input('Enter the article url')
    content = Json_output.result(api_key, url)

    f=open("output_html.html", 'w')

    html_open = """<html> """
    f.write(html_open)
    html_heading = """<center><h1>%s</h1></center>"""%(content['title'])
    f.write(html_heading)

    html_author = """<h4 align = "right">by %s</h4>"""%((content['author']))
    f.write(html_author)

    html_date = """<h4 align = "right">%s</h4>"""%((str(content['date_published']))[:10])
    f.write(html_date)
    html_body = """%s"""%(content['content'])
    f.write(html_body)
    html_close = """</html>"""
    f.write(html_close)

    f.close()
    webbrowser.open_new_tab('output_html.html')

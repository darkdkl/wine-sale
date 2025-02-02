from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from get_products import get_products
import datetime

if __name__ == "__main__":

    foundation_date = 1920
    now = datetime.datetime.now()
    company_age = now.year-foundation_date

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    with open('./action.txt', 'r', encoding='utf-8-sig') as text_file:

        rendered_page = template.render(
            company_age=company_age, collections=get_products(text_file.read()))

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

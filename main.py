# coding: utf-8
import json
from jinja2 import Environment, FileSystemLoader

def handler(event, context):
    env = Environment(loader=FileSystemLoader( './templates', encoding='utf8'))

    template = env.get_template('index.html')
    html = template.render()
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": html 
    }


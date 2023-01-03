import boto3
import requests
from flask import *

app = Flask(__name__)

AWS_ACCESS_KEY_ID = 'AKIAXKODE5SLSHX7XF5A'
AWS_SECRET_ACCESS_KEY = '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'


@app.route('/request')
def request_url():
    url = request.args.get('url')
    if url:
        return requests.get(url).text

    return 'The parameter <code>url</code> is required.'


@app.route('/')
def home():
    return f'''
<h1>Server Side Request Forgery (SSRF)</h1>
<p>Example Usage: http://{request.host}/request?url=http://169.254.169.254/</p>
'''

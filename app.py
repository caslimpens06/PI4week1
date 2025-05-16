from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html lang="nl">
  <head>
    <meta charset="utf-8">
    <title>Hallo Flask!</title>
    <style>
      body {
        background: linear-gradient(to right, #ffecd2, #fcb69f);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;
        color: #333;
        padding-top: 100px;
      }
      h1 {
        font-size: 3em;
        margin-bottom: 0.2em;
      }
      p {
        font-size: 1.2em;
        color: #555;
      }
      .tijdstip {
        margin-top: 2em;
        font-size: 0.9em;
        color: #777;
      }
    </style>
  </head>
  <body>
    <h1>DevOps! 🌍</h1>
    <p>Dit is een CI/CD test. Dit is de nieuwe versie die gepusht is naar main.</p>
    <div class="tijdstip">Huidige serverdatum en -tijd: {{ tijd }}</div>
  </body>
</html>
"""

@app.route('/')
def hallo():
    huidige_tijd = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return render_template_string(HTML_TEMPLATE, tijd=huidige_tijd)

if __name__ == '__main__':
    app.run(debug=True)

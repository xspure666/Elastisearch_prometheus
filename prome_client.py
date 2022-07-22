from flask import Flask, Response
from prometheus_client import Gauge
import prometheus_client
from elastisearch_alarm import elastic

g = Gauge('elastic_number', 'Total message %d seconds' % 100, ['database', 'index_name'])

app = Flask(__name__)


@app.route('/')
def main():
    return Response("<h1>Hello world</h1>")


@app.route('/metric')
def elastic_message():
    elastic_total, index_name = elastic()
    g.labels(database='ElasticsearchGN', index_name=index_name).set(elastic_total)
    return Response(prometheus_client.generate_latest(g), mimetype="text/plain")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

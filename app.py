from flask import Flask
from opencensus.ext.azure.log_exporter import AzureLogHandler
import logging
import os

app = Flask(__name__)

# Fetch the Application Insights connection string from environment variable
APPLICATIONINSIGHTS_CONNECTION_STRING = os.getenv('APPLICATIONINSIGHTS_CONNECTION_STRING')

if APPLICATIONINSIGHTS_CONNECTION_STRING:
    app.logger.addHandler(AzureLogHandler(connection_string=APPLICATIONINSIGHTS_CONNECTION_STRING))
else:
    app.logger.warning("No Application Insights connection string found in environment variables.")

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def hello():
    app.logger.info("Hello World endpoint was accessed")
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

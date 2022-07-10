import requests
from pymed import PubMed
from datetime import datetime
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

api_id = config['TELEGRAM']['api_id']
api_hash = config['TELEGRAM']['api_hash']
token = config['TELEGRAM']['token']
channel_id=config['TELEGRAM']['channel_id']
phone = config['DEFAULT']['phone']
email = config['TELEGRAM']['email']

def pubmed(query):
    pubmed = PubMed(tool="PubMedScraper", email=email)
    results = pubmed.query(query, max_results=500)
    for i in results:
        keywords = ','.join(i.keywords)
        message = f'*{i.title}*\n_{i.journal}_\n{i.publication_date}\n*Keywords:*{keywords}\n\n*Abstract*\n{i.abstract}\n*[Source: PubMed]*'
        sendMessage(message)
    return results


def sendMessage(message):
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={channel_id}&text={message}&parse_mode=Markdown'
    response = requests.post(url)
    print(response.json())


def main():
    now = datetime.now()
    date_time = now.strftime("%Y/%m/%d")
    pubmed(f'homeopathy[All Fields] AND {date_time}[dp]')


if __name__ == '__main__':
    main()



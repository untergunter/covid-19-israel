if __name__ == '__main__': pass
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json


def scrap_the_site():
    """
    this function is scraping the israel health publication site
    :return:
    """
    target_url = r'https://govextra.gov.il/ministry-of-health/corona/corona-virus/spokesman-messages-corona/'
    source = requests.get(target_url).text
    soup = BeautifulSoup(source, 'lxml')
    all_patients = soup.find_all('div', class_='card')
    return all_patients


def find_headr(patient_publication: str):
    """
    this function is finding the header in order to name the file
    :param patient_publication:
    :return: the name
    """
    for line in patient_publication.text.split('\n'):
        if len(line.strip()) > 3:
            result = line.strip()
            return result


def download_and_save_a_data():
    all_records = scrap_the_site()
    downloaded_dict = {find_headr(message): message.text for message in all_records}
    time_for_file_name = str(datetime.now()).replace('-','_').replace(' ','__').replace(':','_')
    with open(f'{time_for_file_name}.txt', 'w', encoding='utf-8') as outfile:
        json.dump(downloaded_dict, outfile,ensure_ascii=False)


download_and_save_a_data()

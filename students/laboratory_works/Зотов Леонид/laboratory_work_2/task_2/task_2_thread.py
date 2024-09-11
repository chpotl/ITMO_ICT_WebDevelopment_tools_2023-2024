import os
from threading import Thread
import requests
from bs4 import BeautifulSoup
import psycopg2
import time
from db import insert_data
from dotenv import load_dotenv

load_dotenv()

# функция для парсинга и сохранения данных
def parse_and_save(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title').text
    insert_data(url, title)

# главная функция для запуска парсинга в нескольких потоках
def main(urls):
    threads = []
    for url in urls:
        thread = Thread(target=parse_and_save, args=(url,))
        threads.append(thread)
        thread.start()  # запускаем поток

    # ожидаем завершения всех потоков
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    urls = [
        'https://career.habr.com/vacancies?type=all',
        'https://career.habr.com/vacancies?s%5B%5D=2&type=all',
        'https://career.habr.com/vacancies?s%5B%5D=4&type=all',
        'https://career.habr.com/vacancies?s%5B%5D=24&type=all'
    ]

    start_time = time.time()
    main(urls)  # запускаем главную функцию
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tread: {execution_time}")

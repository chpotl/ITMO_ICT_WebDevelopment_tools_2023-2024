import os
from multiprocessing import Pool
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
    insert_data(url, title)  # вставляем данные в БД

# главная функция для запуска парсинга в нескольких процессах
def main(urls):
    num_process = len(urls) if len(urls) < 4 else 4  # количество процессов
    pool = Pool(processes=num_process)
    pool.map(parse_and_save, urls)  # распределяем задачи по процессам

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
    print(f"Multiprocess: {execution_time}")  # выводим время выполнения

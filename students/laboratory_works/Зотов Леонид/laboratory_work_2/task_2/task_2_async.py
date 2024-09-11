import os
import aiohttp
import asyncio
import asyncpg
from bs4 import BeautifulSoup
import time
from dotenv import load_dotenv

load_dotenv()

async def create_table(conn):
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS site (
            id SERIAL PRIMARY KEY,
            url TEXT NOT NULL,
            title TEXT NOT NULL
        )
    ''')

# asynchronous function for parsing and saving data
async def parse_and_save(url):
    # create an asynchronous session for HTTP requests
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('title').text

        # connect to the database and perform data insertion
        conn = await asyncpg.connect('postgresql://postgres:postgres@localhost:5432/data')
        try:
            await create_table(conn)
            await conn.execute(
                "INSERT INTO site (url, title) VALUES ($1, $2)",
                url, title
            )
        finally:
            await conn.close()

# main asynchronous function to start parsing in parallel tasks
async def main(urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(parse_and_save(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    urls = [
        'https://career.habr.com/vacancies?type=all',
        'https://career.habr.com/vacancies?s%5B%5D=2&type=all',
        'https://career.habr.com/vacancies?s%5B%5D=4&type=all',
        'https://career.habr.com/vacancies?s%5B%5D=24&type=all'
    ]

    start_time = time.time()
    asyncio.run(main(urls))  # run the main asynchronous function
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"async: {execution_time}")  # output execution time
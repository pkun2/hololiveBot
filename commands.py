import os
from googleSearchApi import search_google_images
from dotenv import load_dotenv

async def say_hello(message):
    await message.channel.send('안녕하세요!')

async def show_help(message):
    help_text = """
**명령어**
다음은 사용 가능한 명령어 목록입니다.

- `안녕` 인사합니다
- `명령어` 명령어 메시지를 표시합니다. 
- `검색` 구글에서 이미지 검색 (검색 검색할 내용)
    """

    await message.channel.send(help_text)

async def show_image(message):
    load_dotenv()

    API_KEY = os.getenv("API_KEY")
    CSE_ID = os.getenv("CSE_ID")
    SEARCH_QUERY = message.content

    images = search_google_images(API_KEY, CSE_ID, SEARCH_QUERY)
    for img in images:
        await message.channel.send(img)
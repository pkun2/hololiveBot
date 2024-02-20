import discord
import os 
from commands import say_hello, show_help, show_image
from dotenv import load_dotenv

class MyClient(discord.Client):
    async def on_ready(self):
        # CHANNEL_ID 를 int 로 변경후 저장
        channel_id = int(self.channel_id)
        channel = self.get_channel(channel_id)
        if channel:
            print(f'Logged on as {self.user}!')
            await self.change_presence(status=discord.Status.online, activity=discord.Game("명령어"))
        else:
            print(f"Channel with ID {channel_id} not found.")

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        command = message.content.split()[0]

        if command == '안녕':
            await say_hello(message)
        elif message.content.startswith('검색'):
            await show_image(message)
        elif command == '명령어':
            await show_help(message)

if __name__ == "__main__":
    # 환경변수 로드
    load_dotenv()

    # 환경 변수로 부터 토큰, 채널ID를 가져오기
    TOKEN = os.getenv('DISCORD_TOKEN')
    CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')

    intents = discord.Intents.default()
    intents.messages = True
    intents.message_content = True

    client = MyClient(intents=intents)
    # CHANNEL_ID를 MyClient 인스턴스 변수로 저장하여 메서드 내에서 쉽게 접근
    client.channel_id = CHANNEL_ID
    client.run(TOKEN)

}
from aiohttp import (
    ClientResponseError,
    ClientSession,
    ClientTimeout
)
from colorama import *
from datetime import datetime
from fake_useragent import FakeUserAgent
import asyncio, json, re, os, random, pytz

wib = pytz.timezone('Asia/Jakarta')

class Clayton:
    def __init__(self) -> None:
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Host': 'tonclayton.fun',
            'Origin': 'https://tonclayton.fun',
            'Pragma': 'no-cache',
            'Referer': 'https://tonclayton.fun/?tgWebAppStartParam=1493482017',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': FakeUserAgent().random
        }
        self.base_url = "https://tonclayton.fun"
        self.api_base_id = None

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        print(
            f"""
        {Fore.GREEN + Style.BRIGHT}Auto Claim {Fore.BLUE + Style.BRIGHT}Clayton - BOT
            """
            f"""
        {Fore.GREEN + Style.BRIGHT}Rey? {Fore.YELLOW + Style.BRIGHT}<INI WATERMARK>
            """
        )

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
    
    async def find_latest_js_file(self):
        async with ClientSession(timeout=ClientTimeout(total=20)) as session:
            async with session.get(self.base_url) as response:
                response.raise_for_status()
                html = await response.text()
                match = re.search(r'\/assets\/index-[^"]+\.js', html)
                return match.group(0).split('/')[-1] if match else None

    async def fetch_api_base_id(self, retries=5, delay=3):
        for attempt in range(retries):
            js_file = await self.find_latest_js_file()
            if js_file:
                try:
                    async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                        async with session.get(f"{self.base_url}/assets/{js_file}") as response:
                            response.raise_for_status()
                            js_content = await response.text()
                            match = re.findall(r'(\w+)\s*=\s*"([^"]+)"', js_content)
                            if match:
                                for _, api_base_id in match:
                                    if api_base_id.startswith("aT83M535"):
                                        return api_base_id
                            return None
                except (Exception, ClientResponseError) as e:
                    if attempt < retries - 1:
                        await asyncio.sleep(delay)
            else:
                if attempt < retries - 1:
                    await asyncio.sleep(delay)
        return None
    
    async def user_authorization(self, query: str, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/user/authorization'
        headers = {
            **self.headers,
            'Content-Length': '0',
            'Init-Data': query,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
    
    async def save_user(self, query: str, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/user/save-user'
        headers = {
            **self.headers,
            'Content-Length': '0',
            'Init-Data': query,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
                
    async def daily_claim(self, query: str, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/user/daily-claim'
        headers = {
            **self.headers,
            'Content-Length': '0',
            'Init-Data': query,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
    
    async def all_tasks(self, query: str, type: str, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/tasks/{type}'
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.get(url=url, headers=headers) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
        
    async def start_tasks(self, query: str, task_id: int, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/tasks/complete'
        data = json.dumps({'task_id': task_id})
        headers = {
            **self.headers,
            'Content-Length': str(len(data)),
            'Init-Data': query,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
        
    async def claim_tasks(self, query: str, task_id: int, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/tasks/claim'
        data = json.dumps({'task_id': task_id})
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }
        headers = {
            **self.headers,
            'Content-Length': str(len(data)),
            'Init-Data': query,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
        
    async def check_tasks(self, query: str, task_id: int, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/tasks/check'
        data = json.dumps({'task_id': task_id})
        headers = {
            **self.headers,
            'Content-Length': str(len(data)),
            'Init-Data': query,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
        
    async def user_achievements(self, query: str, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/user/achievements/get'
        headers = {
            **self.headers,
            'Content-Length': '0',
            'Init-Data': query,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
        
    async def claim_achievements(self, query: str, type: str, level: int, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/user/achievements/claim/{type}/{level}'
        headers = {
            **self.headers,
            'Content-Length': '0',
            'Init-Data': query,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None

    async def claywheel_info(self, query: str, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/spin/info'
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.get(url=url, headers=headers) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None

    async def perform_claywheel(self, query: str, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/spin/perform'
        data = json.dumps({'multiplier':3})
        headers = {
            **self.headers,
            'Content-Length': str(len(data)),
            'Init-Data': query,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
                
    async def start_game1024(self, query: str, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/game/start'
        headers = {
            **self.headers,
            'Content-Length': '0',
            'Init-Data': query,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None

    async def save_tile(self, query: str, session_id: str, tile: int, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/game/save-tile'
        data = json.dumps({'session_id':session_id, 'maxTile':tile})
        headers = {
            **self.headers,
            'Content-Length': str(len(data)),
            'Init-Data': query,
            'Content-Type': 'application/json'
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None

    async def over_tile(self, query: str, session_id: str, tile: int, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/game/over'
        data = json.dumps({'session_id':session_id, 'multiplier':1, 'maxTile':tile})
        headers = {
            **self.headers,
            'Content-Length': str(len(data

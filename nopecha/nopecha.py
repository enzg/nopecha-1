import asyncio
from typing import Optional
import aiohttp
import requests, time



class Client:
    def __init__(self, api_key: str) -> None:
        if not len(api_key) == 10:
            raise ValueError("API key must be 10 characters long")
        self.api_key = api_key
        self.accepted_captcha = (
                "hcaptcha",
                "recaptcha"
            )

    def request(
            self, 
            captcha_type: str, 
            image_urls: list, 
            task: str
        ) -> dict:
        """
        
                """
        if not captcha_type in self.accepted_captcha:
            raise ValueError("Invalid captcha type")
        data = {
            "type": captcha_type,
            "key": self.api_key,
            "task": task,
            "image_urls": image_urls,
        }

        response = requests.post("https://api.nopecha.com/", json=data)
        return response.json() if response.status_code == 200 else response.status_code

    def get_balance(self, api_key: Optional[str] = None) -> dict:
        """
        Gets your Nopecha balance
        
        api_key: str (optional)

        Returns: dict
        """
        key = self.api_key if api_key == None else api_key
        response = requests.get(f"https://api.nopecha.com/status?key={key}")
        return response.json() if response.status_code == 200 else response.status_code

    def hcaptcha(self, image_urls: list, task: str = None) -> dict:
        """
        Solves Hcaptcha using Nopecha API

        image_urls: list(str)
        task: str

        Returns: dict
        """
        task = self.request("hcaptcha", image_urls, task)
        while True:
            time.sleep(3)
            response = requests.get(f"https://api.nopecha.com/?id={task['data']}&key={self.api_key}").json()
            if type(response.get("data")) != list:
                continue
            return response.get("data")

    def recaptcha(self, image_urls: list, task: str = None) -> dict:
        """
        Solves reCAPTCHA v2 and v3 using Nopecha API

        image_urls: list(str)
        task: str

        Returns: dict
        """
        task = self.request("recaptcha", image_urls, task)
        while True:
            time.sleep(3)
            response = requests.get(f"https://api.nopecha.com/?id={task['data']}&key={self.api_key}").json()
            if type(response.get("data")) != list:
                continue
            return response.get("data")

class AsyncClient:
    def __init__(self, api_key: str) -> None:
        if not len(api_key) == 10:
            raise ValueError("API key must be 10 characters long")
        self.api_key = api_key
        self.accepted_captcha = (
                "hcaptcha",
                "recaptcha"
            )

    async def request(
            self, 
            captcha_type: str, 
            image_urls: list, 
            task: str
        ) -> dict:
        """
        
                """
        if not captcha_type in self.accepted_captcha:
            raise ValueError("Invalid captcha type")
        data = {
            "type": captcha_type,
            "key": self.api_key,
            "task": task,
            "image_urls": image_urls,
        }
        with aiohttp.ClientSession() as session:
            async with session.post("https://api.nopecha.com/", json=data) as response:
                return await response.json() if response.status_code == 200 else response.status_code

    async def get_balance(self, api_key: Optional[str] = None) -> dict:
        """
        Gets your Nopecha balance
        
        api_key: str (optional)

        Returns: dict
        """
        key = self.api_key if api_key == None else api_key
        with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.nopecha.com/status?key={key}") as response:
                return await response.json() if response.status_code == 200 else response.status_code

    async def hcaptcha(self, image_urls: list, task: str = None) -> dict:
        """
        Solves Hcaptcha using Nopecha API

        image_urls: list(str)
        task: str

        Returns: dict
        """
        task = await self.request("hcaptcha", image_urls, task)
        while True:
            await asyncio.sleep(3)
            response = await requests.get(f"https://api.nopecha.com/?id={task['data']}&key={self.api_key}").json()
            if type(response.get("data")) != list:
                continue
            return response.get("data")

    async def recaptcha(self, image_urls: list, task: str = None) -> dict:
        """
        Solves reCAPTCHA v2 and v3 using Nopecha API

        image_urls: list(str)
        task: str

        Returns: dict
        """
        task = await self.request("recaptcha", image_urls, task)
        while True:
            await asyncio.sleep(3)
            response = await requests.get(f"https://api.nopecha.com/?id={task['data']}&key={self.api_key}").json()
            if type(response.get("data")) != list:
                continue
            return response.get("data")

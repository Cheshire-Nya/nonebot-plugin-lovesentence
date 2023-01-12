import httpx
from nonebot import logger, on_command
from nonebot.adapters import Message
from nonebot.matcher import Matcher
from nonebot.params import CommandArg

lovesentence_matcher = on_command("土味情话", aliases={"情话"})

@lovesentence_matcher.handle()
async def lovesentence(matcher: Matcher, args: Message = CommandArg()):
    if args:
        return
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.gmit.vip/Api/LoveSentence?format=json")
    if response.is_error:
        logger.error("获取随机情话失败")
        return
    data = response.json()
    msg = data["data"]["text"]
    await matcher.finish(msg)
import discord
from discord.ext import commands
import aiohttp
import json

config = json.loads(open("/app/data/config.json").read())
class AshiChat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_key = config["openrouter_token"]
        self.model = "mistralai/mistral-small-3.2-24b-instruct:free"
        self.msg_history = {}

    def get_system_prompt(self, user_id):
        if user_id == config["ownerID"]:
            return (
                "[PROMPT HERE]"
            )
        else:
            return (
                "[PROMPT HERE]"
            )

    def prune_history(self, user_id, max_messages=20):
        history = self.msg_history.get(user_id, [])
        if len(history) > max_messages:
            self.msg_history[user_id] = history[-max_messages:]

    async def query_openrouter_with_history(self, user_id):
        url = "https://openrouter.ai/api/v1/chat/completions"
        system_prompt = self.get_system_prompt(user_id)
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        user_history = self.msg_history.get(user_id, [])
        self.prune_history(user_id)

        messages = [{"role": "system", "content": system_prompt}] + user_history
        data = {
            "model": self.model,
            "messages": messages,
            "max_tokens": 1800
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as resp:
                if resp.status == 200:
                    json_data = await resp.json()
                    return json_data["choices"][0]["message"]["content"]
                else:
                    text = await resp.text()
                    return f"❌ API error: {resp.status}\n```{text}```"

    async def query_openrouter(self, messages):
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": self.model,
            "messages": messages,
            "max_tokens": 1500
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as resp:
                if resp.status == 200:
                    json_data = await resp.json()
                    return json_data["choices"][0]["message"]["content"]
                else:
                    text = await resp.text()
                    return f"❌ API error: {resp.status}\n```{text}```"
    # This still needs some work...
    @commands.command(name="grok", help="Checks if the message is true.")
    async def check_truth(self, ctx):
        user_id = ctx.author.id
        async for msg in ctx.channel.history(limit=10):
            if msg.author.bot or msg.id == ctx.message.id:
                continue
            target_message = msg.content
            author_name = msg.author.display_name
            break
        else:
            await ctx.send("I can't read. Teehee~")
            return

        system_prompt = self.get_system_prompt(user_id)

        fact_prompt = (
            f"The user {author_name} said:\n\"{target_message}\"\n"
            "Is this statement true, false, or misleading? Explain your answer, but try to be evasive in a short and snarky way."
        )

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": fact_prompt}
        ]

        temp_msg = await ctx.send("☝🤓 ...")
        reply = await self.query_openrouter_with_history(user_id)
        await temp_msg.delete()
        await ctx.send(f"📢 {reply[:1900]}")

    @commands.command(name="ashi", help=f"Talk to me!")
    async def gpt_chat(self, ctx, *, prompt: str):
        user_id = ctx.author.id
        # Start the first convo with an introduction
        if user_id not in self.msg_history:
            self.msg_history[user_id] = [
                {"role": "user", "content": f"My name is {ctx.author.display_name}."}
            ]
        # Add new message to the history
        self.msg_history[user_id].append({"role": "user", "content": prompt})

        # Send query to API with history
        temp_msg = await ctx.send("💬 ...")
        # DEBUG: Stuff to debug what is being sent
        #print("Sending to model: ")
        #for m in messages_prompt:
        #    print(f"[{m['role']}] {m['content']}")
        reply = await self.query_openrouter_with_history(user_id)
        self.msg_history[user_id].append({"role": "assistant", "content": reply})
        await temp_msg.delete()
        await ctx.send(reply[:1900])

    @commands.command(name="ashirefresh", help="Reset conversation memory.")
    async def reset_memory(self, ctx):
        user_id = ctx.author.id
        if user_id in self.msg_history:
            del self.msg_history[user_id]
            await ctx.send("What were we talking about again?")
        else:
            await ctx.send("No memory to reset.")

async def setup(bot):
    await bot.add_cog(AshiChat(bot))
from random import random
from discord.ext import commands
import discord
import datetime
from tabulate import tabulate


class Guides(commands.Cog):
  def __init__(self,client):
    self.client = client
	
  @commands.command()
  async def guides(self, ctx):
    faq_table = [['h!cafe',"h!schedule","h!crafting"]]
    embed = discord.Embed(
      title="Blue Archive Resources Centre",
      color=discord.Color.random(),
      timestamp=datetime.datetime.utcnow())
    embed.add_field(
      name="ˏ⸉ˋ‿̩̩̽‿̩͙‿̩͙‿̩̩̽‿̩̥̩‿̩͙‿̩̩̽‿̩͙ FAQ/Info ‿̩̩̽‿̩͙‿̩͙‿̩̩̽‿̩͙‿̩̥̩‿̩̩̽‿̩͙‘⸊",
      value=f"```\n{tabulate(faq_table,tablefmt='fancy_grid')}```",
      inline=False)
    embed.add_field(
      name="ˏ⸉ˋ‿̩̩̽‿̩͙‿̩͙‿̩̩̽‿̩̥̩‿̩͙‿̩̩̽‿̩͙ Guides ‿̩̩̽‿̩͙‿̩͙‿̩̩̽‿̩͙‿̩̥̩‿̩̩̽‿̩͙‘⸊",
      value="WIP",
      inline=False)
    embed.add_field(
      name="ˏ⸉ˋ‿̩̩̽‿̩͙‿̩̩̽‿̩̥̩‿̩͙‿̩̩̽‿̩͙ Resources ‿̩̩̽‿̩͙‿̩͙‿̩̩̽‿̩͙‿̩̩̽‿̩͙‘⸊",
      value="WIP",
      inline=False)
    embed.add_field(
      name="If you are interested in helping me write these guides, please contact me: Himari#6182 <:raiden_heart:885507681509593128>. I'll discuss with you and share the file I'm using to write these guides down.",
      value="Thanks~",
      inline=False)
    await ctx.send(embed=embed)
  
  @commands.command(aliases=['affection'])
  async def cafe(self,ctx):
    embed=discord.Embed(title="Cafeteria and Affection", url="https://bluearchive.wiki/wiki/Cafe", colour=discord.Colour.random(),description="The Cafe is unlocked at 2-1 and an important part of the game. Here, you can **raise affection** with your girls by tapping on them or giving them gifts. You can also **collect Stamina and Credits** that regenerate hourly separate from your main Stamina bar shown at the top of the screen.")
    embed.add_field(
      name="Q: How do I increase the comfyness rating of my dorm?", 
      value="**A:** You must place furnitures in it. Furnitures can be obtained from crafting, events or other sources.", inline=False)
    embed.add_field(
      name="Q: How often can I tap the students in my dorm to raise their affection?", 
      value="**A:** You can tap them every **4 hours** for affection increase and they will swap out with other students every **12 hours**.", inline=False)
    embed.add_field(
      name="Q: How do I put students in my dorm?",
      value="**A: You can't.** Random students will come and swap with the current students on your dorm every 12 hours. You can, however, call 1 student of your choice to your dorm every 20 hours by clicking the ticket icon at the bottom of the screen.",
      inline=False
    )
    embed.add_field(
      name="Q: How do I increase the energy/credit and energy/credit cap for my dorm?",
      value="**A:** To increase the rate of energy/credit per hour, you need to increase your cafe's comfyness rating. To increase the energy/credit cap, you must obtain the item needed to upgrade the cafe. This upgrade item can be acquired by clearing(even without 3*) Every 3rd chapter after map 3-5.",
      inline=False
    )
    embed.add_field(
      name="Q: How do I unlock Live2d background of students I own for my homescreen?",
      value="You need to increase the student's affection to you by either tapping them in the cafe, schedules, using them in battles, or giving them gifts in the cafe. You will unlock their Live2d once their affection is high enough. **Refer to the Info list to get their required affection for Live2d.**",
      inline=False
    )
    embed.add_field(
      name="Infos:",
      value="__Student Gift Preference Table and Live2d Level Requirement__: https://bluearchive.wiki/wiki/Affection"
    )
    await ctx.send(embed=embed)
  @commands.command()
  async def schedule(self,ctx):
    embed=discord.Embed(title="Schedule", url="https://bluearchive.fandom.com/wiki/Schedule",colour=discord.Colour.random(), description="Schedule allows you to check around SCHALE and different school campuses in Kivotos. Schedule is unlocked after clearing Campaign map 2-4. Students will randomly be placed on random locations and will swap/move locations at daily server reset(4am JST). You can **raise affection** by tapping on locations in the schools/area. A minimum of 1 student and a maximum of 3 students can enter a location in any given area.")
    embed.add_field(
      name="Q: How to unlock more areas in schedule?", 
      value="**A:** You can unlock more areas for schedule by recruiting certain amount of students(check info list for unlock requirements). Two areas(SCHALE Office and Residential area are unlocked initially after unlocking schedule.", inline=False)
    embed.add_field(
      name="Q: How do I increase my schedule ticket limit?", 
      value="Intially, you are given only 2 schedule tickets. You can increase your schedule ticket limit by lvling up to level 10, 25, and 50. Schedule tickets will be refilled everyday at daily server reset(4am JST) to its maximum value. A maximum of 5 schedule tickets can be refilled this way by lvling up to lvl 50", inline=False)
    embed.set_footer(text="Blue Archive")
    await ctx.send(embed=embed)
  @commands.command()
  async def crafting(self,ctx):
    embed=discord.Embed(title="Crafting", url="https://bluearchive.wiki/wiki/Crafting", description="Crafting is an option in the game where you can produce various items such as Exp Reports,Skill Books,Skill Materials,Gifts, and Furnitures. Crafting is unlocked after clearing 3-2 on the main story.")
    embed.add_field(name="Q:", value="", inline=False)
    embed.add_field(name="undefined", value="undefined", inline=False)
    embed.add_field(name="undefined", value="undefined", inline=False)
    embed.add_field(name="undefined", value="undefined", inline=False)
    embed.add_field(name="undefined", value="undefined", inline=False)
    embed.set_footer(text="Blue Archive")
    await ctx.send(embed=embed)



def setup(client):
  client.add_cog(Guides(client))

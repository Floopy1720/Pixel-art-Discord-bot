import discord
from discord.ext import commands
from PIL import Image, ImageDraw
import shutil

client = commands.Bot(command_prefix = "!draw ") 

@client.event
async def on_ready():
	print('All ok')

@client.command()
async def start(ctx):
	shutil.copy("bot.png", "bot1.png" )
	image = Image.open("bot1.png")
	draw = ImageDraw.Draw(image)
	main_run = True
	R = 255
	G = 0
	B = 0
	shouldi = "sendit"
	
	while main_run:
		await ctx.send(file=discord.File('bot1.png'))
		inpx_run = True
		inpy_run = True
		inpcol_run = True
		x = 0
		y = 0
		xdown = 0
		ydown = 0
		while inpx_run:
			await ctx.send("Enter the X value type stop to stop")
			msg = await client.wait_for('message')
			inpx = msg.content	
			if inpx == "1":
				x = 35
				inpx_run = False
				pass
			elif inpx == "2":
				x = 47
				inpx_run = False
				pass
			elif inpx == "3":
				x = 59
				inpx_run = False
				pass
			elif inpx == "4":
				x = 71
				inpx_run = False
				pass
			elif inpx == "5":
				x = 84
				inpx_run = False
				pass
			elif inpx == "6":
				x = 96
				inpx_run = False
				pass
			elif inpx == "7":
				x = 108
				inpx_run = False
				pass
			elif inpx == "8":
				x = 120
				xdown = 1
				inpx_run = False
				pass
			elif inpx == "9":
				x = 133
				inpx_run = False
				pass
			elif inpx == "10":
				x = 145
				inpx_run = False
				pass
			elif inpx == "11":
				x = 157
				inpx_run = False
				pass
			elif inpx == "12":
				x = 169
				inpx_run = False
				pass
			elif inpx == "13":
				x = 182
				inpx_run = False
				pass
			elif inpx == "14":
				x = 194
				inpx_run = False
				pass
			elif inpx == "15":
				x = 206
				inpx_run = False
				pass
			elif inpx == "16":
				x = 218
				inpx_run = False
				pass
			elif inpx == "stop" or inpcol == "STOP" or inpcol == "Stop":
				main_run = False
				inpx_run = False
				inpy_run = False
				inpcol_run = False
				shouldi = "dont"
			else:
				print(inpx)
				await ctx.send("Invalid input try again")
				pass
			###############################
			pass
		#########################
		while inpy_run:
			await ctx.send("Enter the Y value type stop to stop")
			msg = await client.wait_for('message')
			inpy = msg.content	
			if inpy == "1":
				y = 35
				y -= 1
				inpy_run = False
				pass
			elif inpy == "2":
				y = 47
				y -= 1
				inpy_run = False
				pass
			elif inpy == "3":
				y = 59
				y -= 1
				inpy_run = False
				pass
			elif inpy == "4":
				y = 71
				y -= 1 
				inpy_run = False
				pass
			elif inpy == "5":
				y = 84
				y -= 1
				inpy_run = False
				pass
			elif inpy == "6":
				y = 96
				y -= 1
				inpy_run = False
				pass
			elif inpy == "7":
				y = 108
				y -= 1
				inpy_run = False
				pass
			elif inpy == "8":
				y = 120
				y -= 1
				inpy_run = False
				pass
			elif inpy == "9":
				y = 133
				y -= 1
				inpy_run = False
				pass
			elif inpy == "10":
				y = 145
				y -= 1
				inpy_run = False
				pass
			elif inpy == "11":
				y = 157
				y -= 1
				inpy_run = False
				pass
			elif inpy == "12":
				y = 169
				y -= 1
				inpy_run = False
				pass
			elif inpy == "13":
				y = 182
				y -= 1
				inpy_run = False
				pass
			elif inpy == "14":
				y = 194
				y -= 1
				inpy_run = False
				pass
			elif inpy == "15":
				y = 206
				y -= 1
				inpy_run = False
				pass
			elif inpy == "16":
				y = 218
				inpy_run = False
				pass
			elif inpy == "stop" or inpcol == "STOP" or inpcol == "Stop":
				inpx_run = False
				inpy_run = False
				main_run = False
				inpcol_run = False
				shouldi = "dont"
			else:
				await ctx.send("Invalid input please try again")
				pass
	
		while inpcol_run:
			await ctx.send("Enter the colour type stop to stop")
			msg = await client.wait_for('message')	
			inpcol = msg.content
			if inpcol == "BLUE" or inpcol == "Blue" or inpcol == "blue":
				R = 0
				G = 0
				B = 255
				inpcol_run = False
				pass
			elif inpcol == "RED" or inpcol == "Red" or inpcol == "red":
				R = 255
				G = 0
				B = 0
				inpcol_run = False
				pass
			elif inpcol == "GREEN" or inpcol == "Green" or inpcol == "green":
				R = 0
				G = 255
				B = 0
				inpcol_run = False
				pass
			elif inpcol == "YELLOW" or inpcol == "Yellow" or inpcol == "yellow":
				R = 255
				G = 255
				B = 0
				inpcol_run = False
				pass
			elif inpcol == "light blue" or inpcol == "Light Blue" or inpcol == "CYAN" or inpcol == "Cyan" or inpcol == "cyan":
				R = 0
				G = 255
				B = 255
				inpcol_run = False
				pass
			elif inpcol == "PINK" or inpcol == "Pink" or inpcol == "pink":
				R = 255
				G = 0
				B = 255
				inpcol_run = False
				pass
			elif inpcol == "BLACK" or inpcol == "Black" or inpcol == "black":
				R = 0
				G = 0
				B = 0
				inpcol_run = False
				pass
			elif inpcol == "WHITE" or inpcol == "White" or inpcol == "white":
				R = 255
				G = 255
				B = 255
				inpcol_run = False
				pass
			elif inpcol == "stop" or inpcol == "STOP" or inpcol == "Stop":
				shouldi = "dont"
				main_run = False
				inpcol_run = False
			else:
				await ctx.send("Invalid input please try again")
	
		if shouldi == "sendit":
			if inpx == "8":
				xdown = 130
				pass
			elif inpx == "4":
				xdown = 81
			elif inpx == "12":
				xdown = 179
			else:
				xdown = x + 9
	
			if inpy == "4":
				ydown = y + 10
				pass
			elif inpy == "8":
				ydown = y + 10
			elif inpy == "12":
				ydown = y + 10
			else:
				ydown = y + 9
			
			draw.rectangle((x, y, xdown, ydown), fill=(R, G, B), outline=None)
			image.save("bot1.png")
			print(f"X:{x}")
			print(f"Y:{y}")
			print(f"XDOWN:{xdown}")
			print(f"YDOWN: {ydown}")
		else:
			await ctx.send("Stopped")
	

client.run("I AM NOT DUMB")

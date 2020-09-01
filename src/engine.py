import tcod

FONT_PATH = '../font/'

def main():
	screen_width = 80
	screen_height = 50

	tileset = tcod.tileset.load_tilesheet(FONT_PATH+'arial10x10.png', 32, 8, tcod.tileset.CHARMAP_TCOD)
	console = tcod.Console(screen_width, screen_height)
	
	with tcod.context.new_terminal(console.width, console.height, tileset=tileset,) as context:
		while True:
			console.clear()
			console.print(x=1, y=1, string="@")
			context.present(console)

			for event in tcod.event.wait():
				context.convert_event(event)
				print(event)  
				if event.type == "QUIT":
					raise SystemExit()

if __name__ == '__main__':
	main()

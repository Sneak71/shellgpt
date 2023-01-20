"""
-------------------------------------
# shellgpt - chatgpt for shell
-------------------------------------
"""
__author__ = "z0nd3rl1ng"
__version__ = "0.1.1"

from chatgpt_wrapper import ChatGPT
import random

def shellGPT(state):
    bot = ChatGPT()
    while state < 1:
        interact = input("[ShellGPT]╼> ")
        response = bot.ask(interact)
        print(response)
        if interact == "exit":
            i=1
            
def banner():
	padding = '  '
	S = [[' ','┌','─','┐'],
	     [' ','└','─','┐'],
	     [' ','└','─','┘']]
	H = [[' ','┬',' ','┬'],
	     [' ','├','─','┤'],
	     [' ','┴',' ','┴']]
	E = [[' ','┌','─','┐'],
	     [' ','├','┤',' '],
	     [' ','└','─','┘']]
	L = [[' ','┬',' ',' '],
	     [' ','│',' ',' '],
	     [' ','┴','─','┘']]
	G = [[' ','┌','─','┐'],
	     [' ','│',' ','┬'],
	     [' ','└','─','┘']]
	P = [[' ','┌','─','┐'],
	     [' ','│','─','┘'],
	     [' ','┴',' ',' ']]
	T = [[' ','┌','─','┐'],
	     [' ',' ','│',' '],
	     [' ',' ','┴',' ']]
	
	banner = [S,H,E,L,L,G,P,T]
	final = []
	print('\r')
	init_color = random.randint(10,40)
	txt_color = init_color
	cl = 0

	for charset in range(0, 3):
		for pos in range(0, len(banner)):
			for i in range(0, len(banner[pos][charset])):
				clr = f'\033[38;5;{txt_color}m'
				char = f'{clr}{banner[pos][charset][i]}'
				final.append(char)
				cl += 1
				txt_color = txt_color + 36 if cl <= 3 else txt_color

			cl = 0

			txt_color = init_color
		init_color += 31

		if charset < 2: final.append('\n   ')

	print(f"   {''.join(final)}")
	print(f'{padding}           by z0nd3rl1ng\n')

if __name__ == "__main__":
    banner()
    shellGPT(0)

"""
-----------------------------------------------------------------------
# shellgpt - chatgpt for shell
-----------------------------------------------------------------------
"""
__author__ = "z0nd3rl1ng"
__version__ = "1.0.0"

import random, os

try:
    import openai
except ModuleNotFoundError:
    print("[*] install missing module: openai")
    os.system("pip3 install openai")
    import openai
    
openai.api_key = "[PUT YOUR API KEY HERE]"

"""----------------------------------------------------------------"""


def shellGPT():
    while True:
        interact = input("[ShellGPT]╼> ")
        if interact == "exit":
            exit()
        else:
            response = openai.Completion.create(engine="text-davinci-002",
                prompt=interact,
                max_tokens=2048
            )
            print(response["choices"][0]["text"])
            
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
    shellGPT()

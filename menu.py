from initialize import initialize
from help import help
import os
from ssh_brute import ssh_brute
from ftp_brute import ftp_brute
from smtp import smtp
from facebook_brute import facebook_brute
from twitter_brute import twitter_brute

def menu():
	initialize()
	while 1:
		usr_inp=raw_input("brutus>")

		if usr_inp=="":
			usr_inp=raw_input("brutus>")

		elif usr_inp=="quit" or usr_inp=="exit":
			quit()

		elif usr_inp=="help":
			print("\n")
			help()	

		elif usr_inp=="clear":
			os.system("clear")
		
		elif usr_inp=="ssh":
			ssh_brute()

		elif usr_inp=="ftp":
			ftp_brute()

		elif usr_inp=="smtp":
			smtp()

		elif usr_inp=="facebook":
			facebook_brute()

		elif usr_inp=="twitter":
			twitter_brute()

		else:
			print(usr_inp+": command not recognised ~brutus")
		

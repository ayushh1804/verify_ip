# This is a simple python program which confirms whether the given IP Address is valid or not.
#importing the required libraries
import re

#Function which verifies whether the ip received is valid or not
def check_ip(IP):

	# Regex expression for validating IPv4
	regex_ipv4 = "(([0-9]|[1-9][0-9]|1[0-9][0-9]|"\
			"2[0-4][0-9]|25[0-5])\\.){3}"\
			"([0-9]|[1-9][0-9]|1[0-9][0-9]|"\
			"2[0-4][0-9]|25[0-5])"
	
	# Regex expression for validating IPv6
	regex_ipv6 = "((([0-9a-fA-F]){1,4})\\:){7}"\
			"([0-9a-fA-F]){1,4}"
	
	reg1 = re.compile(regex_ipv4)
	reg2 = re.compile(regex_ipv6)

	#Check whether it is a valid IPv4 addresses
	if (re.search(reg1, IP)):
		return "Valid IPv4"

	#Check Whether it is a valid IPv6 addresses
	elif (re.search(reg2, IP)):
		return "Valid IPv6"

	# If the given IP is invalid
	return "Invalid IP"

#Driver code
if __name__ == "__main__":
    print("Enter the IP Address")
    ip_address = input()
    print(check_ip(ip_address)) 


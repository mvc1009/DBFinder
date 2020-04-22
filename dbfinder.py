#!/bin/python3

#
#
#	This tools is made for educational purpose!
#	A bad usage of this tool is not allowed
#
#	:::::::-.  :::::::.  .-:::::'::::::.    :::.:::::::-.  .,:::::: :::::::..  
#	 ;;,   `';, ;;;'';;' ;;;'''' ;;;`;;;;,  `;;; ;;,   `';,;;;;'''' ;;;;``;;;;  
#	 `[[     [[ [[[__[[\.[[[,,== [[[  [[[[[. '[[ `[[     [[ [[cccc   [[[,/[[['  
#	  $$,    $$ $$""""Y$$`$$$"`` $$$  $$$ "Y$c$$  $$,    $$ $$""""   $$$$$$c    
#	  888_,o8P'_88o,,od8P 888    888  888    Y88  888_,o8P' 888oo,__ 888b "88bo,
#	  MMMMP"`  ""YUMMMP"  "MM,   MMM  MMM     YM  MMMMP"`   """"YUMMMMMMM   "W" 
#
#
#
#
# MOST COMMON DataBases known ports
#
# - Relational databases:
#	MaxDB:			7210
#	MySQL:			3306
#	OracleDB:		1521,1830
#	PostgreSQL:		5432
#	SQL Server (MSSQL):	1433,1434
#
# - NoSQL databases and others data stores:
#	ArangoDB: 		8529
#	Cassandra: 		7000,7001,9042
#	CouchDB:		5984 
#	Elasticsearch:		9200,9300
#	MongoDB:		27017,27018,27019,28017
#	Neo4J:			7473,7474
#	Redis:			6379
#	Riak:			8087,8098
#	RethinkDB:		8080,28015,29015
#	Solr:			7574,8983
#




import sys, os
try:
	import argparse
except:
	print('[!] argparse is not installed. Try "pip install argparse"')
	sys.exit(0)

try:
	import nmap
except:
	print('[!] nmap is not installed. Try "pip install python-nmap"')
	sys.exit(0)



# Display DBFinder Banner
def banner():
	print('\n\n')
	print(':::::::-.  :::::::.  .-:::::\'::::::.    :::.:::::::-.  .,:::::: :::::::..  ')
	print(' ;;,   `\';, ;;;\'\';;\' ;;;\'\'\'\' ;;;`;;;;,  `;;; ;;,   `\';,;;;;\'\'\'\' ;;;;``;;;;  ')
	print(' `[[     [[ [[[__[[\.[[[,,== [[[  [[[[[. \'[[ `[[     [[ [[cccc   [[[,/[[[\'  ')
	print('  $$,    $$ $$""""Y$$`$$$"`` $$$  $$$ "Y$c$$  $$,    $$ $$""""   $$$$$$c    ')
	print('  888_,o8P\'_88o,,od8P 888    888  888    Y88  888_,o8P\' 888oo,__ 888b "88bo,')
	print('  MMMMP"`  ""YUMMMP"  "MM,   MMM  MMM     YM  MMMMP"`   """"YUMMMMMMM   "W" ')
	print('\n')
	print("\t\t\t\t\t\t\t\tVersion 0.1")
	print("\t\t\t\t\t\t\t\tBy: @mvc1009")
	print('\n\n')

def dbprint(args, nmScan):
	for host_up in nmScan.all_hosts():
		if args.verbose:
			print('[+] Host up %s\t(%s)' % (host_up, nmScan[host_up].hostname()))
		for proto in nmScan[host_up].all_protocols():
			lport = nmScan[host_up][proto].keys()
			for port in lport:
				if args.verbose:
					print('\t[+] Port : %s\t%s' % (port , nmScan[host_up][proto][port]['name']))

def listHosts(file):
	f=open(file, 'r')
	hosts = f.read().split()
	list_of_hosts = ''
	for i in hosts:
    		list_of_hosts += i +',';
	list_of_hosts = list_of_hosts[:-1]
	print('List of Hosts to scan: ' + list_of_hosts)
	return hosts


def main():
	#Presentation
	banner()

	# Parsing arguments
	parser = argparse.ArgumentParser(description='DBFinder is used for discovering DB with public visibility.\n\t\t\n Example: $ python3 dbfinder.py -l www.example.com -m -c -o example_databases.txt', epilog='Thanks for using me!')

	group1 = parser.add_mutually_exclusive_group()
	parser.add_argument('-v', '--verbose', action='store_true', help='Turn verbose output on')
	group1.add_argument('-i', '--ids-evasion', action='store_true', dest='ids',help='Turn NMAP to T1 in order to evade IDS protection')
	group1.add_argument('-f', '--fast', action='store_true', help='Turn NMAP to T4 in order to reduce timeouts')
	group2 = parser.add_mutually_exclusive_group()
	group2.add_argument('-l', '--host', action='store', dest='host', help='Target Host', type=str)
	group2.add_argument('-L', '--list-hosts', action='store', dest='list', help='List of target hosts', type=str)
	parser.add_argument('-m', '--most-common', action='store_true', dest='most_common', help='Makes faster by reducing the number of ports to the most common ones')
	parser.add_argument('-o', '--output', action='store', dest='file', help='Write results to a file', type=str)
	parser.add_argument('-c', '--color', action='store_true', help='Colorize DBFinder output')
	global args
	args =  parser.parse_args()

  	#Usage
	if len(sys.argv) < 2:
		parser.print_help()

	#Program
	nmap_arguments = ''
		#MODE: most_common
	if args.most_common:
		print('[!] MOST COMMON mode turned on')
		db_ports = '3306,1521,1830,1433,1434,7000,7001,27017,27018,27019,28017,7473,7474'
	else:
		db_ports = '7210,3306,1521,1830,5432,1433,1434,8529,7000,7001,9042,5984,9200,9300,27017,27018,27019,28017,7473,7474,6379,8087,8089,8080,28015,29015,7574,8983'
		
		#MODE: fast
	if args.fast:
		print('[!] FAST mode turned on')
		nmap_arguments += ' -T4'
		#MODE: ids evasion
	elif args.ids:	
		print('[!] IDS Evasion turned on')
		nmap_arguments += ' -T1'
	
	if args.host or args.list:
		if args.host:
			list_of_hosts=[args.host]
		else:
			list_of_hosts = listHosts(args.list)
		nmScan = nmap.PortScanner()
		for host in list_of_hosts:
			nmScan.scan(host,db_ports, arguments='-sS' + nmap_arguments)
			dbprint(args, nmScan)

try:
	if __name__ == "__main__":
		main()
except KeyboardInterrupt:
	print("[!] Keyboard Interrupt. Shutting down")

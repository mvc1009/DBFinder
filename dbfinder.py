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


def listHosts():
	f=open('list.txt', 'r')
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
	parser = argparse.ArgumentParser(description='DBFinder is used for discovering DB with public visibility')
	parser.add_argument('-v', '--verbose', action='store_true', help='Turn verbose output on')
	parser.add_argument('-i', '--ids-evasion', action='store_true', help='Turn NMAP to T1 in order to evade IDS protection')
	parser.add_argument('-F', '--fast', action='store_true', help='Turn NMAP to T4 in order to reduce timeouts and search for common databases')
	parser.add_argument('-l', '--host', action='store', dest='host', help='Target Host', type=str)
	parser.add_argument('-L', '--list-hosts', action='store', dest='list', help='List of target hosts', type=str)
	parser.add_argument('-o', '--output', action='store', dest='file', help='Write results to a file', type=str)
	parser.add_argument('-c', '--color', action='store_true', help='Colorize DBFinder output')
	global args
	args =  parser.parse_args()

  	#Usage
	if len(sys.argv) < 2:
		parser.print_help()

	#Program
	if args.fast:
		print("fast")
	db_knownports = '7210,3306,1521,1830,5432,1433,1434,8529,7000,7001,9042,5984,9200,9300,27017,27018,27019,28017,7473,7474,6379,8087,8089,8080,28015,29015,7574,8983'



try:
	if __name__ == "__main__":
		main()
except KeyboardInterrupt:
	print("[!] Keyboard Interrupt. Shutting down")

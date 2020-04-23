import os, sys
import nmap


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

def listHosts():
	f=open('list.txt', 'r')
	hosts = f.read().split()
	list_of_hosts = ''
	for i in hosts:
    		list_of_hosts += i +',';
	list_of_hosts = list_of_hosts[:-1]
	print('List of Hosts to scan: ' + list_of_hosts)
	return hosts


db_knownports = '7210,3306,1521,1830,5432,1433,1434,8529,7000,7001,9042,5984,9200,9300,27017,27018,27019,28017,7473,7474,6379,8087,8089,8080,28015,29015,7574,8983'

nmScan = nmap.PortScanner()
list_of_hosts = listHosts()
for host in list_of_hosts:
	nmScan.scan(host,db_knownports, arguments='-sS')
	for host_up in nmScan.all_hosts():
		print('[+] Host up %s\t(%s)' % (host, nmScan[host_up].hostname()))
		for proto in nmScan[host_up].all_protocols():
			lport = nmScan[host_up][proto].keys()
			for port in lport:
				print('\t[+] Port : %s\t%s' % (port , nmScan[host_up][proto][port]['name']))




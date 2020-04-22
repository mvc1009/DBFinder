import os, sys
import nmap

f=open('list.txt', 'r')
hosts = f.read().split()

for i in hosts:
    print(i)

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

db_knownports = '7210,3306,1521,1830,5432,1433,1434,8529,7000,7001,9042,5984,9200,9300,27017,27018,27019,28017,7473,7474,6379,8087,8089,8080,28015,29015,7574,8983'

nmScan = nmap.PortScanner()
nmScan.scan('127.0.0.1',db_knownports)
for host in nmScan.all_hosts():
	print('Host %s (%s)' % (host, nmScan[host].hostname()))
	print('State : %s' % nmScan[host].state())
	for proto in nmScan[host].all_protocols():
		print('-----------')
		print('Protocol : %s' % proto)
		lport = nmScan[host][proto].keys()

		for port in lport:
			print('port : %s\tstate : %s' % (port , nmScan[host][proto][port]['state']))
			print(nmScan[host][proto][port])


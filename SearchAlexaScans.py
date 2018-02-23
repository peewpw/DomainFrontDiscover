from netaddr import IPNetwork, IPAddress
import sys

if len(sys.argv) <= 1:
	print('Please specify a file of "ip,hostname".')
	sys.exit()
ipfile = sys.argv[1]

if len(sys.argv) <= 2:
	print('Please specify a file of ranges.')
	sys.exit()
rangefile = sys.argv[2]

ips = [line.strip() for line in open(ipfile)]

ranges = [line.strip() for line in open(rangefile)]

for ip in ips:
	info = ip.split(',')
	for rng in ranges:
		if IPAddress(info[0]) in IPNetwork(rng):
			print info[1]

# DomainFrontDiscover
Scripts and results for finding domain frontable CloudFront domains

A walkthrough of what happened here can be found at https://www.peew.pw/blog/2018/2/22/how-i-identified-93k-domain-frontable-cloudfront-domains

### ConfirmedFrontableDomains.txt

A list of 93k+ domains that were confirmed to work for domain fronting through CloudFront (on Feb 22, 2018).

### ConfirmedFrontableDomains-Alexa1M.txt

A list of ~4500 domains in the Alexa top million that were confirmed to work for domain fronting through CloudFront (on Feb 22, 2018).

### SearchAlexaScans.py

A Python script that takes 2 files:
    a list of hosts in the format "hostname,IP"
    a list of network ranges
and outputs
    a list of hostnames that have an IP in those ranges

Used for determining what domains in alexa scan results have an IP in CloudFront ranges.

Alexa scan results: https://censys.io/data/443-https-tls-alexa_top1mil (alexa-results.csv.lz4)

CloudFront Ranges: http://d7uri8nf7uskq.cloudfront.net/tools/list-cloudfront-ips

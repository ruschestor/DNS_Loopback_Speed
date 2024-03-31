import time
import os
import socket

number_of_tests = 10000
delay = 0.5
domains = ["dns-speed-test-domain-1.com","dns-speed-test-domain-2.com","dns-speed-test-domain-3.com"]

#print ("DNS Servers:", dns_resolver.nameservers)
for i in range(len(domains)):
	results = []

	# First attempt before main tests
	try:
		result1 = socket.gethostbyname(domains[i])
	except Exception:
		result1 = "0.0.0.0  "

	for j in range(number_of_tests):
		# Flush DNS cache between attempts
		#if (os.name == "nt"):
		#	os.system('ipconfig /flushdns > NUL')
		#else:
		#	os.system('sudo resolvectl flush-caches')

		# Delay between attempts
		time.sleep(delay)

		# START
		start_time = time.perf_counter_ns()
		
		try:
			result = socket.gethostbyname(domains[i])
		except Exception:
			pass
		
		# END
		end_time = time.perf_counter_ns()
		perf_time = end_time - start_time
		results.append(perf_time)

	# Analysis
	#results.remove(max(results))
	#results.remove(min(results))
	average = round(sum(results) / len(results))
	print ("Test #",i+1,"\t| Domain =",domains[i],"\t| IP =",result1, "\t| Number of tests =",number_of_tests,"\t| Min/Max delay =",min(results),"/",max(results), "ns","\t| Average delay =", average, "ns")

# hosts:
#	0.0.0.0   dns-speed-test-domain-1.com
#	127.0.0.0 dns-speed-test-domain-2.com
#	127.0.0.1 dns-speed-test-domain-3.com
#	10.0.0.69 host.docker.internal

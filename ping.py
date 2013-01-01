import subprocess
import pingparser

def ping(host):
	ping = subprocess.Popen(
		["ping", "-c", "1", "-W", "1", host],
		stdout = subprocess.PIPE,
		stderr = subprocess.PIPE
	)
	
	out, error = ping.communicate()
	
	return pingparser.parse(out)
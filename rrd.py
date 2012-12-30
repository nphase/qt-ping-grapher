# apt-get install python-rrdtool
import os, sys, rrdtool, tempfile, random, time


def create_rrd(filename):
	if os.path.isfile(filename):
		os.remove(filename)
	
	ret = rrdtool.create(filename, "--step", "5", "--start", '0',
		"DS:rtt:GAUGE:2:0:5000",
		"RRA:AVERAGE:0.5:1:1500",
		"RRA:MAX:0.5:1:1500")


def update_rrd(filename, latency_stats):
	ret = rrdtool.update(filename,'N:' + str(latency_stats['avgping']));
	if ret:
		print rrdtool.error()

def update_png(png_filename, rrd_filename, width=400, height=100):
	ret = rrdtool.graph( png_filename, 
		"--lower-limit", "0", 
		"--width", `width`, 
		"--height", `height`, 
		"-c", "GRID#bfbfaf", 
		"-c", "MGRID#6B6C5B", 
		"-c", "CANVAS#B0B0A2", 
		"-c", "FONT#b1b1b1", 
		"-c", "BACK#323232", 
		"--border=0", 
		"--start", 
		"-10m", 
		"--vertical-label=RTT (ms)",
		"DEF:roundtrip_avg="+rrd_filename+":rtt:AVERAGE",
		"DEF:roundtrip_max="+rrd_filename+":rtt:MAX",
		"LINE3:roundtrip_avg#000000:Average Latency",
		"GPRINT:roundtrip_avg:LAST:Last\: %5.2lf",
		"GPRINT:roundtrip_avg:AVERAGE:Avg\: %5.2lf",
		"GPRINT:roundtrip_avg:MAX:Max\: %5.2lf")

def remove_png(png_filename):
	if os.path.isfile(png_filename):
		os.remove(png_filename)

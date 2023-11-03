import os
import time
import subprocess
from datetime import datetime

timestamp = 0

while True:
    pcap_filename = f'traffic_{timestamp}.pcap'
    
    tcpdump_process = subprocess.Popen(['sudo', 'tcpdump', '-i', 'enp2s0', '-w', pcap_filename, '-v'])
    
    time.sleep(30)
    
    tcpdump_process.kill()
    subprocess.run(['curl', '-X', 'POST', 'http://moznoporusski.ru:3333/api/pcap/upload',
                    '-H', 'Content-Type: multipart/form-data',
                    '-F', f'file=@{pcap_filename}',
                    '-F', 'flush_all=true'])
    
    os.remove(pcap_filename)
    timestamp += 1

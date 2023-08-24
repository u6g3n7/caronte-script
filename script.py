import os
import time
import subprocess
from datetime import datetime

while True:
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    pcap_filename = f'traffic_{timestamp}.pcap'
    
    tcpdump_process = subprocess.Popen(['sudo', 'tcpdump', '-ni', 'eth1', 'port', '80', '-w', pcap_filename, '-v'])
    
    time.sleep(30)
    
    tcpdump_process.terminate()
    
    subprocess.run(['curl', '-X', 'POST', 'http://10.60.30.129:3333/api/pcap/upload',
                    '-H', 'Content-Type: multipart/form-data',
                    '-F', f'file=@{pcap_filename}',
                    '-F', 'flush_all=true'])
    
    os.remove(pcap_filename)

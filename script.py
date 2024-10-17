import os
import time
import subprocess
import keyboard

timestamp = 0
should_continue = True

def stop_script():
    global should_continue
    should_continue = False


keyboard.add_hotkey('ctrl+shift+x', stop_script)

while should_continue:
    pcap_filename = f'traffic_{timestamp}.pcap'
    
    tcpdump_process = subprocess.Popen(['sudo', 'tcpdump', '-i', 'ens33', '-w', pcap_filename, '-v']) # change ethetnet
    

    for _ in range(15):
        time.sleep(1)
        if not should_continue:
            break
    
    tcpdump_process.terminate()
    tcpdump_process.wait()
    
    if should_continue:
        subprocess.run(['curl', '-X', 'POST', 'http://10.8.0.2:3333/api/pcap/upload', # change ip addres
                        '-H', 'Content-Type: multipart/form-data',
                        '-F', f'file=@{pcap_filename}',
                        '-F', 'flush_all=true'])
    
        os.remove(pcap_filename)
        timestamp += 1

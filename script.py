
# Заменить интернет интерфейс
# Заменить айпи для каронты


import os
import time
import subprocess

a = 1

while True:
    # Запуск tcpdump
    subprocess.Popen(['sudo','tcpdump', '-ni', 'eth1', 'port', '80', '-w', f'traffic{a}.pcap', '-v'])
    
    # Ожидание 30 секунд
    time.sleep(30)
    
    # Завершение tcpdump
    subprocess.run(['pkill', 'tcpdump'])
    
    # Выполнение curl
    subprocess.run(['curl', '-X', 'POST', 'http://10.60.30.129:3333/api/pcap/upload',
                    '-H', 'Content-Type: multipart/form-data',
                    '-F', f'file=@traffic{a}.pcap',
                    '-F', 'flush_all=true'])
    
    # Удаление файла
    os.remove(f'traffic{a}.pcap')
    
    # Увеличение значения a
    a += 1

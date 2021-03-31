import paramiko
import time

host= "192.168.124.60"
port=22
username="f13"
password="!Q2w#E4r%T6y&U"

def main():
    try:
        zimbra = paramiko.SSHClient()
    #    zimbra.load_system_host_keys()
        zimbra.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        zimbra.connect(host,port,username,password,allow_agent=False)
        stdin,stdout,stderr =  zimbra.exec_command('ls -l /tmp')
        time.sleep(5)
        print(''.join(stdout.readlines()))
        
        zimbra.close()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
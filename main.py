import paramiko

hostname = 'localhost'
username = 'codesenju'
password = 'passw0rd'
PORT = '2222'
ssh = paramiko.SSHClient()


def execRemoteCommand(cmd_, client):
    print(cmd_)
    stdin, stdout, stderr = client.exec_command(cmd_)
    output = stderr.readlines()
    for index, item in enumerate(output):
        print(item)
    output = stdout.readlines()
    for index, item in enumerate(output):
        print(item)


if __name__ == "__main__":

    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=hostname, username=username, password=password, port=PORT)
        sftp_client = ssh_client.open_sftp()

        # 1. CHANGE PATH IN REMOTE HOST
        print("##########-1.-CHANGE-PATH-##########")
        sftp_client.chdir("/tmp")
        print(sftp_client.getcwd())

        # 2. RUN COMMAND ON REMOTE HOST
        print("##########-2.-REMOTE-COMMAND-##########")
        execRemoteCommand("ls -l /tmp", ssh_client)

        # 3. COPY FILE TO REMOTE HOST
        print("##########-3.-REMOTE-COMMAND-##########")
        sftp_client.put("README.md", "README.md")
        execRemoteCommand("stat /tmp/README.md", ssh_client)

        # 4. DOWNLOAD FILE FROM REMOTE HOST
        print("##########-4.-DOWNLOAD-FILE-##########")
        sftp_client.get("/tmp/remote_file.txt","remote_file.txt")
        
    except Exception as err:
        print("SSH CLIENT ERROR: {}".format(err))
    finally:
        #    sftp_client.close()
        ssh_client.close()

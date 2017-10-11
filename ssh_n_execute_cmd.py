import paramiko
import os

__author__ = 'Praveen N'


class SshToLinuxMachine():

    def __init__(self):
        self.port = 22
        self.client = None

    def connection(self, **kwargs):
        """
        connect to remote server using password less or password based
        authentication
        :return:
        """
        try:
            username = kwargs.get('username', None)
            password = kwargs.get('password', None)
            port = kwargs.get('port', None)
            host = kwargs.get('host', None)

            if not port:
                port = self.port

            if host:
                self.client = paramiko.SSHClient()
                self.client.set_missing_host_key_policy(paramiko.
                                                        AutoAddPolicy())

                if not password:
                    self.client.connect(host, username=username,
                                        pkey=paramiko.
                                        RSAKey.from_private_key_file
                                        (os.path.expanduser('~/.ssh/id_rsa')))
                else:
                    self.client.connect(host, port=port,
                                        username=username, password=password)

        except Exception as e:
                print(e)

    def execute_command(self, **kwargs):

        try:
            output = ""
            if self.client.connect:
                command = kwargs.get('command', None)
                std_in, std_out, std_err = self.client.exec_command(command)
                output = std_out.readlines()
            print(output)
            return output

        except Exception as e:
            print(e)

    def close_connection(self):
            if self.client is not None:
                self.client.close()
                self.client = None


# Create a Object
SshToLinuxMachine = SshToLinuxMachine()

# SSH using username and password(Connection Establishment)
SshToLinuxMachine.connection(username="root",password="root",
                             port=22,host="192.168.56.103")
                             

# Executing a command
SshToLinuxMachine.execute_command(command="ifconfig enp0s3 ")

# Closing a connection
SshToLinuxMachine.close_connection()

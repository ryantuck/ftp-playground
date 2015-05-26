# FTP server script

import os
import yaml
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# pull in FTP credential configs
dir_path = os.path.dirname(os.path.abspath(__file__))
with open(dir_path + '/config.json') as c:
    config = yaml.safe_load(c)

# define FTP parameters
host        = config['ftp']['host']
username    = config['ftp']['username']
password    = config['ftp']['password']
port        = config['ftp']['port']


print 'creating authorization'
authorizer = DummyAuthorizer()
authorizer.add_user(username,password,'./ftp_directory',perm='elradfmw')

handler = FTPHandler
handler.authorizer = authorizer

print 'spinning up server'
server = FTPServer((host,port), handler)
server.serve_forever()



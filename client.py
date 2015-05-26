# FTP client demo code for local testing

import os
from ftplib import FTP
import yaml

# pull in FTP credential configs
dir_path = os.path.dirname(os.path.abspath(__file__))
with open(dir_path + '/config.json') as c:
    config = yaml.safe_load(c)

# define FTP parameters
host        = config['ftp']['host']
username    = config['ftp']['username']
password    = config['ftp']['password']
port        = config['ftp']['port']

# connect to server
conn = FTP()
conn.connect(host,port)
conn.login(username,password)

# list directory contents
conn.dir()

# load file from local directory
local_dir = dir_path + '/local_directory/'
filename = 'test_file.txt'
abs_filepath = local_dir + filename

# transfer file from local directory
conn.storlines('STOR ' + filename, open(abs_filepath))


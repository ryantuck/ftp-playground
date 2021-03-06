# Quick FTP Demo

Spins up a basic local FTP server, and provides demo client code for reading and writing to it.

## Instructions

**start FTP server**

`python run_ftp_server.py`

**read directory and upload new file**

`python client.py`

## Notes

Uses [ftplib](https://docs.python.org/2/library/ftplib.html), the built-in python FTP library.

Edit `client.py` for messing around with client-side code (obviously!). 

The directories `ftp_directory` and `local_directory` correspond to the respective directories we're reading from and writing to from our local machine.

`config.json` stores the FTP configuration parameters, like host, port, username, and password.


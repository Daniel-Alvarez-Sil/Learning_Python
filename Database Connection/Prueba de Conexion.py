import pyodbc

conexion = pyodbc.connect('DRIVER = {Progress OpenEdge 11.3 Driver}; HostName = localhost; DATABASENAME = scrmcc; PORTNUMBER = 12042')
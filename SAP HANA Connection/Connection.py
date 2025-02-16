from hdbcli import dbapi

cAddress = '192.168.0.179'
cPort = '39015'
cUser = 'hxeadm'
cPassword = 'P0K3M0NJ4P4N26__sap'

connection = dbapi.connect(
    address = cAddress,
    port = cPort
    #,user = cUser,
    #password = cPassword
)

print('connected')



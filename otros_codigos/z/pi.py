import xmlrpclib
import csv
import sys

username = "admin"
pwd = "Mensaje1"
dbname = "lac"
print 'conectado...'
sock_common = xmlrpclib.ServerProxy("http://localhost:8069/xmlrpc/common")

uid = sock_common.login(dbname, username, pwd)

sock = xmlrpclib.ServerProxy("http://localhost:8069/xmlrpc/object")
print 'conectado!'
print 'procesando...'

reader = csv.reader(open('bdclac.csv','rb'))
for row in reader:
    nit=str(row[1])
    print nit
    partner = {'name':row[0] ,  'lang': 'es_BO', 'type' : 'default', 'razon_social':row[0], 'vat':nit, }
    partner_id = sock.execute(dbname, uid, pwd, 'res.partner', 'create', partner)
    sys.stdout.write('.')
    
print 'ok'

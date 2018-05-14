import xmlrpclib
import string
import csv
import sys

username = "admin"
pwd = "M1"
dbname = "ez-zepol-cc"
print 'conectado...'
sock_common = xmlrpclib.ServerProxy("http://ez.zepol.cc/xmlrpc/common")

uid = sock_common.login(dbname, username, pwd)

sock = xmlrpclib.ServerProxy("http://ez.zepol.cc/xmlrpc/object")
print 'conectado!'
print 'procesando...'

reader = csv.reader(open('datos_empleados.csv','rb'))
for row in reader:
    nit=str(row[0])
    print nit
    partner = {'name':string.capwords(row[2]) ,  'lang': 'es_BO', 'type' : 'contact', 'street':string.capwords(row[3]), 'vat':nit, 'customer':False  }
    partner_id = sock.execute(dbname, uid, pwd, 'res.partner', 'create', partner)
    sys.stdout.write('.')
    
print 'ok'

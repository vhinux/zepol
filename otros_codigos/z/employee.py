import erppeek
import string
import csv
import sys

database = 'ez-zepol-cc'
server = 'http://ez.zepol.cc'
admin_password = 'M1'
user = 'admin'

print 'conectado!'
print 'procesando...'

client = erppeek.Client(server, database, user, admin_password)


reader = csv.reader(open('datos_empleados.csv','rb'))
for row in reader:
    nit=str(row[0])
    idc=client.model('res.partner').search([('vat','=',nit)], limit=1, order='id desc')    
    if idc:
       datos_user = client.model('res.partner').browse(idc)
       print(datos_user.name[0])
       config_record = client.model('hr.employee').create({})
       config_record.write({'country_id': 29,
                            'name': datos_user.name[0],
                            'identification_id':datos_user.vat[0],
                            'address_home_id':idc[0],  
})

       config_record.execute()
 

print 'ok'


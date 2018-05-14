import xmlrpclib
import csv

username = "admin"
pwd = "M1"
dbname = "lac-o-openbiz.com.bo"

sock_common = xmlrpclib.ServerProxy("https://lac.o.openbiz.com.bo/xmlrpc/common")
uid = sock_common.login(dbname, username, pwd)

sock = xmlrpclib.ServerProxy("https://lac.o.openbiz.com.bo/xmlrpc/object")

reader = csv.reader(open('output.csv','rb'))
for row in reader:
    print row[0]
    product_template = {
        'default_code': row[1],
        'name': row[2].title(),
        'list_price': row[3],
        'mes_type':'fixed',
        'uom_id':1,
        'uom_po_id':1,
        'type':'product',
        'taxes_id':'[(6, 0, [1, 3])]',
        'procure_method':'make_to_stock',
        'cost_method':'standard',
        'categ_id':1}
    template_id=sock.execute(dbname, uid,pwd, 'product.template','create',product_template)
    change_id = sock.execute_kw(dbname, uid, pwd,'stock.change.product.qty', 'create', [{
                'product_id': template_id,
                'location_id': 15,
                'new_quantity': row[4],
                }])
    sock.execute_kw(dbname, uid, pwd, 'stock.change.product.qty', 'change_product_qty', [change_id])

    # product_product = {
    #     'product_tmpl_id':template_id,
    #     'default_code':row[0],
    #     'taxes_id':[1,3],
    #     'active': True,
    #     }
    # product_id = sock.execute(dbname,uid,pwd,'product.product','create',product_product)




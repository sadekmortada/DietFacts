import xmlrpc.client
import csv

server = "http://localhost:8069"
database = "dietfacts2"
#use your email and password of you odoo account instead
user = "test@test.com"
password = "test"

common = xmlrpc.client.ServerProxy("%s/xmlrpc/2/common" % server)
print(common.version())

uid = common.authenticate(database, user, password, {})

odooApi = xmlrpc.client.ServerProxy("%s/xmlrpc/2/object" % server) #models access

filter1 = [[("categ_id",'=',4)]]
product__count = odooApi.execute_kw(database, uid, password,"product.template","search_count",filter1)
print(product__count)

filter2 = [[["largemeal",'=',True]]]
meal__count = odooApi.execute_kw(database, uid, password,"meal.template","search_count",filter2)
print(meal__count)

ids = odooApi.execute_kw(database, uid, password,"product.template","search",[[]],{'limit':1})
print(ids)

file = "data.csv"
reader = csv.reader(open(file,'r')) #reader for reading line by line



#let's get the Diet Items category Id first
filter = [[("name","=","Diet Items")]]
categ_id = odooApi.execute_kw(database, uid, password, "product.category", "search", filter)
if categ_id:
    print("category is found, with id =", categ_id[0])
else:
    print("category is not found")
categ_map = {"Diet Items" : categ_id[0]}
for row in reader:
    print("checking ",row)
    productname=row[0]
    productcalories=row[1]
    record = [{'name':productname,'calories':productcalories}]
    productid = odooApi.execute_kw(database, uid, password, "product.template", "search",[[("name",'=',productname)]]) 
    if not productid:
        if len(row) == 3 and row[2] in categ_map:
            record[0]["categ_id"]=categ_map[row[2]]
        odooApi.execute_kw(database, uid, password, "product.template", "create",record)
        print("record was saved successfully")
    else:
        print("record already exists, updating fields...")
        if len(row) == 3 and row[2] in categ_map:
            record = [productid, {"calories":productcalories,"categ_id":categ_map[row[2]]}]
            odooApi.execute_kw(database, uid, password, "product.template", "write",record)







from EasySqlLite import *

database = "PATH/EasySqlLite.db"
conn = create_connection(database)
#create table
#Example using
#create_table(conn,'test_EasySqlLite', "column1 type,"
#                                      "column2 type,"
#                                      "column3 type...")
create_table(conn,'test_EasySqlLite', "id INTEGER PRIMARY KEY,"
                                      "name TEXT,"
                                      "email TEXT")

#insert row
#Example using
#insert_row(conn, 'table_name', "column1,column2,column3...", "value1,'value2',value3...")
insert_row(conn, 'test_EasySqlLite', "id,name,email", "1,'Alaa','alaa@nudjh.sa'")
insert_row(conn, 'test_EasySqlLite', "id,name,email", "2,'Alaa Najmi','alaa@nudjh.sa'")

#update row
#Example using
#update_row(conn, 'test_EasySqlLite', "column='value'","where")
update_row(conn, 'test_EasySqlLite', "name='Alaa Najmi'","id=1")

#delete row
#Example using
#delete_row(conn, 'table_name',"where")
delete_row(conn, 'test_EasySqlLite',"id=1")

#Get one result
#Example using
#select_rows(conn,'table_name','where','order by',False)
get_one_result = select_rows(conn,'test_EasySqlLite',None,None,False)
print(get_one_result)

#get All result
#Example using
#select_rows(conn,'table_name','where','order by',True)
get_all_result = select_rows(conn,'test_EasySqlLite','name="Alaa Najmi"',"name ASC",True)
for get_data in get_all_result:
  print('id : ',get_data[0])
  print('name : ',get_data[1])
  print('email : ',get_data[2])

#get num rows
#Example using
#num_rows(conn,'table_name','where)
num = num_rows(conn,'test_EasySqlLite',None)
print(num)


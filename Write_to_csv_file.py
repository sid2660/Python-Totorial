## Writer, DictWriter
## Writer
# from csv import writer
# with open("Wcsv.csv","w",newline="") as f:
#     csv_writer = writer(f)
    ## methods --> writerow, writerows
    ## writerow
    # csv_writer.writerow(['name','country'])
    # csv_writer.writerow(['Siddhartha','India'])
    # csv_writer.writerow(['Mohit','India'])
    
    
    ### Writerows
    # csv_writer.writerows([['name','country'],['Siddhartha','India'],['Mohit','India']])
    
    
    
    
#### DictWriter
from csv import DictWriter
with open("Wfinal.csv","w",newline="") as f:
    csv_writer = DictWriter(f,fieldnames=["firstname","lastname","age"])
    csv_writer.writeheader()
    ### writerow, writerows
    
    csv_writer.writerow({
        'firstname' : "siddhartha",
        "lastname" : "Singh",
        "age" : 20
        
    })
    csv_writer.writerow({
        'firstname' : "Mohit",
        "lastname" : "Singh",
        "age" : 22
        
    })
    
    ##### Writerows ---> [dict,dict,dict]
    csv_writer.writerows([
        {'firstname' : "siddhartha","lastname" : "Singh","age" : 20},
        {'firstname' : "Rohit","lastname" : "Singh","age" : 22},
        {'firstname' : "sid","lastname" : "Singh","age" : 23}
    ])
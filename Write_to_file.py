# w, a,r+
## w mode

# with open("Read_file.txt","w") as f: 
#     f.write("Hello!!!") 
    
### W mode overwrite the data and delete all previus data , 
## use this when file is empty
## it`s also use to create file without delete any file data

## a mode 

with open("Read_file.txt","a") as f: 
    f.write(" Hello!!!") 

## this a = append data means the data i use to write in program is append in file 
## without overriding the data 
## it`s also use to create file without delete any file data

## r+ mode 

with open("Read_file.txt","r+") as f: 
    f.seek(len(f.read()))
    f.write(" Hello!!!") 
    
### r+ mode overwrite the data , 
## for that we use seek method 
## It is able to read and write both


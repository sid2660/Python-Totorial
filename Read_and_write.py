with open("Read_file.txt",'r') as rf:
    with open("Read_file2.txt",'w') as wf:
        wf.write(rf.read())
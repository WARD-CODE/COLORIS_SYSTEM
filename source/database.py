import csv

def add_data(sequence):
   with open("programmes.csv", 'a',newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(sequence)

def retrieve_data(prg):

    data_list = []
    
    with open("programmes.csv", 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        if prg=="ALL":
            for row in csv_reader:
                data_list.append(row)
                
        else:
            for row in csv_reader:
                if row[0]== prg:
                    data_list = row[2:]

        return data_list




            
            


if __name__=="__main__":
    pass
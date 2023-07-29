import csv

def add_data(sequence):
   with open("programmes.csv", 'a',newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(sequence)

def retrieve_data():
    data_list = []
    with open("programmes.csv", 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)

        for row in csv_reader:
            data_list.append(row)
        
        return data_list

def mod_data(name):
    with open("programmes.csv", 'a',newline='') as f:
        csv_writer = csv.writer(f)

            
            


if __name__=="__main__":
    retrieve_data("qdqsd")

import csv
import os

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


def modify(row_num,data):

   input_file = 'programmes.csv'
   output_file = 'temp_file.csv'

   with open(input_file, 'r') as csv_in:
       reader = csv.reader(csv_in)
       rows = list(reader)

       rows[row_num] = data

   with open(output_file, 'w', newline='') as csv_out:
      rows.pop()
      writer = csv.writer(csv_out)
      writer.writerows(rows)

   os.remove(input_file)  # Delete the original CSV file
   os.rename(output_file, input_file)  # Rename the temporary file to the original filename

def save_config(data,motor):
    
    if motor == "M1":
       with open("configuration_M1.csv", 'w') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(data)

    elif motor == "M2":
       with open("configuration_M2.csv", 'w',newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(data)

def load_config(motor):
    if motor == "M1":
       with open("configuration_M1.csv", 'r',newline='') as f:
            csv_reader = csv.reader(f)
            row = next(csv_reader,None)

    elif motor == "M2":
       with open("configuration_M2.csv", 'r',newline='') as f:
            csv_reader = csv.reader(f)
            row = next(csv_reader,None)
     
    return row

if __name__=="__main__":
    pass

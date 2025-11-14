import time
#'C:/Work/Yoobic/space_xyc_12345'
def read_csv_realtime(filepath):
    with open(filepath, 'r') as file:
        headers = next(file).strip().split(',')
        #print(f"Headers: {headers}")
        while True:
            line=file.readline()
            if not line:
                time.sleep(1)
                continue
            row = tuple(line.strip().split(','))
            process_row(row)
def process_row(row_tuple):
    print("Received row:",row_tuple)
result=read_csv_realtime('C:/Work/Yoobic/space_xyc_12345.csv')
print(result)





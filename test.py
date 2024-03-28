import csv

def writeCsv(text,rowInLoop):
    csv_file_path = 'recourses/url_linkedin.csv'

# Read existing data
    rows = []
    with open(csv_file_path, 'r', newline='', encoding='UTF8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        print(rows)

        # rows[rowInLoop][2] = text
    # Modify data for the first row
    # with open(csv_file_path, 'w', newline='', encoding='UTF8') as f:
    #         writer = csv.writer(f)
    #         writer.writerows(rows)

writeCsv("haha",6)

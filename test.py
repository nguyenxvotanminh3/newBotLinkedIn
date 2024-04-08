import csv
import pandas as pd
def writeCsv(text,rowInLoop):

    data = pd.read_csv('recourses/url_linkedin.csv')

    link = data['Message'][0]

    print("thisis " + link)

writeCsv(11,1)






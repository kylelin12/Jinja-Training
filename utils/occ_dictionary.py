import csv

# Converts the csv file to a dictionary 
# minus the 'Job Class' and 'Total' keys
def csv_to_float_dic():
    occ_list = csv.reader(open('./data/occupations.csv', 'r'))
    occ_dic = dict(occ_list)
    occ_dic.pop("Job Class")
    occ_dic_float = dict((key, float(value)) for key, value in occ_dic.iteritems())
    occ_dic_float.pop("Total")
    return occ_dic_float
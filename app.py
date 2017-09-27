from flask import Flask, render_template
import csv, random

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('index.html')

occ_list = csv.reader(open('occupations.csv', 'r'))
occ_dic = dict(occ_list)
occ_dic.pop("Job Class")
occ_dic_float = dict((key, float(value)) for key, value in occ_dic.iteritems())
occ_dic_float.pop("Total")

occ_list = csv.reader(open('occupations.csv', 'r'))
occ_dic_p = dict(occ_list)


def percent_chance(dictionary):
    while True:
        for key, value in dictionary.items(): # For loop that goes through each value for each key in the dictionary
            #print chance
            ran_num = random.random() * 99.8 # Generates a random number between [0, 1) * total chance.
            #print ran_num
            if ran_num <= value:
                #print key
                return key

@app.route("/occupations")
def occupy():
    return render_template('occupations.html', dic=occ_dic_float.items(), dicp=occ_dic_p.items(), rand=percent_chance(occ_dic_float))

if (__name__) == '__main__':
    app.debug = True
    app.run()
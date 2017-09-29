from flask import Flask, render_template
from utils import occ_rand_gen, occ_dictionary

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/occupations")
def occupy():
    occ_float_dic = occ_dictionary.dictionary()
    per_chance = occ_rand_gen.percent_chance(occ_float_dic)
    return render_template('occupations.html', dic=occ_float_dic.items(), rand=per_chance)

if (__name__) == '__main__':
    app.debug = True
    app.run()
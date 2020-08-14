# !Python3

from flask import Flask, request, render_template

application = app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) 

def rootpage ():
	username = ''
	height = ''
	weightlbs = ''
	weightkg = ''
	bmi = ''
	heightm = ''
	
	if request.method == 'POST' and 'username' in request.form:
		username = request.form.get('username')
		height = request.form.get('userheight')
		height = float(height)
		heightm = height/100
		weightlbs = request.form.get('userweight')
		weightlbs = float(weightlbs)
		weightkg = round(0.453592*weightlbs, 2)
		bmi = weightkg/(heightm**2)
		bmi = round(bmi, 2)
	return render_template("BMIindex.html", 
								username=username,
								height=height,
								weightlbs=weightlbs,
								weightkg=weightkg,
								bmi=bmi)




app.run()
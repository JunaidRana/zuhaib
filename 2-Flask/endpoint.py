from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/home')
def home():
	value = [2,3,4]
	return  render_template('index.html', data = value)

@app.route('/second')
def second():
    return  render_template('second.html')


@app.route('/api')
def api():
	data = {
    	"president": {
        	"name": "Zaphod Beeblebrox",
        	"species": "Betelgeusian"
    	}
	}
	json_string = json.dumps(data)
	return json_string

if __name__ == "__main__":
    
    app.run(debug=True, port=8080)
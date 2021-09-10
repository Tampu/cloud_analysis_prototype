from flask import Flask, render_template
import SC_bin
app = Flask(__name__)

@app.route("/")
def loginsignup():
    return render_template("loginsignup.html")

#@app.route("/")
#def sc_page():
#    return SC_bin.func()

@app.route("/spykingcircus")
def spykingcircus():
    render_template("sc.html")
    SC_bin.func()
    
    return 

@app.route("/home")
def home():
    return render_template("home.html")    

@app.route("/kilosort")
def kilosort():
    return render_template("kilosort.html")

#@app.route("/sc")
#def sc():
#    return render_template("sc.html") 

@app.route("/sspipe")
def sspipe():
    return render_template("sspipe.html")    
@app.route("/results")
def results():
    return render_template("results.html")       

if __name__=="__main__":
     #port = int(os.environ.get('PORT',5000))
     app.run(host='0.0.0.0')
    

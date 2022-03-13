from flask import Flask, render_template,request,redirect
import csv
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email},{subject},{message}")

def write_to_csv(data):
    with open('database.csv', 'a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_write = csv.writer(database2, delimiter=',',  quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email,subject,message])

@app.route("/submit_form",methods=['post','get'])
def submit_for():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return "thank you i will reach you shortly"
        except:
            return "something went wrong in database"
    else:
        return "something went wrong please try again later."


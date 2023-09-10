from flask import Flask, render_template, request, url_for, redirect
import csv

# app = Flask(__name__, template_folder='templates_2')
app = Flask(__name__)
print(__name__)


# @app.route("/")
# def hello_world():
#     return "<p>Hello Fabio Santana </p>"

# @app.route("/<username>/<int:post_id>")  # http://127.0.0.1:5000/bob/20
# def hello_world(username=None, post_id=None):
#     return render_template('templates_2/index.html', name=username, post_id=post_id)

@app.route("/index.html")
def my_home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong send again!'


if __name__ == "__main__":
        app.run()



# @app.route("/about.html")
# def about():
#     return render_template('about.html')


# @app.route("/works.html")
# def works():
#     return render_template('works.html')


# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')


# @app.route("/blog/2023/dogs")
# def blog2():
#     return "<p>This is my dog </p>"


# source web_server/bin/activate - at ~/Python_Udemy/project_files
# cd web_server
# make sure to run $ flask --app server run --debug
# to be able to refresh the page with changes made on the code
# if it's not working run $ lsof -i :5000 to find out the PID and kill them
# with $ kill PID (number) and restart the sever with $ flask --app server run --debug
# make sure after you run $ source web_server/bin/activate -> go inside the environment folder as well $ cd web_server
# deactivate - to get out of env.(web_server)
# pip3 freeze > requirements.txt

from flask import Flask, request, render_template, redirect, url_for
# from flask_cors import cross_origin


app = Flask(__name__)

# ##################################  MAIN HTML ROUTES ##############################################

@app.route("/")
# @cross_origin()
def home_route():
    return render_template("index.html")

@app.route("/about")
# @cross_origin()
def about_route():
    return render_template("about.html")

@app.route('/portfolio')
def portfolio_route():
    return render_template('portfolio.html')

@app.route("/contact")
# @cross_origin()
def contact_route():
    return render_template("contact.html")

# ##################################  /MAIN HTML ROUTES/ ##############################################

# ##################################  PROJECT HTML ROUTES ##############################################

@app.route('/cnn_mnist_project')
def cnn_mnist_route():
    return render_template('/projects_intro_html/cnn_mnist_project.html')

@app.route('/flight_fare_project')
def flight_fare_route():
    return render_template('/projects_intro_html/flight_predict_proj.html')

@app.route('/blogspot_project')
def blogspot_route():
    return render_template('/projects_intro_html/blogpost_proj.html')

@app.route('/space_invader_project')
def space_invader_route():
    return render_template('/projects_intro_html/space_invader_proj.html')

@app.route('/todolist_project')
def todolist_route():
    return render_template('/projects_intro_html/todolist_proj.html')

@app.route('/cnn_cifar_project')
def cnn_cifar_route():
    return render_template('/projects_intro_html/cnn_cifar_project.html')

# ##################################  /PROJECT HTML ROUTES/ ##############################################

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    app.run_server(debug=False)

from flask import Flask, render_template, request, redirect, url_for, current_app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db = SQLAlchemy(app)

# app.config['SERVER_NAME'] = 'prakharjain.org'

# Database Model


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(30), nullable=False, default="N/A")
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)

    def __repr__(self):
        return "Blog Post " + str(self.id)

# Handling Index Route


@app.route("/")
def index():
    return render_template("index.html")

# Handling Posts Route


@app.route("/posts", methods=["GET", "POST"])
def posts():
    if request.method == "POST":
        post_title = request.form["title"]
        post_content = request.form["content"]
        post_author = request.form["author"]
        new_post = BlogPost(
            title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect("/posts")
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template("posts.html", var_posts=all_posts)

# Handling New Posts Route


@app.route("/posts/new", methods=["GET", "POST"])
def new_post():
    if request.method == "POST":
        post_title = request.form["title"]
        post_content = request.form["content"]
        post_author = request.form["author"]
        new_post = BlogPost(
            title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect("/posts")
    else:
        return render_template("new_post.html")

# Handling Delete Route


@app.route("/posts/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect("/posts")

# Handling Post Edit Route


@app.route("/posts/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    post = BlogPost.query.get_or_404(id)

    if request.method == "POST":
        post.title = request.form["title"]
        post.author = request.form["author"]
        post.content = request.form["content"]
        db.session.commit()
        return redirect("/posts")
    else:
        return render_template("edit.html", var_post=post)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)  # , host="0.0.0.0"


# ###################################################################################################### Extra Commands for future use ########

# APP ROUTE FOR THE AUTOMATIC FORM SUBMISSION AND DATABASE DELETION

# @app.route("/timeout", methods = ["GET", "POST"])
# def db_delete():
#     all_data = BlogPost.query.filter_by(title = BlogPost.title).all()

#     print(all_data)
#     for data in all_data:
#         print(data)
#         db.session.delete(data)
#         db.session.commit()
#     return redirect("/posts")

# FUNCTION FOR THE FUNCTION RUN BY THREAD CREATION ON SET TIME INTERVAL AND DELETION OF DATABASE

# def delete_db():
#     print ("hello, world")
#     all_data = BlogPost.query.filter_by(title = BlogPost.title).all()

#     x = datetime.now().strftime('%H')

#     if (x == 15):
#         print(all_data)
#         for data in all_data:
#             print(data)
    # db.session.delete(data)
    # db.session.commit()

    # Timer(30.0, delete_db).start()

    # print(x)
    # '%H:%M:%S %Y-%m-%d'

# Timer(30.0, delete_db).start() # after 30 seconds, "hello, world" will be printed

# FUNCTION TO RUN APP WITHOUR REQUEST ROUTE

# def send_time():
#     x = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # with app.app_context() , app.test_request_context():
    #     url = url_for('index')
    #     context = {'time': x}
    #     print(x)
    #     return render_template('index.html', time_now = x)
    # return render_template("posts.html", time=x)

# send_time()

##########################################################################################################

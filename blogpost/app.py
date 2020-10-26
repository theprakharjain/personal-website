from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db = SQLAlchemy(app)

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

# Handling Post Delete Route


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
    app.run(debug=True, host="0.0.0.0")

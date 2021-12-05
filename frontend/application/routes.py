from werkzeug.wrappers import response
from application import app
from application.forms import CreatePostsForm, CreateCommentsForm
from flask import render_template, request, redirect, url_for, jsonify, json
import requests

backend_host = "todo-app_backend:5000"

@app.route('/')
@app.route('/home')
def home():
    all_posts = requests.get(f"http://{backend_host}/read/allPosts").json()
    app.logger.info(f"Posts: {all_posts}")
    return render_template('index.html', title="Home", all_posts=all_posts["posts"])

@app.route('/create/post', methods=['GET','POST'])
def create_post():
    form = CreatePostsForm()

    if request.method == "POST":
        response = requests.post(f"http://{backend_host}/create/post",json={"name": form.name.data})
        return redirect(url_for('home'))

    return render_template("create_post.html", title="Add a New post", form=form)

@app.route('/create/comment', methods=['GET','POST'])
def create_comment():
    form = CreateCommentsForm()

    json = requests.get(f"http://{backend_host}/read/allPosts").json()
    for post in json["posts"]:
        form.posts.choices.append((posts["id"], posts["name"]))

    if request.method == "POST":
        response = requests.post(
            f"http://{backend_host}/create/comment",
            json={
                "name": form.name.data,
                "content": form.content.data,
                "posts_id": form.posts_id.data
            }
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for("home"))

    return render_template("create_comment.html", title="Add a New Comment", form=form)

@app.route('/update/post/<int:id>', methods=['GET','POST'])
def update_post(id):
    form = postForm()
    post = requests.get(f"http://{backend_host}/read/post/{id}").json()

    if request.method == "POST":
        response = requests.put(f"http://{backend_host}/update/post/{id}",json={"name": form.name.data})
        return redirect(url_for('home'))

    return render_template('update_post.html', post=post, form=form)

@app.route('/delete/post/<int:id>')
def delete_post(id):
    response = requests.delete(f"http://{backend_host}/delete/post/{id}")
    return redirect(url_for('home'))

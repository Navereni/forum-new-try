from application import app, db
from application.models import Posts, Comments
from flask import render_template, request, redirect, url_for, Response, jsonify

@app.route('/create/post', methods=['POST'])
def create_post():
    package = request.json
    new_post = Posts(name=package["name"])
    db.session.add(new_post)
    db.session.commit()
    return Response(f"Added post with name {new_post.name}", mimetype='text/plain')

@app.route('/create/comment', methods=['POST'])
def create_comment():
    package = request.json
    new_comment = Comments(name=package["name"])
    db.session.add(new_comment)
    db.session.commit()
    return Response(f"Added post with name {new_post.name}", mimetype='text/plain')

@app.route('/read/allPosts', methods=['GET'])
def read_posts():
    all_posts = Posts.query.all()
    posts_dict = {"posts": []}
    for post in all_posts:
        comment = []
        for comment in post.comments:
            comments.append(
                {
                   "id": comment.id,
                   "comment": comment.content,
                   "comment_id": comment.comment_id,
                }
            )
        json["posts"].append(
            {
                "id": post.id,
                "title": post.title,
                "date_posted": post.date_posted,
            }
        )
    return jsonify(posts_dict)

@app.route('/read/post/<int:id>', methods=['GET'])
def read_post(id):
    post = Posts.query.get(id)
    posts_dict = {
                    "id": post.id,
                    "name": post.name,
                }
    return jsonify(posts_dict)


@app.route('/update/post/<int:id>', methods=['PUT'])
def update_post(id):
    package = request.json
    post = Posts.query.get(id)

    post.name = package['name']
    db.session.commit()
    return Response(f"Updated post (ID: {id}) with name {post.name}", mimetype='text/plain')

@app.route('/delete/post/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = Posts.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return Response(f"post (ID: {id}) has been DELETED!", mimetype='text/plain')

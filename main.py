from flask import Flask, render_template
import requests
from blog import Sleep

app = Flask(__name__)
response = requests.get("https://api.npoint.io/227f607cc2f4df477941").json()
data_lists = []
for i in response:
    data_object = Sleep(i["title"], i["subtitle"], i["date"], i["author"], i["id"], i["body"], i["image_url"])
    data_lists.append(data_object)


@app.route("/")
def home_page():
    return render_template("index.html", blog=data_lists)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:post_id>")
def post(post_id):
    aim_post = None
    aim_id = post_id
    for i in data_lists:
        if i.id == aim_id:
            aim_post = i
    title = aim_post.title
    subtitle = aim_post.subtitle
    author = aim_post.author
    date = aim_post.date
    body = aim_post.body
    img_url = aim_post.image_url
    return render_template("post.html", title=title, subtitle=subtitle, author=author, date=date,
                           body=body, url=img_url)


if __name__ == "__main__":
    app.run(debug=True)
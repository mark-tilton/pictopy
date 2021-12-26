from flask import Flask, render_template, request
import os
import uuid

app = Flask(__name__)

# Start by laying out the API inside this file, separate later.

# Return the landing page
@app.route("/", methods=["POST", "GET"])
def index():
    # Get all the saved images
    images = os.listdir("./static/images")

    if request.method == "POST":
        file = request.files["filename"]
        filename = str(uuid.uuid4())
        print(f"Uploading file: {filename}")
        file.save(f"./static/images/{filename}")
        images.append(filename)

    # Get images
    for image in images:
        print(image)
    return render_template("index.html", images=images)


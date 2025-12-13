from flask import Flask, render_template, request
from job_recommend import recommend_jobs

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        skills = request.form["skills"]
        education = request.form["education"]
        experience = request.form["experience"]

        jobs = recommend_jobs(skills, education, experience)

        return render_template(
            "result.html",
            jobs=jobs.to_dict(orient="records")
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

import os
from flask import Flask, render_template, request

# ✅ Force Flask to use correct static & templates folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, "static"),
    template_folder=os.path.join(BASE_DIR, "templates")
)

print("APP RUNNING FROM:", BASE_DIR)

# 🔥 FLAMES logic function+++++++++

def flames_result(boy, girl):
    num = len(boy) + len(girl)
    girl = list(girl)

    # Remove common letters
    for i in range(len(boy)):
        for j in range(len(girl)):
            if boy[i] == girl[j]:
                num -= 2
                girl[j] = "?"
                break

    # FLAMES elimination
    flames = list("FLAMES")
    index = 0

    while len(flames) > 1:
        index = (index + num - 1) % len(flames)
        flames.pop(index)

    result = flames[0]

    # Map result to text, image, background class
    if result == "F":
        return "FRIEND 🤝", "friend.jpg", "friend"
    elif result == "L":
        return "LOVE ❤️", "love.jpg", "love"
    elif result == "A":
        return "AFFECTION 💖", "affection.jpg", "affection"
    elif result == "M":
        return "MARRIAGE 💍", "marriage.jpg", "marriage"
    elif result == "E":
        return "ENEMY 😠", "enemy.jpg", "enemy"
    elif result == "S":
        return "SISTER 👩‍👦", "sister.jpg", "sister"


# 🌐 Flask route
@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    image = ""
    bg_class = ""

    if request.method == "POST":
        boy = request.form["name1"]
        girl = request.form["name2"]

        result, image, bg_class = flames_result(
            boy.lower().strip(),
            girl.lower().strip()
        )

    return render_template(
        "index.html",
        result=result,
        image=image,
        bg_class=bg_class
    )


if __name__ == "__main__":
    app.run(debug=True)



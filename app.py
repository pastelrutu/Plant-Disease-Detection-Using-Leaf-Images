from flask import Flask,render_template,request,redirect,url_for,session
from tensorflow.keras.models import load_model

import cv2
import numpy as np
import os
import pymysql

app=Flask(__name__)
app.secret_key="plant_disease_secret_key"
conn=pymysql.connect(host="localhost",user="root",password="root@241",database="plant_disease")

model_path="Plant_Disease_Model.keras"
model=load_model(model_path)

classes=[
"Apple___Apple_scab",
"Apple___Black_rot",
"Apple___Cedar_apple_rust",
"Apple___healthy",
"Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
"Corn_(maize)___Common_rust_",
"Corn_(maize)___Northern_Leaf_Blight",
"Corn_(maize)___healthy",
"Pepper__bell___Bacterial_spot",
"Pepper__bell___healthy",
"Potato___Early_blight",
"Potato___Late_blight",
"Potato___healthy",
"Tomato_Bacterial_spot",
"Tomato_Early_blight",
"Tomato_Late_blight",
"Tomato_Leaf_Mold",
"Tomato_Septoria_leaf_spot",
"Tomato_Spider_mites_Two_spotted_spider_mite",
"Tomato__Target_Spot",
"Tomato__Tomato_mosaic_virus",
"Tomato__Tomato_YellowLeaf__Curl_Virus",
"Tomato_healthy"
]
class_names={
    "Apple___Apple_scab":"Apple - Apple Scab",
    "Apple___Black_rot":"Apple - Black Rot",
    "Apple___Cedar_apple_rust":"Apple - Cedar Apple Rust",
    "Apple___healthy":"Apple - Healthy",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot":"Corn - Cercospora Leaf Spot",
    "Corn_(maize)___Common_rust_":"Corn - Common Rust",
    "Corn_(maize)___Northern_Leaf_Blight":"Corn - Northern Leaf Blight",
    "Corn_(maize)___healthy":"Corn - Healthy",
    "Pepper__bell___Bacterial_spot":"Bell Pepper - Bacterial Spot",
    "Pepper__bell___healthy":"Bell Pepper - Healthy",
    "Potato___Early_blight":"Potato - Early Blight",
    "Potato___Late_blight":"Potato - Late Blight",
    "Potato___healthy":"Potato - Healthy",
    "Tomato_Bacterial_spot":"Tomato - Bacterial Spot",
    "Tomato_Early_blight":"Tomato - Early Blight",
    "Tomato_Late_blight":"Tomato - Late Blight",
    "Tomato_Leaf_Mold":"Tomato - Leaf Mold",
    "Tomato_Septoria_leaf_spot":"Tomato - Septoria Leaf Spot",
    "Tomato_Spider_mites_Two_spotted_spider_mite":"Tomato - Spider Mites",
    "Tomato__Target_Spot":"Tomato - Target Spot",
    "Tomato__Tomato_mosaic_virus":"Tomato - Tomato Mosaic Virus",
    "Tomato__Tomato_YellowLeaf__Curl_Virus":"Tomato - Yellow Leaf Curl Virus",
    "Tomato_healthy":"Tomato - Healthy"
}

upload_folder="static/uploads"
os.makedirs(upload_folder,exist_ok=True)
app.config["Upload_folder"]=upload_folder

@app.route("/")
def home():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("index.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        password=request.form.get("password")
        hashed_password=password

        cursor=conn.cursor()
        cursor.execute("select * from users where email=%s",(email,))
        user=cursor.fetchone()
        if user:
            return render_template("register.html",error="Email already registered")

        cursor.execute("insert into users(name,email,password) values(%s,%s,%s)",(name,email,hashed_password))
        conn.commit()
        cursor.close()
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")
        cursor=conn.cursor()
        cursor.execute("select * from users where email=%s",(email,))
        user=cursor.fetchone()
        cursor.close()

        if user and user[3]==password :
            session["user_id"]=user[0]
            session["user_name"]=user[1]
            return redirect(url_for("home"))
        return render_template("login.html",error="Invalid email or password.")
    
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/predict",methods=["POST"])
def predict():
    if "user_id" not in session:
        return redirect(url_for("login"))

    file=request.files["image"]

    if file.filename=="":
        return redirect(url_for("home"))

    path=os.path.join(app.config["Upload_folder"],file.filename)
    file.save(path)

    image=cv2.imread(path)
    image=cv2.resize(image,(128,128))
    image=image/255.0
    image=np.expand_dims(image,axis=0)

    prediction=model.predict(image)
    predicted_class=np.argmax(prediction)
    confidence=float(np.max(prediction))*100
    result=class_names[classes[predicted_class]]
    cursor=conn.cursor()
    cursor.execute("insert into prediction_history(user_id,image,prediction,confidence)values (%s,%s,%s,%s)",(session["user_id"],os.path.basename(path),result,confidence))
    conn.commit()
    cursor.close()

    return render_template(
        "index.html",
        result=result,
        confidence=round(confidence,2),
        image=os.path.basename(path)
    )

@app.route("/history")
def history():
    if "user_id" not in session:
        return redirect(url_for("login"))

    cursor=conn.cursor()
    cursor.execute(
        "SELECT image,prediction,confidence,prediction_date FROM prediction_history WHERE user_id=%s ORDER BY prediction_date DESC",
        (session["user_id"],)
    )
    records=cursor.fetchall()
    cursor.close()

    return render_template("history.html",records=records)

@app.route("/about")
def about():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
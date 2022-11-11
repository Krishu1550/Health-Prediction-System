# This is a sample Python scriptfrom


from flask import Flask, render_template, request, url_for
import flask

from utilites import ValueDiabetes, ValueKidney, ValueHeart, ValueCancer, ValueLiver

app = Flask(__name__, template_folder='templates')


@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/diabetes")
def Diabete():
    return render_template('./Diabetes/page.html')
@app.route("/kidney")
def Kidney():
    return render_template('./Kidney/page.html')
@app.route("/heart")
def Heart():
    return render_template("./Heart/page.html")
@app.route("/cancer")
def Cancer():
    return render_template("./Cancer/page.html")
@app.route('/liver')
def Liver():
    return render_template("./Liver/page.html")


@app.route("/predictDiabetes",methods=["POST"])
def predictDiabetes():
    if request.method == "POST":
       #'Glucose','BloodPressure','SkinThickness','Insulin','Age','BMI'
       Glucose= request.form['Glucose']
       BloodPressure=request.form["BloodPressure"]
       SkinThickness=request.form["SkinThickness"]
       Insulin=request.form["Insulin"]
       BMI=request.form["BMI"]
       Age=request.form['Age']
       to_predict=[Glucose,BloodPressure,SkinThickness,Insulin,BMI,Age]
       result=ValueDiabetes(to_predict,6)

       if result==1:
           predict_text=flask.Markup(str("""<h3> Sorry you chances of getting the disease. Please consult the doctor immediately</h3>
           </br></br><h5> Make every meal well balanced.<h5></br><h5>Talk to your doctor about an exercise plan </h5>
           </br>"+"Keep an exercise schedule"+"</br>"+"Store insulin properly"""))

       else:
           predict_text =flask.Markup(""""<h3>No need to fear. You have no dangerous symptoms of the disease</h3>""")

    print(type(predict_text))
    return  render_template("./Diabetes/result.html", Prediction={predict_text} )

#cols = ['bp', 'sg', 'al', 'su', 'rbc', 'pc', 'pcc']
@app.route("/predictKidney",methods=["POST"])
def predictKidney():
    if request.method=="POST":
        bp=request.form["bp"]
        sg=request.form["sg"]
        al=request.form["al"]
        su=request.form["su"]
        rcb=request.form["rbc"]
        pc=request.form["pc"]
        pcc=request.form["pcc"]
        to_predict=[bp,sg,al,su,rcb,pc,pcc]
        if (len(to_predict) == 7):
            result = ValueKidney(to_predict, 7)

    if (int(result) == 1):
        prediction = "Sorry you chances of getting the disease. Please consult the doctor immediately"
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
    return (render_template("./Kidney/result.html", prediction_text=prediction))

#cols = ['cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang','age']
@app.route("/predictHeart",methods=["POST"])
def predictHeart():
    if request.method =="POST":
        cp=request.form["cp"]
        trestbps=request.form["trestbps"]
        chol=request.form["chol"]
        fbs=request.form["fbs"]
        restecg=request.form["restecg"]
        exang=request.form["exang"]
        thalach=request.form["thalach"]
        age=request.form["Age"]
        to_predict=[cp,trestbps,chol,fbs,restecg,thalach,exang,age]
        result=ValueHeart(to_predict,8)

    if (int(result) == 1):
        prediction = "Sorry you chances of getting the disease. Please consult the doctor immediately"
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
    return (render_template("./Heart/result.html", prediction_text=prediction))


#'Total_Bilirubin', 'Direct_Bilirubin','Alkaline_Phosphotase', 'Alamine_Aminotransferase', 'Total_Protiens', 'Albumin', 'Albumin_and_Globulin_Ratio'
@app.route("/predictLiver",methods=["POST"])
def predictLiver():
    if request.method=="POST":
        Total_Bilirubin=request.form["Total Bilirubin"]
        Direct_Bilirubin=request.form["Direct_Bilirubin"]
        Alkaline_Phosphotase=request.form["Alkaline_Phosphotase"]
        Alamine_Aminotransferase=request.form["Alamine_Aminotransferase"]
        Total_Protiens=request.form["Total_Protiens"]
        Albumin=request.form["Albumin"]
        Albumin_and_Globulin_Ratio=request.form["Albumin_and_Globulin_Ratio"]
        to_predict=[Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Total_Protiens
                    , Albumin, Albumin_and_Globulin_Ratio]
        result=ValueLiver(to_predict,7)
    if (int(result) == 1):
        prediction = "Sorry you chances of getting the disease. Please consult the doctor immediately"
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
    return (render_template("./Liver¸/result.html", prediction_text=prediction))





    #'concave points_mean','area_mean','radius_mean','perimeter_mean','concavity_mean'
@app.route("/predictCancer",methods=["POST"])
def predictCancer():
    if request.method=="POST":
        points_mean=request.form["concave points_mean"]
        area_mean=request.form["area_mean" ]
        radius_mean=request.form["radius_mean"]
        perimeter_mean=request.form["perimeter_mean"]
        concavity_mean=request.form["concavity_mean"]
        to_predict=[points_mean,area_mean,radius_mean,perimeter_mean,concavity_mean]
        result=ValueCancer(to_predict,5)
    if int(result)==1:
        prediction="Sorry you chances of getting the disease. Please consult the doctor immediately"
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
    return (render_template("./Cancer/result.html", prediction_text=prediction))


# Press ⌃R to execute it or replace it with your code.

# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


if __name__ == "__main__":
    app.run(debug=True)

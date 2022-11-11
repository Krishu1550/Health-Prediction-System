import pickle as pk
import numpy as np


#Cancer= pk.load(open("./Model/Cancer_Model.pkl","rb"))
#Heart= pk.load(open("./Model/Heart_Model.pkl","rb"))
#Kidney=pk.load(open("./Model/Kideny_Model.pkl","rb"))
#Liver= pk.load(open("./Model/Liver_Model.pkl","rb"))

def ValueDiabetes(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if (size == 6):
            Diabetes= pk.load(open("./Model/Diabete_Model.pkl","rb"))
            result = Diabetes.predict(to_predict)
    return result[0]

def ValueCancer(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if (size == 5):
            Cancer= pk.load(open("./Model/Cancer_Model.pkl","rb"))
            result = Cancer.predict(to_predict)
    return result[0]


def ValueKidney(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if (size == 7):
            Kidney=pk.load(open("./Model/Kideny_Model.pkl","rb"))
            result = Kidney.predict(to_predict)
    return result[0]

def ValueLiver(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if (size == 7):
            Liver= pk.load(open("./Model/Liver_Model.pkl","rb"))
            result = Liver.predict(to_predict)
    return result[0]

def ValueHeart(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if (size == 8):
            Heart= pk.load(open("./Model/Heart_Model.pkl","rb"))
            result = Heart.predict(to_predict)
    return result[0]
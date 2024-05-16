from django.shortcuts import render
import joblib
import pandas as pd

model = joblib.load('prediction/prediction-app/ml_housing_model.joblib')
scaler = joblib.load('prediction/prediction-app/ml_housing_scaler.joblib')

def HousingPricePrediction(request):
    
    output = ''
    if request.method == 'GET' and 'GrLivArea' in request.GET:
        oq = int(request.GET['OverallQual'])
        gla = int(request.GET['GrLivArea'])
        sc = request.GET['SaleCondition']
        # print(type(oq), type(gla), type(sc))
        num = list(scaler.transform(pd.DataFrame([[oq,gla]],columns=['OverallQual','GrLivArea']))[0])
        cat = list(map(lambda x: int(x==sc),['Abnorml','AdjLand','Alloca','Family','Normal','Partial']))
        num.extend(cat)
        output = '$'+str(int(model.predict([num])[0]))

    return render(request, 'index.html', {'result': output})
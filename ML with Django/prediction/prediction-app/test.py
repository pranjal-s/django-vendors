import joblib

model = joblib.load('ml_housing_model.joblib')

def main():

    # Test a prediction
    input = [[-0.07183611,  0.6863431 ,  0.        ,  0.        ,  0.        ,
         0.        ,  1.        ,  0.        ]]
    print(model.predict(input).astype(int)[0])

if __name__ == "__main__":
    main()
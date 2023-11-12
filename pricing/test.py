import joblib

model = joblib.load('ml_housing_model.joblib')
scaler = joblib.load('ml_housing_scaler.joblib')

def main():
    """
    Testing prediction/estimation of price for a real estate (SalePrice) given:
     - its overall quality (OverallQual)
     - its ground floor area (GrLivArea)
     - and its sale type/condition (SaleCondition)
    """

    # OverallQual = 7/10 and GrLivArea = 1717 sqft
    input_data = list(scaler.transform([[7,1717]])[0])

    # SaleCondition Choices
    #    Normal     : Normal Sale
    #    Abnorml    : Abnormal Sale -  trade, foreclosure, short sale
    #    AdjLand    : Adjoining Land Purchase
    #    Alloca     : Allocation - two linked properties with separate deeds, typically condo with a garage unit	
    #    Family     : Sale between family members
    #    Partial    : Home was not completed when last assessed (associated with New Homes)
    input_data.extend([0,0,0,0,1,0]) # choosing sale condition as family
    
    # Prediction of SalePrice
    output_value = model.predict([input_data]).astype(int)[0]
    if output_value > 210000 and output_value < 230000:
        print("ML prediction test passed.")

if __name__ == "__main__":
    main()
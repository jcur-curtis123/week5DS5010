'''
As provided in canvas - each boolean attribute looks at the record object and determines 

if the lambda is satisifed, the record is appended to the True list, otherwise to the False

Each partition is used to calculate it's impurity given the label "High Risk" or "Low Risk"
'''
PIVOTS = {
    "OnHypertensionMedication": lambda r: r.attrs["OnHypertensionMedication"] == True,
    "HasDiabetes": lambda r: r.attrs["HasDiabetes"] == True,
    "IsSmoker": lambda r: r.attrs["IsSmoker"] == True,
    "IsAfricanAmerican": lambda r: r.attrs["IsAfricanAmerican"] == True,
    "Gender": lambda r: r.attrs["Gender"] == "Female" # If gender returned "Male" - append to false group
}

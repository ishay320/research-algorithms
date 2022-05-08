import pandas as pd

# Load the csv
def read_csv():
    return pd.read_csv('national-budget.csv')

# Global var
df = read_csv()

# Get year to check and return the sum of education budget
def education_budget(year:int)->int:
    csv_filter = df[df["שנה"] == year]
    csv_filter = csv_filter[csv_filter["הוצאה/הכנסה"] == "הוצאה"]
    csv_filter = csv_filter[csv_filter["שם תכנית"].str.contains("חינוך")]
    csv_filter = csv_filter["הוצאה נטו"]
    return csv_filter.sum()

# Show the security budget ratio of specific year
def security_budget_ratio(year:int)->float:
    csv_filter = df[df["שנה"] == year]

    sum_of_all_year:float = csv_filter["הוצאה נטו"].sum()

    csv_filter = csv_filter[csv_filter["שם תחום"] == "בטחון"]
    sum_of_security_budget:float = csv_filter["הוצאה נטו"].sum()

    return sum_of_security_budget / sum_of_all_year

# The year with the largest budget
def largest_budget_year(office:str)->int:
    csv_filter = df[df["שם סעיף"] == office]

    max = (0,0)
    for df_year in df["שנה"].unique():
        frame = csv_filter[csv_filter["שנה"] == df_year]
        sum:float = frame["הוצאה נטו"].sum()
        if(max[0] < sum):
            max = (sum, df_year)
    return max[1]

# Show all the out after removing the income
def out_after_income()->float:
    frame =  df[df["הוצאה/הכנסה"] == "הוצאה"]
    out:float = frame["הוצאה נטו"].sum()
    frame =  df[df["הוצאה/הכנסה"] == "הכנסה"]
    income:float = frame["הוצאה נטו"].sum()
    return out + income

if __name__ == "__main__":
    print("education budget:     ", education_budget(2000))
    print("security budget ratio:", security_budget_ratio(1997))
    print("largest budget year:  ", largest_budget_year("משרד הבטחון"))
    print("out after income:     ", out_after_income())
    
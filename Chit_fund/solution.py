import pandas as pd

#read excel sheet
df = pd.read_excel('chit fund exercise.xlsx', header=1)

#Amount submit by each person in every month.
df["submitted amount by each in a month"] = df["Contribution"] - df["Amount returned to everyone in the group"]

#total amount submitted by each person
total_sbmt_amt_by_each_in_month = df["submitted amount by each in a month"].sum()

# return % for every participant
df['return'] = df['Net amount recd by Bid winner'] - total_sbmt_amt_by_each_in_month
df['return%'] = (df['return']/ total_sbmt_amt_by_each_in_month)*100

#Annualized  Return of the person who bids in the last month
annualized_Return_last_mnth = ((((1 + (df["return%"][24])/100)) ** (12/25)) - 1) * 100
print('1. Annualized  Return of the person who bids in the last month {}'.format(annualized_Return_last_mnth))


#Annualized Return of the person who bids in the first month
annualized_Return_1st_mnth = ((((1 + (df["return%"][0])/100)) ** (12/25)) - 1) * 100
print('2. Annualized Return of the person who bids in the first month is {}'.format(annualized_Return_1st_mnth))

#Return % for each month's bid winner
print(df["return%"])

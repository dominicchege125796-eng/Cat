name = input("Enter your Names \n")
limit = float(input("Enter your Fuliza Limit \n"))
salary = float(input("Enter yor Monthluy Salary \n"))
crb = str(input("Enter your CRB status(Listed or Not Listed) \n"))
desired = float(input("Enter your Desired Loan Amount \n"))
if limit >= 10000 :
    if salary >= 50000 and crb == "Not Listed":
        category = "Platinum Loan"
        loan = 1000000
        remark = "Excellent Borrower"
        rate = 10
elif 5000 <= limit < 10000 :
    if 30000 <= salary < 50000 and crb == "Not Listed":
        category = "Gold Loan"
        loan = 500000
        remark = "Reliable Borrower"
        rate = 13
elif limit < 5000 :
    if salary < 30000 and crb == "Not Listed":
        category = "Silver Loan"
        loan = 100000
        remark = "Fair Borrower"
        rate = 15
else:
    if crb == "Listed":
      remark = "CRB issue Detected"
      rate = 0
    else:
        remark = "Invalid"
interest = (rate/100)*desired
repayment = desired + interest


print("Applicant Name : ",name)
print("Fuliza Limit : ",limit)
print("Monthly Salary : ",salary)
print("CRB Status : ",crb )
print("Loan Category : ",category)
print("Maximum Loan Limit : ",loan)
print("Rate : ",rate)
print("Interest : ",interest)
print("Total Repayment : ",repayment)
print("Remarks : ",remark)
print("===THANK YOU!===")
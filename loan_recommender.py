print("---NIBS Microfinance Agency--- ")
print("====WELCOME=== ")
name = input("Enter your Names \n")
limit = float(input("Enter your Fuliza Limit \n"))
salary = float(input("Enter yor Monthluy Salary \n"))
crb = str(input("Enter your CRB status(Listed or Not Listed) \n"))
if limit >= 10000 :
    if salary >= 50000 and crb == "Not Listed":
        category = "Platinum Loan"
        loan = 1000000
        remark = "Excellent Borrower"
elif 5000 <= limit < 10000 :
    if 30000 <= salary < 50000 and crb == "Not Listed":
        category = "Gold Loan"
        loan = 500000
        remark = "Reliable Borrower"
elif limit < 5000 :
    if salary < 30000 and crb == "Not Listed":
        category = "Silver Loan"
        loan = 100000
        remark = "Fair Borrower"
else:
    if crb == "Listed":
      remark = "CRB issue Detected"
    else:
        remark = "Invalid"


print("Applicant Name : ",name)
print("Fuliza Limit : ",limit)
print("Monthly Salary : ",salary)
print("CRB Status : ",crb )
print("Loan Category : ",category)
print("Maximum Loan Limit : ",loan)
print("Remarks : ",remark)
print("===THANK YOU!===")
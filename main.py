#### Input from user the total hours worked and save as totalHours
##### calulate the number of overtimes hours as totalHours minus 40. Save as otHours.
##### calculate the number of regular hours as totalHours minus otHours. Save as regHours.
#### calculate the pay for regular hours as regHours * 20. Save as regPay
#### calculate total pay for OT hours as otHours * 30. save as otPay
#### if totalHours is greater than or equal to 40, then
print("Pay calculator will give your paycheck amount based on your pay rate and hours worked.  Overtime is calculated at time and a half.")

payRate = float(input('Enter your pay rate per hour: \n'))
totalHours = float(input('Enter the amount of hours worked: \n'))

if totalHours <= 40:
    totalPay = totalHours * payRate

else:
    otHours = totalHours - 40
    regHours = totalHours - otHours
    totalPay = (otHours * payRate * 1.5 ) + (regHours * payRate)
    # Calculating the federal tax

print('Your paycheck will be: $', "{:.2f}".format(totalPay))



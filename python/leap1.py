import datetime
cy=datetime.date.today().year
fy=int(input("enter the final year"))
if(fy<cy):
   print("final year must be greater than current year")
else:
   print(f"leap years from {cy} to {fy}")
   for year in range(cy,fy + 1):
     if( year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year)

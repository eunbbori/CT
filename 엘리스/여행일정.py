def main():
  inputDate = input()
  DateArr = inputDate.split('-')
  MM_31 = ['01','03','05','07','08','10','12']
  MM_30 = ['04','06','09','11']

  year = int(DateArr[0]) ;
  month = int(DateArr[1]) ;
  date = int(DateArr[2]) ; 
  
  trueMonth =  month >= 1 and month <= 12 # MM이 1이상 12이하인지 T/F
  YoonYear = ( year%4 == 0 and year %100 != 0) or ( year % 400 == 0 ) #윤년인지 아닌지 T/F


  if (trueMonth == False) or (DateArr[1] in MM_31 and date > 31) or (DateArr[1] in MM_30 and date > 30) or ( month == 2 and (YoonYear == True) and date > 29 ) or ( month == 2 and (YoonYear == False) and date > 28 ) or date<= 0 : 
      print(0)
  else : 
      print(1)


 

if __name__=="__main__":
    main()
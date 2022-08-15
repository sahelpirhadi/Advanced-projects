tarikh=input()
seprate=tarikh.split("/")
for i in range(0,len(seprate)):
    seprate[i]=int(seprate[i])
class sen:
    def __init__(self,seprate):
        self.seprate=seprate
    def mohasebe(self):
        if self.seprate[1]>12 or self.seprate[2]>31:
            print('WRONG')
        else:
            from datetime import datetime, date
            import datetime
            self.emrooz=str(datetime.date.today())
            self.seprate2=self.emrooz.split("-")
            for j in range(0,3):
               self.seprate2[j]=int(self.seprate2[j])
            t1=date(year=self.seprate[0],month=self.seprate[1],
                                      day=self.seprate[2])
            t2=date(year=self.seprate2[0],month=self.seprate2[1],
                                      day=self.seprate2[2])
            t3=t2-t1
            joda=str(t3).split(" ") 
            joda[0]=int(joda[0])
            final=joda[0]//365
            print(final)
man=sen(seprate)
man.mohasebe()

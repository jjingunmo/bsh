class Date(object):
    def __init__(self, year, month):
        self.year = year 
        self.month = month
        print('Date init ')

    def __del__(self):
        print('Date del ')

    def disp_Date(self):
        print('{}년{}월'.format(self.year, self.month))        


d1 = Date(2000, 12)
d2 = Date(2021, 3)
d1.disp_Date()
d2.disp_Date()



class Smart(Date):  ## Date class상속
    cnt = 0 ## class 변수 

    @staticmethod
    def get_cnt():
        return Smart.cnt

    @classmethod
    def get_cnt2(cls):
        return Smart.cnt
    

    def __init__(self, year, month, model, price): ## 생성자(constructor)
        Date.__init__(self, year, month)

        self.model = model 
        self.price = price 
        Smart.cnt += 1
        print(' Smart init ')

    def __del__(self):  ## 소멸자(destructor), 파괴자       
        Smart.cnt -= 1
        #print(' Smart del ')

    def __str__(self):
        return '{} {}'.format(self.model, self.price)
        #return "안녕하세요."

    def __eq__(self, other): ## 재정의,  overload  
        if self.model == other.model and self.price == other.price:
            return True
        else:
            return False

    ''' default 
    def __eq__(self, other):
        if id(self) == id(other):
            return True 
        else:
            return False
    '''

    def __add__(self, price):
        self.price += price 

    def __sub__(self, price):
        self.price -= price 

    def Disp(self):  ## 물밑으로 주소값이 전달된다. 주소를 저장하는 변수가 self, this       
        print(self.model, self.price)
        Date.disp_Date(self)

    def set_model(self, model):
        self.model = model

    def set_price(self, price):
        self.price = price

    def get_model(self):
        return self.model

    def get_price(self):
        return self.price


print(' 현재 객체수는 : ', Smart.get_cnt())
print(' 현재 객체수는 : ', Smart.get_cnt2())

s1 = Smart(2021, 2, '갤럭시20', 1200000)  ## 객체 생성, 인스턴스화
s2 = Smart(2020, 11, '아이폰12', 15000)

#s1.set_model('갤럭시21')
#s2.set_price(1500000)

print(s1)  ## __str__ method 호출 
print(s2)
'''
s1 + 30000  ## price 가격 인상 
s3 - 50000  ## price 다운 
'''
s1.Disp()
s2.Disp()


print(' 현재 객체수는 : ', Smart.get_cnt())
print(' 현재 객체수는 : ', s2.get_cnt2())
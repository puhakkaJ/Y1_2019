'''
Created on 28.10.2019

@author: jenni
'''

class StudentLoan:
    LOAN_PER_MONTH = 650
    
    def __init__(self, loan_id, holder, start_months):
        self.__id = loan_id
        self.__holder = holder
        self.__amount_left = start_months * StudentLoan.LOAN_PER_MONTH
        self.__amount_paid = 0
        self.__interest = 0.01
        self.__in_effect = True
        
    def get_id(self):
        return self.__id
    
    def get_holder(self):
        return self.__holder
    
    def get_amount_left(self):        
        return self.__amount_left 
    
    def get_amount_paid(self):
        return self.__amount_paid
    
    def get_interest(self):
        return self.__interest
    
    def is_in_effect(self):
        if self.__in_effect:
            return True
        else:
            return False
        
    def take_more_loan(self,months):    
        if self.__in_effect:
            self.__amount_left += months * StudentLoan.LOAN_PER_MONTH
        else:
            self.__amount_left = self.__amount_left
            
    def pay_loan(self,amount):    
        if self.__in_effect:
            jaljella = self.__amount_left
            self.__amount_left -= amount
            
            if self.__amount_left < 0:
                self.__amount_paid += jaljella
                self.__amount_left = 0
                
            else:
                self.__amount_paid += amount    
                
    def pay_loan_compensation(self,creds):            
        vuodet = creds/60
        summa = self.__amount_left - 2500
        maksimi = vuodet * 1240
        hyvitys = summa * 0.4
        if hyvitys > maksimi:
            self.pay_loan(maksimi)
        elif hyvitys > 0:
            self.pay_loan(hyvitys)
                
    def grow_yearly_interest(self):    
        if self.__in_effect:
            self.__amount_left = self.__amount_left * (self.__interest + 1)
            
    def terminate(self):
        if self.__amount_left == 0 and self.__in_effect:
            self.__in_effect = False
            return True
        else:
            return False
            
    def __str__(self):
        if self.__in_effect:
            mjono = "Student loan (in effect), loan id: {:s} \nLoan Holder: {:s} \nAmount left to pay: {:.2f} eur \nAmount paid: {:.2f} eur\n".format(self.__id,self.__holder,self.__amount_left,self.__amount_paid)
        elif not self.__in_effect: 
            mjono = "Student loan (outdated), loan id: {:s} \nLoan Holder: {:s} \nAmount left to pay: {:.2f} eur \nAmount paid: {:.2f} eur\n".format(self.__id,self.__holder,self.__amount_left,self.__amount_paid)
        
        return mjono
                
                    
            
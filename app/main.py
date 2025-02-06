from fastapi import FastAPI, HTTPException



class FunFactOfNumbers():
    def __init__(self, number):
        self.number = number
    
    def is_prime(self):
        n = self.number
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
            
        return True
        
    def is_odd(self):
        n = self.number
        if n % 2 != 0:
            return True
        return False
    
    def is_armstrong(self):
        n = self.number
        num_str = str(n)
        num_of_digits = len(num_str)
        
        armstrong_num = sum(int(num) ** num_of_digits for num in num_str)

    def is_perfect(self):
        n = self.number

        if n < 2:
            return False
        divisor = [1]
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                divisor.append(i)

                if i != n:
                    divisor.append(n // i)

        return sum(divisor) == n
    

    def is_even(self):
        n = self.number
        if n < 2:
            return False
        if n % 2 == 0:
            return True
        
        return False
    
    def properties(self):
        num_properties = []
        if self.is_armstrong() and self.is_odd():
            num_properties =  ["armstrong", "odd"]

        if self.is_armstrong() and self.is_even():
            num_properties =  ["armstrong", "even"]

        if not self.is_armstrong() and self.is_even():
            num_properties =  ["even"]

        if not self.is_armstrong() and self.is_odd():
            num_properties =  ["odd"]

        return num_properties


    def fun_fact(self):
        n = self.number
        n_to_string = str(n)
        number_of_digits = len(n_to_string)

        if self.is_armstrong():
            return f"{n} is an Armstrong number because the sum of each number raised to the power of the number of digit {number_of_digits} is equal to {n}"
        
        if self.is_perfect():
            return f"{n} is a perfect number because the sum of the divisors of the number is equal to the number which is {n}"
        
        if self.is_even() and not self.is_armstrong() and not self.is_perfect():
            return f"{n} is an even number because it is divisible by two"
        
        if self.is_odd() and not self.is_armstrong() and not self.is_perfect():
            return  f"{n} is an odd number because it is not divisible by two"
        

    def digit_sum(self):
        n = self.number
        n_to_list = str(n)

        return sum(int(i) for i in n_to_list)
        
app = FastAPI()

@app.get('/api/classify-number', status_code=200)
def home(number: int = 22):
    if not isinstance(number, int):
        data = {
            "number": "alphabet",
            "error": True
        }

        return HTTPException(status_code=400, detail=data)
    
    fun_fact = FunFactOfNumbers(number=number)
    
    data = {
        "number": number,
        "is_prime": fun_fact.is_prime(),
        "is_perfect": fun_fact.is_perfect(),
        "properties": fun_fact.properties(),
        "properties": fun_fact.properties(),
        "digit_sum": fun_fact.digit_sum(),
        "fun_fact": fun_fact.fun_fact()
    }

    return data
    

    
        



    
    
    
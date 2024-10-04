class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0  # To track $5 bills
        tens = 0   # To track $10 bills
        
        for bill in bills:
            if bill == 5:
                fives += 1  # Collect a $5 bill
            elif bill == 10:
                if fives > 0:
                    fives -= 1  # Use one $5 bill as change
                    tens += 1   # Collect a $10 bill
                else:
                    return False  # Can't give change if no $5 bill available
            elif bill == 20:
                if tens > 0 and fives > 0:
                    tens -= 1  # Use one $10 bill
                    fives -= 1  # Use one $5 bill
                elif fives >= 3:
                    fives -= 3  # Use three $5 bills if no $10 bill is available
                else:
                    return False  # Can't give change

        return True

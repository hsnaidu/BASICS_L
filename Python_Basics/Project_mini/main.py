# Complete Python

# Sloth Machine : Gambling Game : NOTE Do not Gamble


# Step 1 : we need user money & bet amount



def user_money():
    
    while True: # Run Conti..
        
        try:
            # Checking for int..
            amount  = int(input('Enter the number : '))
            if amount > 0:
                break
            else:
                # Checking for -ve val..
                print('Amountmust be greater than 0 ')
                amount  = int(input('Enter the number : '))
        
        # TypeError 
        except ValueError as t:
            print(t)
        
    return amount

print(user_money())
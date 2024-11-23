def myFunc():
    print('Hello World !!!')


# myFunc() : Un comment this and run the sample.py file and then comment this and run the sample.py file 

if __name__ == '__main__': # This is important 

    
    # So basically this makes sure what ever is inside this function dosent gets executed automatically when 
    # we call the from module import myFun  function
    
    print("we are running this code directly")
    myFunc()
    print(__name__)    
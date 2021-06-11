def search(L, n):

    for i in range(0,len(L)):
        
        if( L[i]== n ):
            
            print("Position =",[i])
            return True
            
        
   

List = [1,2,5,7,9,3,10]
n = 10

if search(List, n):
    print("Yes! Found")

else:
    print("Oops! Not Found")
        

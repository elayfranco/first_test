from number import comp,simp #main function runing every thing
import col

def main ():
    print ( "add ="  ,simp.adding (5,6)) 
    print ( "sub =" ,simp.subtracting(10,5))

    print(comp.ispal(113311))
    print ("sum =",comp.sumofdigits(123451))

    br1 = [1,2,3,4,5]
    br2 = ["a","b","c","d","e"]
    print(col.myzip(br1,br2))
    
    
    

if __name__ == "__main__":
    main()


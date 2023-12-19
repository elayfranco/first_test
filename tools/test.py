from number import comp,simp
import col

 #testing all func in the modules
 
 #simp
print ( "add ="  ,simp.adding (5,6)) 
print ( "sub =" ,simp.subtracting(10,5))

#comp
print(comp.ispal(113311))
print ("sum =",comp.sumofdigits(123451))

#col
br1 = [1,2,3,4,5]
br2 = ["a","b","c","d","e"]
print(col.myzip(br1,br2))


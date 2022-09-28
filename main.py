print("Favorite Tv Show")
print()
fave_tv = input("Whats is your favorite tv show?:")


if fave_tv == "Power":
    print("Mines too")
    
    favecharacter = input("who is your favorite character?:")
   
    if favecharacter == "Kanan":
       print("Mines too")
       input("What do you like about Kanan?:")
       print("Okay, i see why you like that character")
       input("Whats Kanan birth city at?:")
    
    if favecharacter == "Ghost":
      print("Okay, now your talking")
      input("What do you like about Ghost?:")
      input("Do you think he is still alive?:")
      print("I think so, because ghost lives forever")

    else: 
      print("Im not mad at that answer")
    
      
elif fave_tv == "Sistas":
    print("ugh, why")
    print("I guess, my girlfriend watches that show.")
else:
  print("Thats cool")
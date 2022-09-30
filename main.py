print("Favorite Tv Show")
print()
fave_tv = input("Whats is your favorite tv show?:")


if fave_tv == "Power":
    print("Thats the best show on Tv right now")
    
    favecharacter = input("who is your favorite character on Power series?:")
    if favecharacter == "Kanan":
       print("Mines too")
       input("What do you like about Kanan?:")
       print("Okay, i see why you like that character")
    birth_place = input("What city was Kanan Born?:")
    if birth_place == "NewYork":
      print("Correct")
    else:
      print("try again")
    
    
    if favecharacter == "Ghost":
      print("Okay, now yor talking")
      input("What do you like about Ghost?:")
      input("Do you think he is still alive?:")
      print("I think so, because ghost lives forever")

    
      
elif fave_tv == "Sistas":
    print("ugh, why")
    print("I guess, my girlfriend watches that show.")
else:
  print("Thats cool")
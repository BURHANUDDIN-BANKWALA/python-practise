## match or also called switch in other languages
## case _: represents a default case
## also to remember there must be a space before the underscore( _) in default case 
## every case needs its own colon :
## unlike c lang the case executes where the value is true further execution is stopped

clas=input("enter your class ")

match clas :
    case "first":
     print("1")

    case "second":
    
     print("2")

    case _: 
     print("none")
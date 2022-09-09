def drawtree(number):
    for x in range(number):
        noofstars = x
        stars = "*" * noofstars
        emptyspace = " " * (number - x)
        
        print(emptyspace + stars + "*" + stars)
        
drawtree(7)
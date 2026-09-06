# a simple question about determining the apps and oranges that falls in sam's house 
def countApplesAndOranges(s, t, a, b, apples,oranges):
    apple_count = 0      #s = start point, t = end point, a = apple tree location, b = orange tree                      #t = end p
    for d in apples:
        if s <= a + d <= t:
            apple_count +=1
    orange_count = 0
    for d in oranges:
        if s <= b+d <=t:
            orange_count += 1
    print (apple_count)
    print(orange_count)
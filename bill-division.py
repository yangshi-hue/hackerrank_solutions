def bonAppetit(bill, k, b):
    total = sum(bill)

    anna_share = (total - bill[k]) //2

    if b == anna_share:
        print("Bon Appetit")
    else:
        print(b - anna_share)
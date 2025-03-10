# list of all the hoomans
hoomans = [
    {
        'name': 'Rebbi', 
        'desc': 'pho no. 17 + shared spring rolls', 
        'base price': 17.95 + 4.475
    },
        {
        'name': 'Kelly', 
        'desc': 'vermicelli + shared spring rolls', 
        'base price': 19.95 + 4.475
    },
        {
        'name': 'Carolyn', 
        'desc': 'pho no. 18', 
        'base price': 17.95
    },
        {
        'name': 'Sophia', 
        'desc': 'pho no. 17', 
        'base price': 17.95
    },
        {
        'name': 'Emma', 
        'desc': 'pho no. 17', 
        'base price': 17.95
    },
]

TIP = 1.08
PAYER = 'Carolyn'
SANITY_CHECK_TARGET = 122.89

# apply tip and tax to base price
def calculate_payment(base_price: float) -> float:
    tax = 1.13
    tip = TIP
    return base_price * tip * tax


if __name__ == '__main__':
    sanity_check = 0
    sanity_check_target = SANITY_CHECK_TARGET
    for hooman in hoomans:
        print(
            hooman['name'] , 'committed the crime: ' + 
            hooman['desc'] + '. \n\t' + 'amount owed: $' + str(round(calculate_payment(hooman['base price']), 2)) + '\n'
            )
        sanity_check += calculate_payment(hooman['base price'])
    
    print("sum of above totals: " + str(round(sanity_check, 2)))
    print(f"how much {PAYER} paid: " + str(sanity_check_target))

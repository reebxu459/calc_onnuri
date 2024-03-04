# list of all the hoomans
hoomans = [
    {
        'name': 'rebbi', 
        'desc': 'split teok with rosanne. split 2 half chickens with austin kelly rosanne eric nick', 
        'base price': (16.99 / 2) + ((2 * 21.99) / 6)
    },
    {
        'name': 'rosanne', 
        'desc': 'split teok with rebbi. split 2 half chickens with austin kelly rebbi eric nick', 
        'base price': (16.99 / 2) + ((2 * 21.99) / 6)
    },
    {
        'name': 'eric', 
        'desc': 'split 2 half chickens with austin kelly rebbi rosanne nick', 
        'base price': (2 * 21.99) / 6
    },
    {
        'name': 'nick', 
        'desc': 'split 2 half chickens with austin kelly rebbi rosanne eric', 
        'base price': (2 * 21.99) / 6
    },
    {
        'name': 'austin', 
        'desc': 'covered the kimchijeon. split 2 half chickens with nick kelly rebbi rosanne eric', 
        'base price': 16.99 + (2 * 21.99) / 6
    },
    {
        'name': 'kelly', 
        'desc': 'split 2 half chickens with austin eric rebbi rosanne nick', 
        'base price': (2 * 21.99) / 6
    },
    {
        'name': 'becky', 
        'desc': 'split a whole chicken with steven and cynthia', 
        'base price': 32.99 / 3
    },
    {
        'name': 'steven', 
        'desc': 'split a whole chicken with becky and cynthia', 
        'base price': 32.99 / 3
    },
    {
        'name': 'cynthia', 
        'desc': 'split a whole chicken with steven and becky', 
        'base price': 32.99 / 3
    },
    {
        'name': 'daniel', 
        'desc': 'ordered kimchi fried rice', 
        'base price': 13.99
    },
    {
        'name': 'bryan', 
        'desc': 'ordered yaki udon', 
        'base price': 15.99
    },
    {
        'name': 'meilin', 
        'desc': 'ordered soon tofu stew', 
        'base price': 14.99
    },
    {
        'name': 'felix', 
        'desc': 'ordered bibimbap', 
        'base price': 15.99
    },
]

# apply tip, tax, and amount to base price to cover andrew's food
def calculate_payment(base_price: float) -> float:
    tax = 1.13
    tip = 1.15
    pay_for_andrew = 1.40
    return base_price * tip * tax + pay_for_andrew


if __name__ == '__main__':
    sanity_check = 0
    sanity_check_target = 241.58
    for hooman in hoomans:
        print(hooman['name'] , 'committed the crime: ' + hooman['desc'] + '. \n\t' + 'amount owed: $' + str(round(calculate_payment(hooman['base price']), 2)) + '\n')
        sanity_check += calculate_payment(hooman['base price'])
    
    print("sum of above totals: " + str(round(sanity_check, 2)))
    print("how much rebbi paid: " + str(sanity_check_target))

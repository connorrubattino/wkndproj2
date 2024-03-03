def shopping_cart():
    cart = {}
    while True:
        entry = input('What would you like to do? Please type "add", "remove", "show", or "finish"').lower()
        if entry == 'add':
            name = input('What would you like to add to your cart?').title()
            # price = float(input(f'How much does one {name} cost? - Please enter numerical value (i.e. \'2.50\')')) -- only want to ask for price if item not yet in cart
            while True:
                quantity_input = input(f"How many {name}'s would you like to add? - Please enter numerical value (i.e. '5' not 'five')")
                if quantity_input.isdigit():
                    quantity = int(quantity_input)
                    break
                else:
                    print('Ivalid entry - please input numerical digit value')
            if name not in cart:
                price = float(input(f'How much does one {name} cost? - Please enter numerical value (i.e. \'2.50\')'))
                cart[name] = {'quantity': quantity, 'price': price}
            else:
                cart[name]['quantity'] += quantity
            print(f'{quantity} {name}\'s have been added to your cart')
        elif entry == 'remove':
            removed_item = input('Which item would you like to remove?').title()
            if removed_item not in cart:
                print(f'{removed_item} not found in your cart')
            else:
                remove_qty = int(input(f'How many {removed_item}\'s would you like to remove?'))
                if remove_qty >= cart[removed_item]['quantity']:
                    del cart[removed_item]
                    print(f'All {removed_item}\'s removed from cart!')
                else:
                    cart[removed_item]['quantity'] -= remove_qty
                    print(f'We have removed {remove_qty} {removed_item}\'s from your cart!')
        elif entry == 'show':
            if not cart:
                print('Your cart is empty')
            else:
                total = 0
                print('Current Cart:')
                for name, details in cart.items():
                    print(f"\t{name} X {details['quantity']} @ ${details['price']}")
                    total += details['quantity'] * details['price']
                print(f'\nYour current total cost is: ${total:.2f}')
        elif entry == 'finish':
            if not cart:
                print('No items in cart.')      
            else:
                print('Hope you found everything you need!')
                print('Your reciept:')
                total = 0
                for name, details in cart.items():
                    total += details['quantity'] * details['price']
                    print(f"\t{name} X {details['quantity']} @ ${details['price']}")
            print(f'Your grand total today is: ${total:.2f}')
            print('Thank you for shopping with us today and we hope to see you soon :)')
            break
        else:
            print('Invalid selection')
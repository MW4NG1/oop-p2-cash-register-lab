#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        """
        Initializes the CashRegister. The discount attribute uses a setter 
        property to handle validation automatically upon creation.
        """
        self.discount = discount
        self.total = 0
        self.items = []
        # Keeps track of each added transaction: (total_price_added, quantity_added)
        self.previous_transactions = []

    @property
    def discount(self):
        """Getter for discount."""
        return self._discount

    @discount.setter
    def discount(self, value):
        """
        Setter for discount. Validates that the discount is an integer 
        and between 0 and 100 inclusive.
        """
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            # Default to 0 if an invalid value is provided
            self._discount = 0

    def add_item(self, item, price, quantity=1):
        """
        Adds item(s) to the register, updates total price, 
        and stores transaction history for voiding.
        """
        # Add the item name to the items list 'quantity' times
        for _ in range(quantity):
            self.items.append(item)
        
        # Calculate subtotal for this addition
        added_cost = price * quantity
        self.total += added_cost

        # Record this transaction so we can void it if needed
        self.previous_transactions.append({
            'cost': added_cost,
            'quantity': quantity
        })

    def apply_discount(self):
        """
        Applies percentage discount to total if discount > 0,
        otherwise prints an error message.
        """
        if self.discount > 0:
            # Calculate total after percentage discount
            self.total -= self.total * (self.discount / 100)
            
            # Format output (handles integer display if total is whole number)
            formatted_total = int(self.total) if self.total.is_integer() else self.total
            print(f"After the discount, the total comes to ${formatted_total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """
        Reverts the last added transaction by subtracting its cost
        and removing the added items from self.items.
        """
        if self.previous_transactions:
            # Pop the most recent transaction history entry
            last_tx = self.previous_transactions.pop()
            
            # Subtract cost from running total
            self.total -= last_tx['cost']
            
            # Remove the last N items from the list based on quantity
            for _ in range(last_tx['quantity']):
                if self.items:
                    self.items.pop()

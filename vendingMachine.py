class VendingMachine:
    def __init__(self):
        # Initialize inventory and balance
        self.inventory = {
            "A1": {"item": "Coke", "price": 1.25, "quantity": 10},
            "A2": {"item": "Pepsi", "price": 1.50, "quantity": 10},
            "B1": {"item": "Chips", "price": 1.00, "quantity": 10},
            "C1": {"item": "Candy", "price": 0.75, "quantity": 10},
            # Add other slots as necessary
        }
        self.balance = 0.0

    def add_money(self, amount):
        """Add money to the vending machine."""
        if amount <= 0:
            return "Invalid amount. Please insert a positive value."
        self.balance += amount
        return f"Current balance: ${self.balance:.2f}"

    def select_item(self, slot_code):
        """Select an item based on the slot code."""
        if slot_code not in self.inventory:
            return "Invalid slot code. Please try again."

        item = self.inventory[slot_code]
        if item["quantity"] == 0:
            return f"{item['item']} is out of stock."

        if self.balance < item["price"]:
            return f"Insufficient balance. {item['item']} costs ${item['price']:.2f}."

        # Deduct the price and dispense the item
        self.balance -= item["price"]
        item["quantity"] -= 1
        change = self.balance
        self.balance = 0  # Reset balance after purchase
        return f"Vending {item['item']}. Change: ${change:.2f}"

    def check_inventory(self):
        """Return the current inventory status."""
        inventory_status = {}
        for slot, details in self.inventory.items():
            inventory_status[slot] = f"{details['item']}: {details['quantity']} left"
        return inventory_status

    def restock(self, slot_code, quantity):
        """Restock a specific slot with additional items."""
        if slot_code not in self.inventory:
            return "Invalid slot code. Cannot restock."
        if quantity <= 0:
            return "Invalid quantity. Please provide a positive value."

        self.inventory[slot_code]["quantity"] += quantity
        return f"Restocked {self.inventory[slot_code]['item']} to {self.inventory[slot_code]['quantity']} units."

    def return_balance(self):
        """Return the remaining balance."""
        change = self.balance
        self.balance = 0
        return f"Returning ${change:.2f}."

# Example usage
if __name__ == "__main__":
    vm = VendingMachine()

    # Add money
    print(vm.add_money(2.00))

    # Select item
    print(vm.select_item("A1"))

    # Check inventory
    print(vm.check_inventory())

    # Restock
    print(vm.restock("A1", 5))

    # Return balance
    print(vm.return_balance())

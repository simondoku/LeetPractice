import unittest

class VendingMachine:
    def __init__(self):
        self.items = {}  # Dictionary to store items and their details {item_name: (price, quantity)}
        self.balance = 0  # Tracks the money added to the machine

    def add_item(self, item_name, price, quantity):
        if item_name in self.items:
            current_price, current_quantity = self.items[item_name]
            self.items[item_name] = (price, current_quantity + quantity)
        else:
            self.items[item_name] = (price, quantity)
        print(f"{item_name} restocked. New quantity: {self.items[item_name][1]}")

    def display_items(self):
        print("Available items:")
        for item_name, (price, quantity) in self.items.items():
            if quantity > 0:
                print(f"- {item_name}: ${price} (Quantity: {quantity})")
            else:
                print(f"- {item_name}: Out of stock")

    def add_money(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} added. Current balance: ${self.balance}")
        else:
            print("Invalid amount. Please add a positive value.")

    def buy_item(self, item_name):
        if item_name not in self.items:
            print(f"{item_name} is not available in the vending machine.")
            return

        price, quantity = self.items[item_name]

        if quantity <= 0:
            print(f"{item_name} is out of stock.")
        elif self.balance < price:
            print(f"Insufficient balance. {item_name} costs ${price}, but your balance is ${self.balance}.")
        else:
            self.balance -= price
            self.items[item_name] = (price, quantity - 1)
            print(f"You bought {item_name} for ${price}. Remaining balance: ${self.balance}")

    def return_change(self):
        print(f"Returning ${self.balance} in change.")
        self.balance = 0

class TestVendingMachine(unittest.TestCase):
    def setUp(self):
        self.vm = VendingMachine()

    def test_add_item(self):
        self.vm.add_item("Soda", 1.50, 10)
        self.assertIn("Soda", self.vm.items)
        self.assertEqual(self.vm.items["Soda"], (1.50, 10))

    def test_add_money(self):
        self.vm.add_money(5)
        self.assertEqual(self.vm.balance, 5)
        self.vm.add_money(-1)
        self.assertEqual(self.vm.balance, 5)  # Balance should not change with invalid amount

    def test_buy_item(self):
        self.vm.add_item("Soda", 1.50, 10)
        self.vm.add_money(5)
        self.vm.buy_item("Soda")
        self.assertEqual(self.vm.balance, 3.50)
        self.assertEqual(self.vm.items["Soda"], (1.50, 9))

    def test_buy_item_insufficient_balance(self):
        self.vm.add_item("Soda", 1.50, 10)
        self.vm.add_money(1)
        self.vm.buy_item("Soda")
        self.assertEqual(self.vm.balance, 1)
        self.assertEqual(self.vm.items["Soda"], (1.50, 10))

    def test_buy_item_out_of_stock(self):
        self.vm.add_item("Soda", 1.50, 0)
        self.vm.add_money(5)
        self.vm.buy_item("Soda")
        self.assertEqual(self.vm.balance, 5)
        self.assertEqual(self.vm.items["Soda"], (1.50, 0))

    def test_return_change(self):
        self.vm.add_money(5)
        self.vm.return_change()
        self.assertEqual(self.vm.balance, 0)

if __name__ == '__main__':
    unittest.main()
"""
Inventory Management System Module
Handles addition, removal, and tracking of stock items.
"""

import json
from datetime import datetime
import ast


class InventorySystem:
    """Class-based inventory management system."""

    def __init__(self, file_path="inventory.json"):
        """Initialize inventory system with optional file path."""
        self.file_path = file_path
        self.stock_data = {}
        self.logs = []

    def add_item(self, item="default", qty=0):
        """Add an item and quantity to the inventory."""
        if not isinstance(item, str) or not isinstance(qty, (int, float)):
            print("Invalid item name or quantity type.")
            return

        self.stock_data[item] = self.stock_data.get(item, 0) + qty
        self.logs.append(f"{datetime.now()}: Added {qty} of {item}")

    def remove_item(self, item, qty):
        """
        Remove quantity of an item from stock_data. Deletes item if qty <= 0.
        """
        try:
            self.stock_data[item] -= qty
            if self.stock_data[item] <= 0:
                del self.stock_data[item]
            self.logs.append(f"{datetime.now()}: Removed {qty} of {item}")
        except KeyError:
            print(f"Item '{item}' not found in inventory.")

    def get_qty(self, item):
        """Retrieve the quantity of a given item."""
        return self.stock_data.get(item, 0)

    def load_data(self):
        """Load stock data from a JSON file."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                self.stock_data = json.load(f)
        except FileNotFoundError:
            print(f"File {self.file_path} not found. Starting empty...")
            self.stock_data = {}
        except json.JSONDecodeError:
            print("Error decoding JSON file.")
            self.stock_data = {}

    def save_data(self):
        """Save the current stock_data to a JSON file."""
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(self.stock_data, f, indent=4)
        except FileNotFoundError:
            print(f"Error : File {self.file_path} not Found")

    def print_data(self):
        """Print all items and their quantities."""
        print("Items Report:")
        for item, qty in self.stock_data.items():
            print(f"{item} -> {qty}")

    def check_low_items(self, threshold=5):
        """
        Return a list of items whose quantities fall below the given threshold.
        """
        result = [
            item for item, qty in self.stock_data.items()
            if qty < threshold
            ]
        return result


def main():
    """Demonstrate inventory system operations."""
    inv = InventorySystem()

    inv.add_item("apple", 10)
    inv.add_item("banana", -2)
    inv.add_item(123, "ten")  # invalid types handled using isinstance()
    inv.remove_item("apple", 3)
    inv.remove_item("orange", 1)
    print(f"Apple stock: {inv.get_qty('apple')}")
    print(f"Low items: {inv.check_low_items()}")
    inv.save_data()
    inv.load_data()
    inv.print_data()

    try:
        expression = "['eval used safely']"
        safe_result = ast.literal_eval(expression)
        print(safe_result)
    except (SyntaxError, ValueError):
        print("Unsafe expression detected — not evaluated.")


if __name__ == "__main__":
    main()

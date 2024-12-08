import unittest
from lorequest.inventory import Inventory


class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()

    def test_add_item(self):
        self.inventory.add_item("Potion of Healing", 3)
        self.assertEqual(self.inventory.items["Potion of Healing"], 3)

    def test_remove_item(self):
        self.inventory.add_item("Legendary Sword", 1)
        self.assertTrue(self.inventory.remove_item("Legendary Sword"))
        self.assertNotIn("Legendary Sword", self.inventory.items)

    def test_remove_item_insufficient_quantity(self):
        self.inventory.add_item("Bag of Gold Coins", 2)
        self.assertFalse(self.inventory.remove_item("Bag of Gold Coins", 3))

    def test_view_inventory_empty(self):
        self.assertEqual(self.inventory.view_inventory(), "Your inventory is empty.")

    def test_view_inventory_with_items(self):
        self.inventory.add_item("Magic Staff", 1)
        self.inventory.add_item("Ancient Amulet", 2)
        expected_output = "Magic Staff: 1\nAncient Amulet: 2"
        self.assertEqual(self.inventory.view_inventory(), expected_output)


if __name__ == "__main__":
    unittest.main()

# Hotel-Menu-Ordering-System-python-project
# Description:
A basic text-based restaurant menu where users can order food items. Prices are predefined in a dictionary. The user can select one or two items, and the program calculates the total bill.

# Key Concepts:

* Dictionary for menu storage
* Conditional logic
* Basic input handling and total computation

# Improvement Suggestion:

* Fix the bug: order_total += menu[item1] is incorrectly used for both items. It should be menu[item2] for the second item.
* Enhance with a loop to allow multiple orders and support invalid input handling.

#!/usr/bin/env python3
"""
Dan's Pizza and Sub Shop — command-line ordering system.
"""
import sys


def valid_input(question, valid_answers):
    while True:
        answer = input(question)
        if answer in valid_answers:
            return answer
        print("Please enter one of the valid values: " + str(valid_answers))


class Pizza:
    TOPPINGS = sorted([
        "pepperoni", "extra cheese", "mushroom", "sausage",
        "garlic", "olives", "bacon", "ham", "prosciutto", "basil",
    ])

    def __init__(self, toppings):
        self.toppings = toppings

    def pretty_name(self):
        if not self.toppings:
            return "cheese pizza"
        return " and ".join(self.toppings) + " pizza"

    def cost(self):
        count = len(self.toppings)
        if count == 0:
            return 10
        elif count <= 2:
            return 12
        return 16

    @classmethod
    def topping_list(cls):
        return "\nAvailable toppings: " + ", ".join(cls.TOPPINGS) + "\n"


class Sub:
    PRICES = {
        "Italian": 12,
        "Cuban": 12,
        "Turkey": 11,
        "Chicken": 11,
        "Meatball": 10,
        "Club Sub": 10,
        "Tuna": 10,
        "Grilled Cheese": 8,
    }

    def __init__(self, sub):
        self.sub = sub

    def pretty_name(self):
        return self.sub + " sandwich"

    def cost(self):
        return self.PRICES[self.sub]

    @classmethod
    def sub_list(cls):
        return "\nAvailable subs: " + ", ".join(sorted(cls.PRICES)) + "\n"


def main():
    print("Welcome to Dan's Pizza and Sub Shop!")

    if valid_input("Would you like to place an order? ", ["yes", "no"]) == "no":
        sys.exit(0)

    items = []

    while True:
        item = valid_input("What item would you like? ", ["pizza", "sub"])

        if item == "pizza":
            print(Pizza.topping_list())
            toppings_ordered = []
            while True:
                choice = input("Add a topping (or 'none'/'quit' when done): ").strip().lower()
                if choice in ("quit", "none"):
                    break
                if choice in Pizza.TOPPINGS:
                    toppings_ordered.append(choice)
                else:
                    print("Please enter a valid topping.")
            p = Pizza(toppings_ordered)
            items.append(p)
            print(f"\nYou have successfully ordered a {p.pretty_name()}\n")

        elif item == "sub":
            print(Sub.sub_list())
            while True:
                choice = input("What sub would you like to order? ").strip()
                match = next((s for s in Sub.PRICES if s.lower() == choice.lower()), None)
                if match:
                    s = Sub(match)
                    items.append(s)
                    print(f"You have ordered: {s.pretty_name()}\n")
                    break
                print("Please enter a sub from the list.")

        if valid_input("Would you like to order another item? ", ["yes", "no"]) == "no":
            break

    print("\nHere is a summary of your order:")
    total_cost = 0
    for item in items:
        print(f"  {item.pretty_name()}: ${item.cost()}")
        total_cost += item.cost()

    tax = round(total_cost * 0.07, 2)
    final_cost = round(total_cost + tax, 2)
    print(f"\nSubtotal: ${total_cost}")
    print(f"Tax (7%): ${tax}")
    print(f"Total:    ${final_cost}")
    print("\nYour order will be ready in about 30 minutes. Thank you!")


if __name__ == "__main__":
    main()

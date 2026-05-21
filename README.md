# Dan's Pizza and Sub Shop

A command-line ordering system for pizzas and subs, written in Python.

## Usage

```bash
python3 pizza_sub_project.py
```

Follow the prompts to build your order. You can add multiple items before checking out.

## Pricing

**Pizza**
| Toppings | Price |
|----------|-------|
| 0 (cheese only) | $10 |
| 1–2 toppings | $12 |
| 3+ toppings | $16 |

**Subs**
| Sub | Price |
|-----|-------|
| Italian, Cuban | $12 |
| Turkey, Chicken | $11 |
| Meatball, Club Sub, Tuna | $10 |
| Grilled Cheese | $8 |

A 7% tax is applied to the final total.

## Available Toppings

bacon, basil, extra cheese, garlic, ham, mushroom, olives, pepperoni, prosciutto, sausage

Type `none` or `quit` when you are done adding toppings.

## Available Subs

Chicken, Club Sub, Cuban, Grilled Cheese, Italian, Meatball, Tuna, Turkey

Sub names are matched case-insensitively.

## Requirements

Python 3.x — no external dependencies.

# Spend Chart in Python

A function that takes a list of budget categories and draws a text bar chart showing what percentage of the total spending went to each category. It's meant to go with a `Category` budget class .

## What it needs

`create_spend_chart(categories)` expects a list of `Category` objects, where each one has:

- `name`: a string like `"Food"`
- `ledger`: a list of dictionaries, each with an `"amount"` and a `"description"`

```python
{"amount": -15.50, "description": "groceries"}
```

Negative amounts are **withdrawals** (money spent). Positive amounts are deposits and are ignored by the chart.

## How it works

1. **Total spent.** Adds up every withdrawal across all categories (using `-item["amount"]` to turn negatives into positive numbers).
2. **Percentages.** For each category, works out its share of the total, then rounds **down** to the nearest 10. For example, 47% becomes 40%, and 99% becomes 90%. If nothing was spent at all, every category gets 0%.
3. **Bars.** Loops from 100 down to 0 in steps of 10. For each level, it prints an `o` under every category whose percentage is at or above that level.
4. **Horizontal line.** Draws dashes that are wide enough for all the bars (`3 * number of categories + 1`).
5. **Category names.** Prints each name vertically, one letter per row, padded with spaces so shorter names line up with longer ones.

## Usage

```python
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(50, "groceries")

entertainment = Category("Entertainment")
entertainment.deposit(1000, "initial deposit")
entertainment.withdraw(40, "movies")

business = Category("Business")
business.deposit(1000, "initial deposit")
business.withdraw(10, "supplies")

print(create_spend_chart([business, food, entertainment]))
```

Output (spent 10, 50, and 40 out of 100 total):

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60|          
 50|    o     
 40|    o  o  
 30|    o  o  
 20|    o  o  
 10| o  o  o  
  0| o  o  o  
    ----------
     B  F  E  
     u  o  n  
     s  o  t  
     i  d  e  
     n     r  
     e     t  
     s     a  
     s     i  
           n  
           m  
           e  
           n  
           t
```

## Things to know

- **Percentages are rounded down to the nearest 10**, not to the closest number. A category with 59% spending shows as 50%.
- **Percentages are based on total spending, not on deposits.** Only withdrawals count.
- **Trailing spaces matter.** Each row of the chart ends with spaces (every bar column is 3 characters wide), and the last line is trimmed with `rstrip("\n")` so there's no extra blank line at the end. This matters if you compare the output with an exact expected string in tests.
- **Order of the bars follows the order of the list** you pass in.
- **An empty list will crash.** `max()` on zero categories raises a `ValueError`, so make sure there's at least one category.
- The function only returns the chart as a string, so you need to `print()` it.

## Ideas to improve it

- Handle an empty category list without crashing
- Pull the "total spent for a category" loop into a helper, since the same loop is written twice
- Remove the extra `int(...)` step by doing `int(category_spent / total_spent * 10) * 10` directly
- Add unit tests for the zero-spending case and for categories with different name lengths

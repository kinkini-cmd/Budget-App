def create_spend_chart(categories):
    # Calculate total amount spent
    total_spent = 0

    for category in categories:
        for item in category.ledger:
            if item["amount"] < 0:
                total_spent += -item["amount"]

    # Calculate percentages
    percentages = []

    for category in categories:
        category_spent = 0

        for item in category.ledger:
            if item["amount"] < 0:
                category_spent += -item["amount"]

        if total_spent == 0:
            percentage = 0
        else:
            percentage = int(category_spent / total_spent * 100)
            percentage = (percentage // 10) * 10

        percentages.append(percentage)

    # Title
    chart = "Percentage spent by category\n"

    # Bars
    for level in range(100, -1, -10):
        chart += f"{level:>3}| "

        for percentage in percentages:
            if percentage >= level:
                chart += "o  "
            else:
                chart += "   "

        chart += "\n"

    # Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Vertical category names
    max_length = max(len(category.name) for category in categories)

    for i in range(max_length):
        chart += "     "

        for category in categories:
            if i < len(category.name):
                chart += category.name[i]
            else:
                chart += " "

            chart += "  "

        if i < max_length - 1:
            chart += "\n"

    return chart.rstrip("\n")

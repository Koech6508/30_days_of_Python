#Python is an object oriented programming language. Everything in Python is an object, with its properties and methods.
# We create class to create an object. A class is like an object constructor, or a "blueprint" for creating objects

#
class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return max(self.data) - min(self.data)

    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            mid1 = sorted_data[n // 2 - 1]
            mid2 = sorted_data[n // 2]
            return (mid1 + mid2) / 2
        else:
            return sorted_data[n // 2]

    def mode(self):
        frequency_dict = {}
        for value in self.data:
            frequency_dict[value] = frequency_dict.get(value, 0) + 1
        max_count = max(frequency_dict.values())
        mode_values = [key for key, count in frequency_dict.items() if count == max_count]
        return {'mode': mode_values[0], 'count': max_count}

    def std(self):
        mean_value = self.mean()
        variance = sum((x - mean_value) ** 2 for x in self.data) / len(self.data)
        return variance ** 0.5

    def var(self):
        mean_value = self.mean()
        return sum((x - mean_value) ** 2 for x in self.data) / len(self.data)

    def freq_dist(self):
        sorted_data = sorted(self.data)
        unique_values = list(set(sorted_data))
        freq_distribution = [(sorted_data.count(value), value) for value in unique_values]
        return sorted(freq_distribution, reverse=True)
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)

print('Count:', data.count())
print('Sum:', data.sum())
print('Min:', data.min())
print('Max:', data.max())
print('Range:', data.range())
print('Mean:', data.mean())
print('Median:', data.median())
print('Mode:', data.mode())
print('Standard Deviation:', data.std())
print('Variance:', data.var())
print('Frequency Distribution:', data.freq_dist())


# PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses
class PersonAccount:
    def __init__(self, firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_info(self):
        return f"{self.firstname} {self.lastname}'s Account Information"

    def add_income(self, description, amount):
        self.incomes[description] = amount

    def add_expense(self, description, amount):
        self.expenses[description] = amount

    def account_balance(self):
        return self.total_income() - self.total_expense()

# Example usage:
incomes = {'Salary': 5000, 'Freelance': 1000}
expenses = {'Rent': 1200, 'Utilities': 200, 'Groceries': 300}

person_account = PersonAccount('John', 'Doe', incomes, expenses)

print(person_account.total_income())  # Output: 6000
print(person_account.total_expense())  # Output: 1700
print(person_account.account_info())  # Output: John Doe's Account Information
print(person_account.account_balance())  # Output: 4300

person_account.add_income('Bonus', 1000)
person_account.add_expense('Dining out', 150)

print(person_account.total_income())  # Updated income with Bonus: 7000
print(person_account.total_expense())  # Updated expense with Dining out: 1850
print(person_account.account_balance())  # Updated balance: 5150

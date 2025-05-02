class CustomerManager:
    def __init__(self):
        self.customers = {}
        self.tax_rate = 0.2
        self.tax_threshold = 100
        self.discount_threshold = 500

    def add_customer(self, name, purchases):
        if name in self.customers.keys():
            self.customers[name].extend(purchases)
        else:
            self.customers[name] = purchases

    def add_purchase(self, name, purchase):
        self.add_customer(name, [purchase])

    def add_purchases(self, name, purchases):
        self.add_customer(name, purchases)

    def check_for_discount(self, total):
        if total > self.discount_threshold:
            print("Eligible for discount")
        elif total > 300:
            print("Potential future discount customer")
        else:
            print("No discount")

    def check_customer_type(self, total):
        if total > 1000:
            print("VIP Customer!")
        elif total > 800:
            print("Priority Customer")

    def calculate_purchases_total(self, purchases):
        total = 0
        for purchase in purchases:
            if purchase['price'] > self.tax_threshold:
                taxed_price = purchase['price'] * (1 + self.tax_rate)
                total += taxed_price
            else:
                total += purchase['price']

        return total

    def generate_report(self):
        for name, purchases in self.customers.items():
            total = self.calculate_purchases_total(purchases)
            print(name)
            self.check_for_discount(total)
            self.check_customer_type(total)


def calculate_shipping_fee_for_heavy_items(purchases):
    for purchase in purchases:
        if purchase.get('weight', 0) > 20:
            return 50
    return 20

def calculate_shipping_fee_for_fragile_items(purchases):
    for purchase in purchases:
        if purchase.get('fragile', False):
            return 60
    return 25

flat_tax = 0.2

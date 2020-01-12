class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        k = []
        if not self.ingredients or not self.toppings:
            return []
        else:
            for i in self.ingredients:
                for j in self.toppings:
                    k.append([i, j])
            return k


machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
# should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
print(machine.scoops())

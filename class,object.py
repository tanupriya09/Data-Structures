class Phone:
    def make_call(self):
        print("Making a phone call")

    def play_game(self):
        print("Playing a game ")

p1 = Phone()
p1.make_call()
p1.play_game()

#new class-

class Phone:
    def add_color(self,color):
        self.color=color
    def show_color(self):
        return self.color
    def add_cost(self,cost):
        self.cost=cost
    def show_cost(self):
        return self.cost
    def make_call(self):
        print("Making a call")
    def play_game(self):
        print("Playing game")
p2 = Phone()
p2.add_color("blue")

print(p2.show_color())
p2.add_cost(40)
print(p2.show_cost())

class Iphone(Phone):
    def cure_cancer(self):
        print("I can cure cancer")
ip1 = Iphone()
ip1.add_cost(100)
print(ip1.show_cost())
ip1.cure_cancer()

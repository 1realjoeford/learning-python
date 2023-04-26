class Cook:
    def __init__(self, chef, food):
        self.chef = chef
        self.food = food

    def introduce(self):
        print(f"Hi my name is {self.chef}, i am a chef and today I'll be cooking {self.food} today")

joe_cooks = Cook('Joe Ford', 'rice')
joe_cooks.introduce()
class Enemy:

    def __init__(self, life):
        self.life = life

    def get_life(self):
        print(self.life)

enemy1 = Enemy(5)
enemy2 = Enemy(20)

enemy1.get_life()
enemy2.get_life()
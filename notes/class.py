class player():
    def __init__(self, name) -> None:
        self.name = name

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


n_player = player('Seth')
print(n_player.name)

n_player.set_name('Woofers')
print(n_player.name)

print(n_player.get_name())
from mediaclass import Media

class Clip(Media):
    def __init__(self, t, n, d, s, u, l, c, y, g):
        super().__init__(t, n, d, s, u, l, c, y)
        self.genre=g
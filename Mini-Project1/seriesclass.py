from mediaclass import Media

class Series(Media):
    def __init__(self, t, n, d, s, u, l, c, y, e):
        super().__init__(t, n, d, s, u, l, c, y)
        self.episodnumber=e
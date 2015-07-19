class TryIteration:
    def __getitem__(self, number):
        self.data='hello'
        return self.data[number]

x=TryIteration()

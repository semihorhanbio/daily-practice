class Ship:
    """Taking into account that an average crew member on board adds 1.5 units to the draft, 
    a ship that has a draft of more than 20 without crew is considered worthy to loot. 
    Any ship weighing that much must have a lot of booty!"""
    
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    
    def is_worth_it(self):
        return self.draft - (self.crew * 1.5) > 20

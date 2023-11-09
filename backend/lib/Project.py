class Project:
    def __init__(self, id, name, link, notes, created_at):
        self.id = id
        self.name = name
        self.link = link
        self.notes = notes
        self.created_at = created_at

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Project({self.id}, {self.name}, {self.link}, {self.notes}, {self.created_at})"
    
    def is_valid(self):
        if self.name == "" or self.name == None:
            return False
        if self.link == "" or self.link == None:
            return False
        
        return True
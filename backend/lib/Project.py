class Project:
    def __init__(self, id, name, link, notes):
        self.id = id
        self.name = name
        self.link = link
        self.notes = notes

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Project({self.id}, {self.name}, {self.link}, {self.notes})"
    
    def __name_is_invalid(self):
        if self.name == "" or self.name == None:
            return True
        
    def __link_is_invalid(self):
        if self.link == "" or self.link == None:
            return True
        
    def is_valid(self):
        if self.__name_is_invalid() or self.__link_is_invalid():
            return False
        return True
    
    def generate_error_message(self):
        error_message = "Error: "
        if self.__name_is_invalid() and self.__link_is_invalid():
            error_message += "name and link"
        elif self.__name_is_invalid():
            error_message += "name"
        else:
            error_message += "link"
        error_message += " must have a value"
        return error_message

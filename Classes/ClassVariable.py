"""
Example on how too use class variables
that are like static variables
"""
class Contact:

    contact_list = list()
    last_added = ""

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.contact_list.append(self)
        Contact.last_added = name


if __name__ == "__main__":
    _c1 = Contact("marcello chiuminatto",  "mchiuminatto@gmail.com")
    print("last added from c1", _c1.last_added)
    _c2 = Contact("capitain america",  "camer@gmail.com")
    print("last added from c1 again", _c1.last_added)
    print("last added from c2 again", _c2.last_added)
    print([c.name for c in _c1.contact_list])
    print([c.name for c in _c2.contact_list])

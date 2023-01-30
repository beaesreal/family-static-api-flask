
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""

from random import randint



class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # Example list of members
        self._members = []


    # Read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)
        

    def add_member(self, member):
        # Fill this method and update the return
        member["lastname"] = self.last_name
        if "id" not in member : member["id"] = self._generateId()
        self._members.append(member)

        return member


    def delete_member(self, id):
        # Fill this method and update the return
        for i in range(len(self._members)):
            if self._members[i]['id'] == id:
                aux = self._members[i]
                del self._members[i]
                return aux

        return {"msg" : "Id not found"}


    def get_member(self, id):
        for i in range(len(self._members)):
            if self._members[i]['id'] == id:
                return self._members[i]

        return {"msg" : "Id not found"}
        
        

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
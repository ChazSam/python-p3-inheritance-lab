#!/usr/bin/env python

from user import User

import random
import ipdb

class Teacher(User):

    def __init__(self, first_name, last_name, knowledge=["Art","Music"]):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge
        
        

    def teach(self):
        # self.teach = teach
        # ipdb.set_trace()
        print(self.knowledge)
        return self.knowledge[random.randint(0, len(self.knowledge)-1)]
    

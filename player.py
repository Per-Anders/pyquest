import math

class Player():

    xp = 0
    level = 1
    quest_list = []
    completed_quests = []
    id = 0
    xp_levels = 0



    def generate_levels(self, level_count, xp_increase):
        levels = {}
        i = 1
        while i <= level_count:
            levels[i] = i*math.ceil(i*xp_increase)
            i+=1
        self.xp_levels = levels



    def calculate_xp(self, level):
        xp = 0
        for k,v in self.xp_levels.items():
            if level == k:
                xp = math.floor(v/k)
        return xp



    def get_quest(self, id):
        for quest in self.quest_list:
            if quest['id'] == id:
                return quest


    def show_possible_quests(self):
        for quest in self.quest_list:
            if quest['level_required'] <= self.level:
                print(quest)


    def show_all_quests(self):
        for quest in self.quest_list:
            print(quest)
         

    def add_quest(self, quest):
        xp = self.calculate_xp(quest['level_required'])
        q = {}
        self.id = self.id + 1
        q['id'] = self.id
        q['name'] = quest[0]
        q['level_required'] = quest[1]
        q['xp'] = xp
        self.quest_list.append(q)



    def add_many_quests(self, list):
        for quest in list:
            xp = self.calculate_xp(quest[1])
            q = {}
            self.id = self.id + 1
            q['id'] = self.id
            q['name'] = quest[0]
            q['level_required'] = quest[1]
            q['xp'] = xp
            self.quest_list.append(q)


    def complete_quest(self, id):
        quest = self.get_quest(id)
        if quest:
            if self.level >= quest['level_required']:
                self.xp = self.xp + quest['xp']
                self.quest_list.remove(quest)
                self.completed_quests.append(quest)
                self.level_up()
            else:
                print("You must be level", quest['level_required'], "to complete this quest")  
        else:
            print("Quest does not exists")



    def level_up(self):
        level_counter = 1
        for k,v in self.xp_levels.items():
            if self.xp >= v:
                level_counter+=1
        self.level = level_counter
        
        

    def delete_quest(self, id):
        for quest in self.quest_list:
            if quest['id'] == id:
                self.quest_list.remove(quest)







# initialize player object
player = Player()

#generate levels and xp
player.generate_levels(20, 10.5)


# generate quests: [name, level_required]
quests = [
    ['make fire', 1],
    ['choop wood', 1],
    ['eat steak', 2],
    ['kill monsters', 3],
    ['make a cabin', 20],
    ['shoot a bear', 15]
]

# add quests to player list
player.add_many_quests(quests)


#show possible quest in level 
player.show_possible_quests()

# complete a quest
player.complete_quest(1)

#complete another quest
player.complete_quest(2)

# show player stats
print("Level:", player.level)
print("Xp:", player.xp)



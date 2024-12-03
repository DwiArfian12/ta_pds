import random, math, sys, ft, time, os

#Variables
startPopulation = 50
food = 75
agriculture = 4.4
populationBurden = 1
disasterChance = 10
simulationLimit = 1000

peopleDictionary = []
peopleDictionaryAncestors = []
peopleDictionaryHistory = []

fertilityx = 18
fertilityy = 45
infantMortality = 10
workingx = 14
workingy = 67
lastNames = [
'Smith', 'Jones', 'Williams', 'Brown', 'Wilson', 'Taylor', 'Anderson', 'Johnson', 'White', 
'Thompson', 'Lee', 'Martin', 'Thomas', 'Walker', 'Kelly', 'Young', 'Harris', 'King', 'Ryan', 
'Roberts', 'Hall', 'Evans', 'Davis', 'Wright', 'Baker', 'Campbell', 'Edwards', 'Clark', 
'Robinson', 'McDonald', 'Hill', 'Scott', 'Clarke', 'Mitchell', 'Stewart', 'Moore', 'Turner', 
'Miller', 'Green', 'Watson', 'Bell', 'Wood', 'Cooper', 'Murphy', 'Jackson', 'James', 'Lewis', 
'Allen', 'Bennett', 'Robertson']
femmSuffix = ['ine', 'ela', 'a', 'lyn']
alphabet = 'abcdefghijklmnopqrstuvwxyz'
consonats = 'bcdfghjklmnpqrstvwxyz'
vowel = ['a', 'e', 'i', 'o', 'u']
inbreeding = 0
totalLived = 0

#graphing
born_this_year = 0
died_this_year = 0

class God:
    def __init__(self, name):
        self.name = name

class Person:
    def __init__(self, age, name, mother, father, id, gender):
        self.gender = gender #0 Male, 1 Female
        self.age = age
        self.name = name
        self.pregnant = False
        self.id = id
        self.maxLife = float(random.randint(50, 88))

        #reproduction
        self.mother = mother
        self.father = father
        self.children = []
        self.married = False
        self.partner = object

        global totalLived
        totalLived += 1

        #Plotting on first generation
        if 'Eve' in self.mother.name:
            peopleDictionaryHistory.append([self.name, self.name, 'God'])
        else:
            peopleDictionaryHistory.append([self.name, self.name, self.mother.name])

        #Adam and Eve protocol
        if len(peopleDictionary) == 0:
            self.gender = 0
        elif len(peopleDictionary) == 1:
            self.gender = 1

    def eat(self):
        global food
        lfood = ft.line_food
        multiplier = float(lfood[-1] / len(peopleDictionary))
        if len(peopleDictionary) > 150:
            if multiplier >= 1:
                if self.age < 10:
                    food -= multiplier * .2
                elif self.age > 13 and self.age < 60:
                    food -= 1 + multiplier
                    self.maxLife -= multiplier / self.maxLife
                else:
                    food -= multiplier * .4
            else:
                if self.age < 10:
                    food -= .2
                elif self.age > 13 and self.age < 60:
                    food -= 1
                else:
                    food -= .5
        else:
            multiplier = 1
            if self.age < 10:
                food -= .2
            elif self.age > 13 and self.age < 60:
                food -= 1
            else:
                food -= .5
        return multiplier

    def marraige(self, name):
        global agriculture
        name = name
        inbred = False
        if self.age > 18:
            try:
                possible_partners = [p for p in peopleDictionary if p.name != self.name]
                for partner in possible_partners:
                    if partner.mother.name == self.mother.name:
                        possible_partners.remove(partner)
                    elif partner.father.name == self.father.name:
                        possible_partners.remove(partner)
                if len(possible_partners) < 1:
                    possible_partners = [p for p in peopleDictionary if p.name != self.name]

                partner = random.choice(possible_partners)

                if self.married is True:
                    if self.partner not in peopleDictionary:
                        self.married = False
                    else:
                        pass

                elif self.married is not True and partner.married is not True:
                    self.married = True
                    self.partner = partner
                    partner.married = True
                    partner.partner = self

                else:
                    self.partner = partner
                    if partner.partner.married is not True:
                        partner.partner = self

                if self.mother.name == partner.mother.name:
                    inbred = True

                if self.father.name == partner.father.name:
                    inbred = True

                lfood = ft.line_food
                multiplier = math.ceil(lfood[-1] / len(peopleDictionary))

                if multiplier > 6:
                    for x in range(0, 6):
                        if random.randint(0, 6) == 1:
                            self.have_child(name, inbred)
                elif multiplier > 0 and multiplier < 6:
                    for x in range(0, multiplier):
                        if random.randint(0, multiplier) == 1:
                            self.have_child(name, inbred)
                else:
                    if random.randint(0, 1) == 1:
                        self.have_child(name, inbred)

            except IndexError:
                print('index error')
                pass

    def generate_name(self, name, partner):
        name = name
        global vowel
        partner = str(partner)
        n = random.randint(0, 20)
        new_name = ''
        gender = random.randint(0, 1)
        if n == 0:
            second = random.choice(lastNames)
            new_name = name[:len(name) // 2] + second[len(second) // 2:]

        elif n == 1:
            new_name = random.choice(lastNames)
            new_name = new_name[::-1]

        elif n == 2:
            new_name = name[:1] + partner[1:-1]

        elif n == 3:
            new_name = partner[:1] + name[1:-1]

        elif n == 4:
            second = random.choice(lastNames)
            second = second[::-1]
            new_name = name[:len(name) // 2] + second[len(second) // 2:]

        elif n == 5:
            second = random.choice(lastNames)
            second = second[::-1]
            new_name = second[len(second) // 2:] + name[:len(name) // 2]

        elif n == 6:
            new_name = partner[:len(partner) // 2] + name[len(name) // 2:]

        elif n == 7:
            second = random.choice(lastNames)
            second = second[::-1]
            new_name = name[len(name) // 2:] + second[:len(second) // 2]

        elif n == 8:
            second = random.choice(lastNames)
            second = second[::-1]
            new_name = second[:len(second) // 2] + name[:len(name) // 2:]

        elif n == 9:
            new_name = partner[::-1] + name[:len(name) // 2]

        elif n == 10:
            new_name = name[::-1] + partner[:len(partner) // 2]

        elif n == 11:
            new_name = name[::-1]

        elif n == 12:
            new_name = partner[::-1]

        elif n == 13:
            new_name = name[:len(name) // 2] + name[:len(name) // 2]

        elif n == 14:
            new_name = partner[:len(name) // 2] + partner[:len(name) // 2]

        elif n == 15:
            new_name = name[:len(name) // 2] + partner[:len(name) // 2]

        elif n == 16:
            new_name = partner[:len(name) // 2] + name[:len(name) // 2]

        elif n == 17:
            new_name = partner[:2]

        elif n == 18:
            new_name = name[:2]

        elif n == 19:
            new_name = name[::-1]
            new_name = new_name[:2]

        else:
            new_name = name[:len(name) // 2] + partner[len(partner) // 2:]

        if '.jr' in new_name:
            new_name = new_name.replace('.jr', '')
        if 'rj.' in new_name:
            new_name = new_name.replace('rj.', '')
        if '.j' in new_name:
            new_name = new_name.replace('.j', '')
        if 'j.' in new_name:
            new_name = new_name.replace('j.', '')
        if '.' in new_name:
            new_name = new_name.replace('.', '')

        for l in alphabet:
            n = new_name.count(l)
            if n > 2:
                for x in range(0, n-1):
                    new_name = new_name.replace(l, '')

        last = ''
        for r in new_name:
            if r in consonats and r == last:
                new_name = new_name.replace(r, '')
            else:
                last = r

        vowels = 0
        for l in vowel:
            s = new_name.count(l)
            if s > 0:
                vowels += 1
        if vowels == 0:
            new_name = new_name[:len(new_name) // 2] + random.choice(vowel) + new_name[len(new_name) // 2:]

        if len(new_name) < 3:
            if vowels == 0:
                if random.randint(0, 1) == 1:
                    new_name = new_name[random.randint(0,1)] + random.choice(vowel)
                else:
                    new_name = random.choice(vowel) + new_name[random.randint(0,1)]

        if len(new_name) < 4 and gender == 1:
            new_name = new_name + random.choice(femmSuffix)

        if gender == 0:
            for x in femmSuffix:
                if x in new_name:
                    new_name = new_name.replace(x, '')

        if len(new_name) < 2:
            new_name = new_name + random.choice(vowel) + random.choice(consonats)

        new_name = new_name.lower().title()
        return new_name, n, gender

    def have_child(self, name, inbred=False):
        name = name
        global born_this_year, inbreeding
        if self.gender == 1 and self.partner.gender == 0:
            if self.pregnant is False:
                if self.age > fertilityx and self.age < fertilityy:
                    if food > len(peopleDictionary):
                        self.pregnant = True
                    elif random.randint(0, 1) == 1:
                        self.pregnant = True

        if self.pregnant is True:
            self.pregnant = False
            if random.randint(0, 100) > infantMortality:

                new_name, n, gender = self.generate_name(name, self.partner.name)


                if inbred is True:
                    new_name = self.partner.name + '.jr'
                    inbreeding += 1


                if new_name not in lastNames:

                    peopleDictionary.append(Person(age=0,
                                                   name=new_name,
                                                   mother=self,
                                                   father=self.partner,
                                                   id= self.id,
                                                   gender= gender))

                    self.children.append(peopleDictionary[-1])
                    self.partner.children.append(peopleDictionary[-1])
                    born_this_year += 1

                    lastNames.append(new_name)

                else:
                    new_name = new_name[::-1].lower().title()

                    if inbred is True:
                        new_name = new_name.replace('Rj.', '')
                        new_name = self.partner.name + '.jr'
                        inbreeding += 1


                    if new_name not in lastNames:
                        peopleDictionary.append(Person(age=0,
                                                       name=new_name,
                                                       mother=self,
                                                       father=self.partner,
                                                       id=self.id,
                                                       gender= gender))

                        self.children.append(peopleDictionary[-1])
                        self.partner.children.append(peopleDictionary[-1])
                        born_this_year += 1
                        lastNames.append(new_name)

        if self.gender == 0 and self.partner.gender == 1:
            if self.partner.pregnant is False:
                if self.partner.age > fertilityx and self.partner.age < fertilityy:
                    if random.randint(0, 1) == 1:
                        self.partner.pregnant = True

def harvest(line_year, line_food):
    ablePeople = 0
    foodToDegrade = 0
    global peopleDictionary, food

    for person in peopleDictionary:
        if person.age > workingx and person.age < workingy:
            ablePeople += 1

    food += ablePeople * agriculture

    consumptionList = []
    for person in peopleDictionary:
        c = person.eat()
        consumptionList.append(c)
    try:
        consumption = (sum(consumptionList) / len(consumptionList))
    except ZeroDivisionError:
        pass

    if food < len(peopleDictionary):
        peopleToStarve = len(peopleDictionary) - math.ceil(food)
        killPeople(peopleToStarve, 'starve')

        food = 0

    else:
        food -= len(peopleDictionary)

        if food > len(peopleDictionary):
            foodToDegrade = food / 3

        food -= foodToDegrade
        if food < 0:
            food = 0

    return ablePeople, foodToDegrade, consumption

def killPeople(victim, event, person=object):
    global died_this_year, peopleDictionaryAncestors

    if event == 'disaster' or 'starve':
        if len(peopleDictionary) > victim:
            peopleToKill = random.sample(peopleDictionary, victim)
        else:
            peopleToKill = peopleDictionary

        for person in peopleToKill:
            peopleDictionary.remove(person)
        peopleDictionaryAncestors.append(peopleToKill)
        died_this_year += len(peopleToKill)
    else:
        peopleDictionary.remove(person)
        peopleDictionaryAncestors.append(person)
        died_this_year += 1

def disaster(year):
    global food
    if year > 5:
        if random.randint(0, 1) == 1:
            if random.randint(0, 400) < disasterChance:
                toKill = int(random.uniform(0.05, 0.2) * len(peopleDictionary))
                killPeople(toKill, 'disaster')
                print('\033[31m' + '------------DISASTER-----------' + '\033[0m')
        else:
            if random.randint(0, 400) < disasterChance:
                toKill = int(random.uniform(0.05, 0.5) * food)
                food -= toKill
                print('\033[31m' + '------------FOOD LOSS-----------' + '\033[0m')

def runYear():
    global died_this_year, agriculture, infantMortality, populationBurden, disasterChance, born_this_year, totalLived, inbreeding
    line_year = ft.line_year
    line_food = ft.line_food
    avgage = ft.line_avg_age[-1]

    # Birth, Deaths and Marraiges
    for person in peopleDictionary:
        if person.age > person.maxLife:
            killPeople(1, 'age', person)
            continue
        elif person.age > 13:
            person.marraige(person.name)
        person.age += 1
    infantMortality *= 0.985

    #Agriculture
    populationBurden = len(peopleDictionary)  * .005
    populationBurden += food * .001
    workers, ftd, con = harvest(line_year, line_food)
    agriculture *= 1.002

    #Disaster
    maxDisasterChance = math.floor(0 + agriculture)
    disasterChance = random.randint(0, max(maxDisasterChance, 15))
    disaster(line_year[-1])

    ft.plot_graph(peopleDictionary, born_this_year, died_this_year, food)

    if len(line_food) > 1:

        os.system('cls')
        print(f'---[Year: {line_year[-1]}, '
              f'\t Total Lived: {totalLived}]--- '
              f'\t  |   Alive: {"0" + str(len(peopleDictionary)) if len(peopleDictionary) < 100 else len(peopleDictionary)} '
              f'\t Deaths: {died_this_year}   '
              f'\t Births: {born_this_year}   '
              f'\t Inbreeding: {inbreeding}   |   '
              f'\t Active Workers: {workers}  '
              f'\t --[Food: {"%.2f" % food}  '
              f'\t Food lost: {"%.2f" % ftd}]-- ')

    born_this_year = 0
    died_this_year = 0
    inbreeding = 0

def beginSim():
    for x in range(0, startPopulation):
        peopleDictionary.append(Person(age= 20,
                                       name=lastNames[x],
                                       mother=God(name=f'Eve_{x}'),
                                       father=God(name=f'Adam_{x}'),
                                       id=x,
                                       gender=random.randint(0, 1)))

def main():
    global simulationLimit, startPopulation
    
    # beginSim()
    o = str(input('Run simulation? Y or N: ')).lower()
    if o == 'y':
        o = int(input('Start Population? (>=2 or < <=50): '))
        if type(o) != int:
            print('You have not entered a valid number')
            time.sleep(2)
            sys.exit()
        elif type(o) == int:
            if o > 1 and o <= 50:
                startPopulation = o
                beginSim()
            else:
                print('You have not entered a valid number')
                time.sleep(2)
                sys.exit()

        c = int(input('Target population cap (must be greater than start population): '))
        if type(c) != int:
            print('You have not entered a valid number')
            time.sleep(2)
            sys.exit()
        elif type(c) == int:
            if c > o:
                simulationLimit = c
                beginSim()
            else:
                print('You have not entered a valid number')
                time.sleep(2)
                sys.exit()
    else:
        print('See you')
        sys.exit()


if __name__ == '__main__':
    main()

while len(peopleDictionary) < simulationLimit and len(peopleDictionary) > 1:
    runyear = runYear()
else:
    o = str(input("\nWhat output would you like; '\033[32mG\033[0m'raph, '\033[32mF\033[0m'amily Tree, or '\033[32mB\033[0m'oth? ")).lower()
    try:
        if o == 'g':
            ft.show_graph()
        elif o == 'f':
            ft.familyTree(peopleDictionaryHistory)
        elif o == 'b':
            ft.familyTree(peopleDictionaryHistory)
            ft.show_graph()
        else:
            print('None selected')
            time.sleep(1)
            sys.exit()
    except NameError:
        print('Graphing Modules not installed')
        time.sleep(1)
        sys.exit()

# -*- coding: utf-8 -*-
class Employee:
    '''There are 3 types of employee: developer, designer and manager.
    Each employee has: first name, second name, salary, experiance (years) and 
    manager. Each employee gets the salary, defined in field Salary.    
    If experiance of employee is > 2 years, he gets bonus + 200$, 
    if experiance is > 5 years, he gets salary*1.2 + bonus 500'''
    def __init__(self, first_name, second_name, salary, experiance, manager):
        self.first_name = first_name
        self.second_name = second_name
        self.experiance = experiance
        self.manager = manager
        self.salary = salary
        if self.experiance > 5:
            self.salary = self.salary * 1.2 + 500
        elif self.experiance > 2:
            self.salary += 200
        
    def __str__(self):
        '''Redefine string representation for employee as follows: "@firstName@ 
        @secondName@, manager:@manager secondName@, experiance:@experiance@'''
        return '{} {}, manager:{}, experiance:{}'.format(self.first_name, 
                self.second_name, self.manager.second_name, self.experiance)
        

class Designer(Employee):
    '''Each designer has effectivness coefficient(0-1). Each designer gets the 
    salary = salary*effCoeff'''
    def __init__(self, eff_coeff=0):
        self.eff_coeff = eff_coeff
        self.salary = super().salary * eff_coeff
        super().manager.team.append(self)
        
class Developer(Employee):
    def __init__(self):
        super().manager.team.append(self)
    
class Manager(Employee):
    '''Each manager has team of developers and designers.
    Each manager gets salary +
#   ii) 200$ if his team has >5 members
#   iii) 300$ if his team has >10 members
#   iiii) salary*1.1 if more than half of team members are developers.'''
    def __init__(self):
        self.salary = super().salary
        self.team = []
       
    def count_salary(self, team):
        if len(team)>5:
            self.salary += 200
        elif len(team)>10:
            self.salary += 300
        devs = 0
        for human in team:
            if human.__class__() == 'Developer':
                devs += 1
            if devs > len(team)/2:
                self.salary *= 1.1
                    

class Department():
    '''Department should have list of managers(which have their own teams)
       Department should be able to give salary (for each employee message: 
    "@firstName@ @secondName@: got salary: @salaryValue@")'''
    def __init__(self, managers):
        self.managers = managers
        
    def give_salary(self):
        for manager in self.managers:
            print('{} {}: got salary: {}'.format(self.manager.first_name, 
                self.manager.second_name, self.manager.salary, self.experiance))
            
            for human in manager.team:
                print('{} {}: got salary: {}'.format(human.first_name, 
                human.second_name, human.salary, human.experiance))
            
class LinkedList(list):
    '''2. Create LinkedList Class with methods:
     a) get(i) 
     b) put(i)
     c) delete(i)
     d) indexOf(el) - first element = el
     e) size()'''
    def get(self, i):
        return self[i]
    
    def put(self, i):
        return self.append[i]
    
    def delete(self, i):
        return self[i]
    
    def indexOf(self, el):
        return self[el]
    
    def size(self):
        return len(self)
    
mihalych = Manager()
vasya = Developer('Vasya', 'Petrenko', 1000, 2, mihalych)
dep = Department([mihalych])
dep.give_salary()
print(type(a))


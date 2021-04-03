'''
Created on 30.10.2019

@author: jenni
'''

import random

class CivilizationUnit:
    
    MAX_HP = 100
    DAMAGE_SCALE = 30
    RANDOM_DAMAGE_DIFF = 8

    def __init__(self, unit_name, attack, defense = None, is_ranged = False):
        "Initializes a new CivilizationUnit"
        self.__name = unit_name
        self.__attack_strenght = attack
        self.__defense_strenght = self.kumpi(defense, attack)
        self.__fortified = False
        self.__ranged = is_ranged
        self.__hp = CivilizationUnit.MAX_HP
    
    def kumpi(self,defense, attack):
        if defense == None:
            return attack
        else:
            return defense
    
    def get_name(self):
        return self.__name
    
    def is_alive(self):
        # Implement me!
        pass # Remove this afterwards 
    
    def is_eliminated(self):
        if self.__hp == 0:
            return True 
        else:
            return False    
            
    def get_effective_defense_strength(self):
        defense = self.__hp / 100 
        defense = 50 * defense
        defense = (50 + defense) / 100
        
        if not self.__fortified:
            defense = self.__defense_strenght * defense
            return defense
        elif self.__fortified:
            defense = self.__defense_strenght * defense * 1.4
            return defense
    
    def get_effective_attack_strength(self):
        attack = self.__hp / 100
        attack = 50 * attack
        attack = (50 + attack) / 100
        
        attack = self.__attack_strenght * attack
        return attack 
              
    def attack(self, other_unit):
        damage_dealt = other_unit.defend(self)
        if self.__ranged:
            damage_taken = 0
        elif not self.__ranged:
            excepted_damage_taken = int(CivilizationUnit.DAMAGE_SCALE * other_unit.get_effective_attack_strength() / self.get_effective_defense_strength())
            alaraja = excepted_damage_taken - CivilizationUnit.RANDOM_DAMAGE_DIFF
            ylaraja = excepted_damage_taken + CivilizationUnit.RANDOM_DAMAGE_DIFF
            if alaraja < 1:
                alaraja = 1
            damage_taken = random.randint(alaraja, ylaraja)
            self.__hp -= damage_taken
            if self.__hp < 0:
                self.__hp = 0
        
        return damage_dealt, damage_taken
        
    def defend(self, other_unit):
        excepted_damage_taken = int(CivilizationUnit.DAMAGE_SCALE * other_unit.get_effective_attack_strength() / self.get_effective_defense_strength())
        alaraja = excepted_damage_taken - CivilizationUnit.RANDOM_DAMAGE_DIFF
        ylaraja = excepted_damage_taken + CivilizationUnit.RANDOM_DAMAGE_DIFF
        if alaraja < 1:
            alaraja = 1
        damage_taken = random.randint(alaraja, ylaraja)
        self.__hp -= damage_taken
        if self.__hp < 0:
            self.__hp = 0
        return damage_taken
    
    def fortify(self):
        self.__fortified = True 
    
    def unfortify(self):
        self.__fortified = False
    
    def heal(self, amount):
        self.__hp += amount
        if self.__hp > CivilizationUnit.MAX_HP:
            self.__hp = CivilizationUnit.MAX_HP          
            
    def get_hp(self):
        return self.__hp 
            
    def is_fortified(self):
        return self.__fortified
        
    def __str__(self):
        if self.__fortified and self.__hp != 0 and self.__ranged:
            mjono = "{:s} - {:.0f}/{:.0f} (ranged) - HP: {:.0f}, FORTIFIED".format(self.__name,self.__attack_strenght,self.__defense_strenght,self.__hp) 
        elif not self.__fortified and self.__hp != 0 and self.__ranged:
            mjono = "{:s} - {:.0f}/{:.0f} (ranged) - HP: {:.0f}".format(self.__name,self.__attack_strenght,self.__defense_strenght,self.__hp) 
        elif self.__fortified and self.__hp != 0 and not self.__ranged:
            mjono = "{:s} - {:.0f}/{:.0f} (melee) - HP: {:.0f}, FORTIFIED".format(self.__name,self.__attack_strenght,self.__defense_strenght,self.__hp) 
        elif not self.__fortified and self.__hp != 0 and not self.__ranged:
            mjono = "{:s} - {:.0f}/{:.0f} (melee) - HP: {:.0f}".format(self.__name,self.__attack_strenght,self.__defense_strenght,self.__hp) 
        elif self.__hp == 0 and not self.__ranged:
            mjono = "{:s} - {:.0f}/{:.0f} (melee) - HP: 0, ELIMINATED".format(self.__name,self.__attack_strenght,self.__defense_strenght) 
        elif self.__hp == 0 and self.__ranged:
            mjono = "{:s} - {:.0f}/{:.0f} (ranged) - HP: 0, ELIMINATED".format(self.__name,self.__attack_strenght,self.__defense_strenght) 
  
        return mjono

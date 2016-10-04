class Species:
    # abilities
    abilities = {'brawn': 2, 'agility': 2, 'intellect': 2,
                'cunning': 2, 'willpower': 2, 'presence': 2}

    def get_ability(this, abl):
        return this.abilities[abl]

    def update_ability(this, abl, num):
        this.abilities[abl] += num


    # skills
    general_skills = {'astrogation': 0, 'athletics': 0, 'charm': 0, 'coercion': 0,
                        'computers': 0, 'cool': 0, 'coordination': 0, 'deception': 0,
                        'discipline': 0, 'leadership': 0, 'mechanics': 0, 'medicine': 0,
                        'negotiation': 0, 'perception': 0, 'piloting (planatary)': 0,
                        'piloting (space)': 0, 'resilience': 0, 'skulduggery': 0,
                        'stealth': 0, 'streetwise': 0, 'survival': 0, 'vigilance': 0}


    general_abilities = {'astrogation': 'intellect', 'athletics': 'brawn', 'charm': 'presence',
                        'coercion': 'willpower', 'computers': 'intellect', 'cool': 'presence',
                        'coordination': 'agility', 'deception': 'cunning', 'discipline': 'willpower',
                        'leadership': 'presence', 'mechanics': 'intellect', 'medicine': 'intellect',
                        'negotiation': 'presence', 'perception': 'cunning', 'piloting (planatary)': 'agility',
                        'piloting (space)': 'agility', 'resilience': 'brawn', 'skulduggery': 'cunning',
                        'stealth': 'agility', 'streetwise': 'cunning', 'survival': 'cunning',
                        'vigilance': 'willpower'}

    combat_skills = {'brawl': 0, 'gunnery': 0, 'melee': 0, 'ranged (heavy)': 0,
                    'ranged (light)': 0}

    combat_abilities = {'brawl': 'brawn', 'gunnery': 'agility', 'melee': 'brawn',
                        'ranged (heavy)': 'agility', 'ranged (light)': 'agility'}

    knowledge_skills = {'core worlds': 0, 'education': 0, 'lore': 0, 'outer rim': 0,
                        'underworld': 0, 'warfare': 0, 'xenology': 0}

    talents = list()


#class Bothans(Species):
    #abilities['brawn'] -= 1
    #abilities['cunning'] += 1
    #wound_threshold = 10 + abilities['brawn']
    #strain_threshold = 11 + abilities['willpower']
    #xp = 100

    #general_skills['streetwise'] += 1
    #talents.append('convincing_demeanor')


#class Duros(Species):
    #abilities['brawn'] -= 1
    #abilities['intellect'] += 1
    #wound_threshold = 11 + abilities['brawn']
    #starin_threshold = 10 + abilities['willpower']
    #xp = 100

    #general_skills['piloting (space)'] += 1


#class Gran(Species):
    #abilities['cunning'] -= 1
    #abilities['presence'] += 1
    #wound_threshold = 10 + abilities['brawn']
    #strain_threshold = 9 + abilities['willpower']

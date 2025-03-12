intro = ['Once upon a time,', 'There was a great nation known as the Even More United States of America, or EMUSA', 
         'The nation lived harmonously, with citizens of all different species and creeds living peacefully amongst each other,', 
         'until the day the constitution was split across the land.', 'Chaos erupted as regional leaders took the pages of the constitution for themselves for power and glory.', 
         'For days it seemed like EMUSA was going to meet its end', 'until...', 
         'A heroic intern alongside the very witty and attractive voice in his head fought the leaders and reunited the constitution',
         "They held grand festival in the intern's honor, unifying the country once again.", "It's almost been a year since that intern's quest for the country.", 'Well, I should say, it has almost been a year since YOUR quest for the country.',
         "Also don't forget how I, the voice in your head, helped you out.", "That's besides the point.", 'The point is that the country, yet again, finds itself divided.', 
         'The North Pole, Spookyland, The Mythical State of North Dakota, and the planet Vorlum are fighting over who gets to hold the festival celebrating your victory this year!', 'In a panic, President Daniel Smithson has organized a tournament.',
         'Whoever wins the tournament, their region gets to host the festival,', 'and you get to choose who fights!', "Now, let's see how this tournament goes!"]

tutorial = ["Oh,", 'yeah.', "It's almost been a year since you last battled.", 'You might need a refresher.', 'You see, alongside having to manage your health,', 'you gotta manage your nerves.', "If you have low nerves, you'll likely fail your attacks",
            'On the other hand,', "if you have high nerves, you're more likely to hit an attack really well.", 'Fighters with high amounts of bravery have higher amounts of nerves than most.', 
            "Also, you didn't have to worry about this but in arena settings, means a ton.", 'If you have more speed than your opponent, you get to go first.', "If you have the same amount of speed as your opponent, it's basically a coin flip as to who goes first.",
            "Since there are no items in this arena setting, that's all there is!", 'Feel refreshed?']

classes = [
    {
        'name': 'Elf',
        'brief': 'Damage Dealing',
        'description': 'Elves are small and fiesty. They may be easy to underestimate but trust me. You do not want to mess with an elf.',
        'alligence': 'The North Pole',
        'attacks': [
            {
                'name': 'Christmas Blast',
                'damage': 25,
                'discomfort': 0,
                'target_self': False,
                'super_effective': ['0'],
                'effective': ['1'],
                'failure': ['2'],
                'super_failure': ['3']
            },
            {
                'name': 'Coal',
                'damage': 0,
                'discomfort': 15,
                'target_self': False,
                'super_effective': ['After a quick sign, Santa N. Claus himself jumps into the arena and personally hands their opponent a lump of coal.', 'Santa Claus then pulls out a piece of piece of paper and a microscope', 'He puts the paper under the microscope',
                                    '"Hohoho, it seems like you are on my naughty list"', "Their opponent's eyes widen in shock", 'They kneel down, and with tears in their eyes, beg and plead for forgivness', 'Santa Claus silently shakes his head and leaves the arena.'],
                'effective': ['They deliver a lump of coal to their opponent', 'From what it seems, their opponent has ended up on the naughty list.', 'Their opponent cries, devastated that they will not be getting the Playbox 5 they asked for this Christmas.'],
                'failure': ['They just chuck the coal at their opponent.', 'Their opponent is too dazed to realize that they are on the naughty list.'],
                'super_failure': ['After a quick sign, Santa N. Claus himself jumps into the arena and personally hands their opponent a lump of coal', 'Santa Claus then pulls out a piece of piece of paper and a microscope', 'He puts the paper under the microscope',
                                  'He looks confused and readjusts the microscope.', '"Hohoho, it seems like there has been a mistake."', '"You are not on the naughty list"', 'Santa shrugs and walks away.']
            },
            {
                'name': 'Candy Cane',
                'damage': -15,
                'discomfort': 0,
                'target_self': True,
                'super_effective': ['0'],
                'effective': ['1'],
                'failure': ['2'],
                'super_failure': ['3']
            },
            {
                'name': 'Falcon Punch',
                'damage': 1000,
                'discomfort': 0,
                'target_self': False,
                'super_effective': ['0'],
                'effective': ['1'],
                'failure': ['2'],
                'super_failure': ['3']
            }
        ]
    },
    #{
    #    'name': 'Skeleton',
    #    'brief': 'Causing Nervousness',
    #    'description': 'AAAAAA! Sorry, got a little spooked. Skeletons are terrifying creatures but do not worry, they are very weak.',
    #    'alligence': 'Spookyland',
    #    'attacks': [{
    #        'name': 'Shin Kick',
    #        'damage': 20,
    #        'discomfort': 0,
    #    }]
    #}
]
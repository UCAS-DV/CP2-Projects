classes = [
    {
        'name': 'Elf',
        'brief': 'Brawler',
        'description': 'Elves are small and fiesty. They may be easy to underestimate but trust me. You do not want to mess with an elf.',
        'alligence': 'The North Pole',
        'attacks': [
            {
                'name': 'Christmas Blast',
                'damage': 25,
                'discomfort': 0,
                'target_self': True,
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
                'super_effective': ['0'],
                'effective': ['1'],
                'failure': ['2'],
                'super_failure': ['3']
            },
            {
                'name': 'Candy Cane',
                'damage': -15,
                'discomfort': 0,
                'target_self': False,
                'super_effective': ['0'],
                'effective': ['1'],
                'failure': ['2'],
                'super_failure': ['3']
            }
        ]
    },
    {
        'name': 'Skeleton',
        'brief': 'Scarer',
        'description': 'AAAAAAAAAAAAAAAAAAAAAAAA! Sorry, got a little spooked. Skeletons are terrifying creatures but do not worry, they are very weak.',
        'alligence': 'Spookyland',
        'attacks': [{
            'name': 'Shin Kick',
            'damage': 20,
            'discomfort': 0,
        }]
    }
]
from model import Creature


_creature: list[Creature] = [

    Creature(   name="yeti",
                country="CN",
                area="Himalayas",
                description="Hirsute Himalayan",
                aka="Abominable Snowman"
 ),
    Creature(   name="sasquatch",
                country="US",
                area="*",
                description="Yeti's Cousin Eddie",
                aka="Bigfoot")
]
def get_creature() -> list[Creature]:
    return _creature


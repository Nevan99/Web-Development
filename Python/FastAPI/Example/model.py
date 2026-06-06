from pydantic import BaseModel


class Creature(BaseModel):
    name: str
    country: str 
    area: str
    description: str
    aka: str 

if __name__ == "__main__":
    # This code only runs when model.py is executed directly, not when imported
    thing = Creature(name = "yeti",
                   country = "Chinese",
                   area = "Himalayas", 
                   description = "Hirsute Himalayan",
                   aka = "Abominable Snowman")
    
    print("Name is: ", thing.name)

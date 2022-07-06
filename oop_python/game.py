from character import character
# import random
tarig = character ("tarig","Space-Traveler")
tarig.set_power("teleportation")
man = character ("Man", "Super-MAN")
man.set_power("superMAn")
man.set_power("fly")
print(f"{tarig.name} is actually the superhero {tarig.super} and his power is {tarig.power}")
print(f"{man.name} is actually the superhero {man.super}")

tarig.get_power()
man.get_power()
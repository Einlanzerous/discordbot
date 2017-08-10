from random import randint


def generate(res):
    points = res
    weapon = ""
    variant = ""
    shells = ""
    size = ""
    mods = ""

    if (points >= 5):
        arms_level = 5
    elif (points == 4):
        arms_level = 4
    elif (points == 3):
        arms_level = 3
    elif (points == 2):
        arms_level = 2
    elif (points == 1):
        arms_level = 1
    else:
        return "Invalid resource level given"

    arms_type = randint(0, 12)

    if (arms_type == 0):
        weapon = "Pistol"
    elif (arms_type == 1):
        weapon = "Submachine Gun"
    elif (arms_type == 2):
        weapon = "Rifle"
    elif (arms_type == 3):
        weapon = "Swarm Drone"
    elif (arms_type == 4):
        weapon = "Combat Drone"
    elif (arms_type == 5):
        weapon = "Puncture Rifle"
    elif (arms_type == 6):
        weapon = "Assault Rifle"
    elif (arms_type == 7):
        weapon = "Assault Drone"
    elif (arms_type == 8):
        weapon = "Sniper Rifle"
    elif (arms_type == 9):
        weapon = "Disruptor Rifle"
    elif (arms_type == 10):
        weapon = "Cannon"
    elif (arms_type == 11):
        weapon = "Auto-Canon"
    elif (arms_type == 12):
        chemical = randint(0, 4)

        if (chemical == 0):
            weapon = "Chemical Thrower (Cryo-Gel)"
        elif (chemical == 1):
            weapon = "Chemical Thrower (Napalm)"
        elif (chemical == 2):
            weapon = "Chemical Thrower (Synthetic Poison)"
        elif (chemical == 3):
            weapon = "Chemical Thrower (Antimonic Acid)"
        elif (chemical == 4):
            weapon = "Chemical Thrower (Neurotoxin)"

    variantN = randint(0, 10)

    if (variantN == 0):
        variant = "Burst Spores"
    elif (variantN == 1):
        variant = "Gauss"
    elif (variantN == 2):
        variant = "Ion"
    elif (variantN == 3):
        variant = "Irradiated"
    elif (variantN == 4):
        variant = "Particle"
    elif (variantN == 5):
        variant = "Rail"
    elif (variantN == 6):
        variant = "Self-Propelled"
    elif (variantN == 7):
        variant = "Spine Launcher"
    elif (variantN >= 8):
        variant = "Standard"

    shellsN = randint(0, 10)

    if (shellsN == 0):
        shells = "Dispersion"
    elif (shellsN == 1):
        shells = "Dummy"
    elif (shellsN == 2):
        shells = "Electro-Gravity"
    elif (shellsN == 3):
        shells = "Kinetic"
    elif (shellsN == 4):
        shells = "Shrapnel"
    elif (shellsN == 5):
        shells = "Smoke"
    elif (shellsN == 6):
        shells = "Snare"
    elif (shellsN >= 7):
        shells = "Normal"

    mods = "no mods"

    return "" + size + " " + weapon + "- " + variant + " variant, with " + shells + " shells. Including " + mods + "."

print (generate(4))
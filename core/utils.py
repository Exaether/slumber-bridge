def calculate_level_keyFrame(phase, level: int):
    factor = level / phase["maxLevel"]
    minStats = phase["minStats"]
    maxStats = phase["maxStats"]

    stats = {
        "maxHP": round(
            minStats["maxHP"] + (maxStats["maxHP"] - minStats["maxHP"]) * factor
        ),
        "atk": round(minStats["atk"] + (maxStats["atk"] - minStats["atk"]) * factor),
        "def": round(minStats["def"] + (maxStats["def"] - minStats["def"]) * factor),
        "res": round(minStats["res"] + (maxStats["res"] - minStats["res"]) * factor),
        "cost": minStats["cost"],
        "baseAttackTime": minStats["baseAttackTime"],
        "respawnTime": minStats["respawnTime"],
        "taunt": minStats["taunt"],
    }

    return stats

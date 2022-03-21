import json
import os

from generate.mcuuid import MCUUID


def resummon_mcfunction() -> str:
    return os.path.join(
        os.getcwd(),
        "data",
        "banner",
        "functions",
        "load",
        "resummon.mcfunction",
    )


def summon_mcfunction() -> str:
    return os.path.join(
        os.getcwd(),
        "data",
        "banner",
        "functions",
        "load",
        "summon.mcfunction",
    )


def banners_mcfunction() -> str:
    return os.path.join(
        os.getcwd(),
        "data",
        "banner",
        "functions",
        "tick",
        "banners.mcfunction",
    )


def looking_at_json(file_name: str) -> str:
    return os.path.join(
        os.getcwd(),
        "data",
        "banner",
        "predicates",
        "looking_at",
        f"{file_name}.json",
    )


def teleport_mcfunction(folder_name: str) -> str:
    file_dir = os.path.join(
        os.getcwd(),
        "data",
        "banner",
        "functions",
        "locations",
        f"{folder_name}",
    )
    os.makedirs(file_dir, exist_ok=True)

    return os.path.join(file_dir, "teleport.mcfunction")


def title_mcfunction(folder_name: str) -> str:
    file_dir = os.path.join(
        os.getcwd(),
        "data",
        "banner",
        "functions",
        "locations",
        f"{folder_name}",
    )
    os.makedirs(file_dir, exist_ok=True)

    return os.path.join(file_dir, "title.mcfunction")


def tellraw_mcfunction(folder_name: str) -> str:
    file_dir = os.path.join(
        os.getcwd(),
        "data",
        "banner",
        "functions",
        "locations",
        f"{folder_name}",
    )
    os.makedirs(file_dir, exist_ok=True)

    return os.path.join(file_dir, "tellraw.mcfunction")


def looking_at_predicate(uuid_1: str, uuid_2: str) -> str:
    return f'[\n\t{{\n\t\t"condition": "minecraft:alternative",\n\t\t"terms": [\n\t\t\t{{\n\t\t\t\t"condition": "minecraft:entity_properties",\n\t\t\t\t"entity": "this",\n\t\t\t\t"predicate": {{\n\t\t\t\t\t"player": {{\n\t\t\t\t\t\t"looking_at": {{\n\t\t\t\t\t\t\t"type": "minecraft:villager",\n\t\t\t\t\t\t\t"nbt": "{{UUID:{uuid_1}}}"\n\t\t\t\t\t\t}}\n\t\t\t\t\t}}\n\t\t\t\t}}\n\t\t\t}},\n\t\t\t{{\n\t\t\t\t"condition": "minecraft:entity_properties",\n\t\t\t\t"entity": "this",\n\t\t\t\t"predicate": {{\n\t\t\t\t\t"player": {{\n\t\t\t\t\t\t"looking_at": {{\n\t\t\t\t\t\t\t"type": "minecraft:villager",\n\t\t\t\t\t\t\t"nbt": "{{UUID:{uuid_2}}}"\n\t\t\t\t\t\t}}\n\t\t\t\t\t}}\n\t\t\t\t}}\n\t\t\t}}\n\t\t]\n\t}}\n]'


if __name__ == "__main__":
    with open("locations.json") as json_file:
        locations = json.load(json_file)

    facing_coords = {
        "north": ("~0.2 ~-0.9 ~0.5", "~-0.2 ~-0.9 ~0.5", "0"),
        "east": ("~-0.5 ~-0.9 ~0.2", "~-0.5 ~-0.9 ~-0.2", "90"),
        "south": ("~0.2 ~-0.9 ~-0.5", "~-0.2 ~-0.9 ~-0.5", "-180"),
        "west": ("~0.5 ~-0.9 ~0.2", "~0.5 ~-0.9 ~-0.2", "-90"),
    }

    summon_template = "execute positioned {positioned} run summon minecraft:villager {facing} {{Silent: 1b, Invulnerable: 1b, UUID: {uuid}, NoAI: 1b, CanPickUpLoot: 0b, ActiveEffects: [{{Id: 14b, Amplifier: 0b, Duration: 20000000, ShowParticles: 0b}}], Offers: {{}}}}\n"
    banner_template = "execute at {uuid} if entity @s[distance=..10] at @s if predicate banner:looking_at/{area_name} run function banner:locations/{area_name}/title\n"

    for index, location in enumerate(locations):
        file_name: str = location["area_name"].lower().replace(" ", "_")
        rel_coords = facing_coords.get(location["facing"])
        villager_uuids = [MCUUID(), MCUUID()]

        with open(summon_mcfunction(), "w" if index == 0 else "a") as summon_file:
            summon_file.writelines(
                [
                    "" if index == 0 else "\n",
                    "# {} [{}]\n".format(
                        location["area_name"], location["facing"].title()
                    ),
                    summon_template.format(
                        positioned=location["location"],
                        facing=rel_coords[0],
                        uuid=villager_uuids[0].nbt,
                    ),
                    summon_template.format(
                        positioned=location["location"],
                        facing=rel_coords[1],
                        uuid=villager_uuids[1].nbt,
                    ),
                ]
            )

        with open(resummon_mcfunction(), "w" if index == 0 else "a") as summon_file:
            summon_file.writelines(
                [
                    "" if index == 0 else "\n",
                    "# {}\n".format(location["area_name"]),
                    "kill {}\n".format(str(villager_uuids[0])),
                    "kill {}\n".format(str(villager_uuids[1])),
                ]
            )

        with open(banners_mcfunction(), "w" if index == 0 else "a") as banner_file:
            banner_file.write(
                banner_template.format(
                    area_name=file_name,
                    uuid=str(villager_uuids[0]),
                )
            )

        with open(looking_at_json(file_name), "w") as looking_at_file:
            looking_at_file.write(
                looking_at_predicate(
                    villager_uuids[0].nbt,
                    villager_uuids[1].nbt,
                )
            )

        with open(teleport_mcfunction(file_name), "w") as teleport_file:
            teleport_file.write(
                "teleport @s {} {} 0\n".format(
                    location["location"],
                    rel_coords[2],
                )
            )

        with open(title_mcfunction(file_name), "w") as title_file:
            title_file.writelines(
                [
                    "title @s[scores={bn.title_cooldown=-1}] times 0 5 2\n",
                    'title @s title {"text":""}\n',
                    'title @s subtitle {{"text":"{}","color":"#ACFFA6","bold":true}}\n'.format(
                        location["area_name"]
                    ),
                    "execute as @s[scores={{mc.talked_to_villager=1..}}] run function banner:locations/{}/tellraw\n".format(
                        file_name
                    ),
                    "scoreboard players set @s bn.title_cooldown 10\n",
                ]
            )

        with open(tellraw_mcfunction(file_name), "w") as title_file:
            title_file.writelines(
                [
                    'tellraw @s {"text":"------------------------------------------","color":"#ACFFA6","bold":true}\n',
                    'tellraw @s {{"text":"{}","color":"#ACFFA6","bold":true,"italic":false}}\n'.format(
                        location["area_name"]
                    ),
                    'tellraw @s {"text":" "}\n',
                    'tellraw @s [{{"text":"\\u27a4 Main Builders: ","color":"#ACFFA6","bold":false,"italic":false}},{{"text":"{}","color":"#FFFFFF","bold":false,"italic":false}}]\n'.format(
                        ", ".join(location["main_builders"])
                    )
                    if len(location["main_builders"]) > 0
                    else 'tellraw @s {"text":" "}\n',
                    'tellraw @s [{{"text":"\\u27a4 Contributors: ","color":"#ACFFA6","bold":false,"italic":false}},{{"text":"{}","color":"#FFFFFF","bold":false,"italic":false}}]\n'.format(
                        ", ".join(location["contributors"])
                    )
                    if len(location["contributors"]) > 0
                    else 'tellraw @s {"text":" "}\n',
                    'tellraw @s {"text":" "}\n',
                    'tellraw @s {{"text":"{}","color":"#FFF4D9","bold":false,"italic":true}}\n'.format(
                        location["description"][0]
                    )
                    if len(location["description"]) > 0
                    else 'tellraw @s {"text":" "}\n',
                    'tellraw @s {{"text":"{}","color":"#FFF4D9","bold":false,"italic":true}}\n'.format(
                        location["description"][1]
                    )
                    if len(location["description"]) > 1
                    else 'tellraw @s {"text":" "}\n',
                    'tellraw @s {{"text":"{}","color":"#FFF4D9","bold":false,"italic":true}}\n'.format(
                        location["description"][2]
                    )
                    if len(location["description"]) > 2
                    else 'tellraw @s {"text":" "}\n',
                    'tellraw @s {"text":"------------------------------------------","color":"#ACFFA6","bold":true}\n',
                ]
            )

    # Append resummon command to end of resummon function
    with open(resummon_mcfunction(), "a") as summon_file:
        summon_file.writelines(
            [
                "\n# Reload Datapack [5s Delay]\n",
                "schedule function banner:load/summon 5s replace\n",
            ]
        )

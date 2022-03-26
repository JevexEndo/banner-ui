import json
import os
from typing import Optional

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


def particles_mcfunction() -> str:
    return os.path.join(
        os.getcwd(),
        "data",
        "banner",
        "functions",
        "tick",
        "particles.mcfunction",
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


def teleport_mcfunction(folder_name: str, teleport_id: Optional[int] = None) -> str:
    file_dir = os.path.join(
        os.getcwd(),
        "data",
        "banner",
        "functions",
        "locations",
        f"{folder_name}",
    )
    os.makedirs(file_dir, exist_ok=True)

    function_name = "teleport{}.mcfunction".format(
        f"_{teleport_id}" if teleport_id is not None else ""
    )
    return os.path.join(file_dir, function_name)


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

    facing_adjustments = {
        "north": ("~0.2 ~-0.9 ~0.5", "~-0.2 ~-0.9 ~0.5", "0"),
        "east": ("~-0.5 ~-0.9 ~0.2", "~-0.5 ~-0.9 ~-0.2", "90"),
        "south": ("~0.2 ~-0.9 ~-0.5", "~-0.2 ~-0.9 ~-0.5", "-180"),
        "west": ("~0.5 ~-0.9 ~0.2", "~0.5 ~-0.9 ~-0.2", "-90"),
    }

    summon_template = "execute in {dimension} positioned {positioned} run summon minecraft:villager {facing} {{Silent: 1b, Invulnerable: 1b, UUID: {uuid}, NoAI: 1b, CanPickUpLoot: 0b, ActiveEffects: [{{Id: 14b, Amplifier: 0b, Duration: 20000000, ShowParticles: 0b}}], Offers: {{}}}}\n"
    banner_template = "execute at {uuid} if entity @s[distance=..10] at @s if predicate banner:looking_at/{area_name_id} run function banner:locations/{area_name}/title\n"
    particle_template = "execute in {dimension} run particle minecraft:glow {coordinates} 0.2 0.5 0.2 0 1 normal\n"

    for index, location in enumerate(locations):
        file_name: str = (
            "".join(
                char for char in location["area_name"] if char.isalnum() or char == " "
            )
            .lower()
            .replace(" ", "_")
        )
        villager_uuids = [MCUUID() for _ in range(len(location["banners"]) * 2)]

        with open(summon_mcfunction(), "w" if index == 0 else "a") as summon_file:
            summon_file.writelines(
                [
                    "" if index == 0 else "\n",
                    "# {}\n".format(location["area_name"]),
                ]
            )

            for count, banner in enumerate(location["banners"]):
                rel_coords = facing_adjustments.get(banner["facing"])
                summon_file.writelines(
                    [
                        summon_template.format(
                            dimension=banner["dimension"],
                            positioned=banner["coordinates"],
                            facing=rel_coords[0],
                            uuid=villager_uuids[count * 2].nbt,
                        ),
                        summon_template.format(
                            dimension=banner["dimension"],
                            positioned=banner["coordinates"],
                            facing=rel_coords[1],
                            uuid=villager_uuids[count * 2 + 1].nbt,
                        ),
                    ]
                )

        with open(resummon_mcfunction(), "w" if index == 0 else "a") as summon_file:
            summon_file.writelines(
                [
                    "" if index == 0 else "\n",
                    "# {}\n".format(location["area_name"]),
                ]
            )

            for count, banner in enumerate(location["banners"]):
                summon_file.writelines(
                    [
                        "kill {}\n".format(str(villager_uuids[count * 2])),
                        "kill {}\n".format(str(villager_uuids[count * 2 + 1])),
                    ]
                )

        with open(banners_mcfunction(), "w" if index == 0 else "a") as banner_file:
            for count, banner in enumerate(location["banners"]):
                banner_file.write(
                    banner_template.format(
                        area_name_id=f"{file_name}_{count+1}"
                        if len(location["banners"]) > 1
                        else file_name,
                        area_name=file_name,
                        uuid=str(villager_uuids[count * 2]),
                    )
                )

        with open(particles_mcfunction(), "w" if index == 0 else "a") as particle_file:
            for count, banner in enumerate(location["banners"]):
                particle_file.write(
                    particle_template.format(
                        dimension=banner["dimension"],
                        coordinates=banner["coordinates"],
                    )
                )

        for count, banner in enumerate(location["banners"]):
            banner_id = count + 1 if len(location["banners"]) > 1 else None

            with open(
                looking_at_json(
                    "{}{}".format(
                        file_name, f"_{banner_id}" if banner_id is not None else ""
                    )
                ),
                "w",
            ) as looking_at_file:
                looking_at_file.write(
                    looking_at_predicate(
                        villager_uuids[count * 2].nbt,
                        villager_uuids[count * 2 + 1].nbt,
                    )
                )

            with open(teleport_mcfunction(file_name, banner_id), "w") as teleport_file:
                teleport_file.write(
                    "execute in {} run teleport @s {} {} 0\n".format(
                        banner["dimension"],
                        banner["coordinates"],
                        facing_adjustments.get(banner["facing"])[2],
                    )
                )

        with open(title_mcfunction(file_name), "w") as title_file:
            title_file.writelines(
                [
                    "title @s[scores={bn.title_cooldown=-1}] times 0 5 2\n",
                    'title @s title {"text":""}\n',
                    'title @s subtitle {{"text":"{}","color":"{}","bold":true}}\n'.format(
                        location["area_name"],
                        location.get("color", "#ACFFA6")
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
                    'tellraw @s {{"text":"{}{}","color":"{}","bold":true,"italic":false}}\n'.format(
                        location["area_name"],
                        " - " + location["objective"]
                        if len(location["objective"]) > 0
                        else "",
                        location.get("color", "#ACFFA6")
                    ),
                    'tellraw @s {"text":" "}\n',
                    'tellraw @s [{{"text":"\\u27a4 Creators: ","color":"#ACFFA6","bold":false,"italic":false}},{{"text":"{}","color":"#FFFFFF","bold":false,"italic":false}}]\n'.format(
                        ", ".join(location["creators"])
                    )
                    if len(location["creators"]) > 0
                    else 'tellraw @s {"text":" "}\n',
                    'tellraw @s [{{"text":"\\u27a4 Contributors: ","color":"#ACFFA6","bold":false,"italic":false}},{{"text":"{}","color":"#FFFFFF","bold":false,"italic":false}}]\n'.format(
                        ", ".join(location["contributors"])
                    )
                    if len(location["contributors"]) > 0
                    else 'tellraw @s {"text":" "}\n',
                    'tellraw @s {"text":" "}\n'
                    if len(location["creators"]) <= 5
                    else "",
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

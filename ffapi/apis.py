from .models import Esper
from time import sleep



GAME_INFORMATIONS = {
    "characters": {
        "vaan": {
            "name": "Vaan",
            "race": "Human",
            "hometown": "Rabanastre",
            "age": "17",
            "type": "Principal"
            },
        "balthier": {
            "name": "Balthier",
            "race": "Human",
            "hometown": "Archades",
            "age": "22",
            "type": "Principal"
        }
        ,
        "penelo": {
            "name": "Penelo",
            "race": "Human",
            "hometown": "Rabanastre",
            "age": "16",
            "type": "Principal"
        }
        ,
        "fran": {
            "name": "Fran",
            "race": "Viera",
            "hometown": "Eruyt Village",
            "age": "Desconhecida",
            "type": "Principal"
        }
        ,
        "basch": {
            "name": "Basch",
            "race": "Human",
            "hometown": "Republic of Landis",
            "age": "36",
            "type": "Principal"
        }
        ,
        "ashe": {
            "name": "Ashe",
            "race": "Human",
            "hometown": "Rabanastre",
            "age": "19",
            "type": "Principal"
        }
        ,
        "reddas": {
            "name": "Reddas",
            "race": "Human",
            "hometown": "Desconhecido",
            "age": "33",
            "type": "Guest"
        }
        ,
        "vossler": {
            "name": "Vossler",
            "race": "Human",
            "hometown": "Rabanastre",
            "age": "38",
            "type": "Guest"
        }
        ,
        "larsa": {
            "name": "Larsa",
            "race": "Human",
            "hometown": "Archades",
            "age": "12",
            "type": "Guest"
        }
        ,
        "reks": {
            "name": "Reks",
            "race": "Human",
            "hometown": "Rabanastre",
            "age": "17",
            "type": "Guest"
        }
        ,
        "vayne": {
            "name": "Vayne Carudas Solidor",
            "race": "Human",
            "hometown": "Archadia",
            "age": "27",
            "type": "Antagonist"
        },
        "cid": {
            "name": "Cidolfus Demen Bunansa",
            "race": "Human",
            "hometown": "Archadia",
            "age": "58",
            "type": "Antagonist"
        },
        "venat": {
            "name": "Venat",
            "race": "Occuria",
            "hometown": "Unknow",
            "age": "Unknow",
            "type": "Antagonist"
        },
        "bagamnan": {
            "name": "Ba'Gamnan",
            "race": "Bangaa",
            "hometown": "Archadia",
            "age": "Unknow",
            "type": "Antagonist"
        }
    },
    "espers": {
        "belias": {
            "name": "Belias, the Gigas",
            "sign": "Aries, the Ram",
            "element": "Fire"
        },
        "chaos": {
            "name": "Chaos, Walker of the Wheel",
            "sign": "Tauros, the Bull",
            "element": "Wind"
        },
        "zalera": {
            "name": "Zalera, the Death Seraph",
            "sign": "Gemini, the Twins",
            "element": "Death"
        },
        "zeromus": {
            "name": "Zeromus, the Condemner",
            "sign": "Cancer, the Crab",
            "element": "Gravity"
        },
        "hashmal": {
            "name": "Hashmal, Bringer of Order",
            "sign": "Leo, the Lion",
            "element": "Earth"
        },
        "exodus": {
            "name": "Exodus, the Judge-Sal",
            "sign": "Libra, the Scales",
            "element": "Aether"
        },
        "ultima": {
            "name": "Ultima, the High Seraph",
            "sign": "Virgo, the Virgin",
            "element": "Holy"
        },
        "cuchulainn": {
            "name": "Cúchulainn, the Impure",
            "sign": "Scorpio, the Scorpion",
            "element": "Poison"
        },
        "shemhazai": {
            "name": "Shemhazai, the Whisperer",
            "sign": "Sagittarius, the Archer",
            "element": "Soul"
        },
        "famfrit": {
            "name": "Famfrit, the Darkening Cloud",
            "sign": "Aquarius, the Water Bearer",
            "element": "Water"
        },
        "mateus": {
            "name": "Mateus, the Corrupt",
            "sign": "Pisces, the Fish",
            "element": "Ice"
        },
        "adrammelech": {
            "name": "Adrammelech, the Wroth",
            "sign": "Capricorn, the Goat",
            "element": "Lightning"
        },
        "zodiark": {
            "name": "Zodiark, Keeper of Precepts",
            "sign": "Ophiuchus, the Snake Bearer",
            "element": "Darkness"
        }
    }
}


def salvaresp():
    a = GAME_INFORMATIONS['espers']
    for i, esper in enumerate(a):
        print(esper)
        print(a[esper])
        newesper = Esper(
            name_esper=a[esper],
            name=a[esper]['name'],
            sign=a[esper]['sign'],
            element=a[esper]['element']
        )
        newesper.save()
        print('salvei?\n\n\n')
        sleep(1)


bew = '111'
import asyncio
import bored_api
from translate import Translator

class BoredActivityGenerator:
    def __init__(self, to_lang=None, provider=None, secret=None):
        if to_lang is not None:
            self.to_lang = to_lang
            
            if provider is not None and secret is not None:
                if provider == "microsoft" or provider == "libretranslate" or provider == "mymemory":
                    if secret is not None:
                        self.translator = Translator(provider=provider, to_lang=to_lang, secret_access_key=secret)
                    else:
                        self.translator = None
            else:        
                self.translator = Translator(to_lang=to_lang)
        else:
            self.to_lang = None
            self.translator = None

        self.activity_types = [
            bored_api.ActivityType.BUSYWORK,
            bored_api.ActivityType.EDUCATION,
            bored_api.ActivityType.RECREATIONAL,
            bored_api.ActivityType.SOCIAL,
            bored_api.ActivityType.DIY,
            bored_api.ActivityType.CHARITY,
            bored_api.ActivityType.COOKING,
            bored_api.ActivityType.RELAXATION,
            bored_api.ActivityType.MUSIC
        ]

        self.activity_types_mappings = {
            "de": {
                "BUSYWORK": "Beschäftigung",
                "EDUCATION": "Bildung",
                "RECREATIONAL": "Freizeit",
                "SOCIAL": "Soziales",
                "DIY": "DIY",
                "CHARITY": "Wohltätigkeit",
                "COOKING": "Kochen",
                "RELAXATION": "Entspannung",
                "MUSIC": "Musik"
            },
            "en": {
                "BUSYWORK": "Busywork",
                "EDUCATION": "Education",
                "RECREATIONAL": "Recreational",
                "SOCIAL": "Social",
                "DIY": "DIY",
                "CHARITY": "Charity",
                "COOKING": "Cooking",
                "RELAXATION": "Relaxation",
                "MUSIC": "Music"
            },
            "fr": {
                "BUSYWORK": "Emploi",
                "EDUCATION": "Éducation",
                "RECREATIONAL": "Loisirs",
                "SOCIAL": "Social",
                "DIY": "Bricolage",
                "CHARITY": "Charité",
                "COOKING": "Cuisine",
                "RELAXATION": "Détente",
                "MUSIC": "Musique"
            },
            "es": {
                "BUSYWORK": "Empleo",
                "EDUCATION": "Educación",
                "RECREATIONAL": "Ocio",
                "SOCIAL": "Vida social",
                "DIY": "Bricolaje",
                "CHARITY": "Caridad",
                "COOKING": "Cocina",
                "RELAXATION": "Relajación",
                "MUSIC": "Música"
            }
        }

        self.client = bored_api.BoredClient()

    async def get_random_activity(self, activity_type):
        activity = await self.client.get_by_type(activity_type)
        return activity.activity

    async def generate_activities(self):
        activities = {}
        for activity_type in self.activity_types:
            activity = await self.get_random_activity(activity_type)
            if self.translator:
                if self.to_lang in self.activity_types_mappings.keys():
                    activities[self.activity_types_mappings[self.to_lang][activity_type.name]] = self.translator.translate(activity)
                else:
                    activities[activity_type.name] = self.translator.translate(activity)
            else:
                activities[activity_type.name] = activity
        return activities

async def main(to_lang=None, provider=None, secret=None):
    activity_generator = BoredActivityGenerator(to_lang)
    activities = await activity_generator.generate_activities()

    for activity_type, activity in activities.items():
        print("{}: {}".format(activity_type, activity))

if __name__ == "__main__":
    pass
    #asyncio.run(main())
    #asyncio.run(main("de"))

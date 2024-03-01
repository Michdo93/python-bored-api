# python-bored-api
A Python script accessing the Bored API with translations.

You can use the Azure AI Translator from Microsoft, Translate from MyMemory or LibreTranslate to translate in any language. But you may have to register with one of these providers in order to use the translation. MyMemory is used by default and is the free version. Better results can be achieved by registering.

Bored API otherwise only returns English results by default.

The programme code even contains fixed translations for the categories in German, English, French and Spanish. This is not translated by the Translator because it would otherwise take longer for the result to be returned. Nothing changes in the categories and each translation could otherwise lead to different results.

Further Informations to the `translate` Module you can finde [here](https://translate-python.readthedocs.io/en/latest/index.html) and about the Bored API you can find [here](http://www.boredapi.com/).

## Pre-Installation

You have to install via pip:

```
pip install asyncio
pip install bored-api
pip install translate
```

## Usage

You have to run:

```
python bored.py
```

As example you will receive:

```
BUSYWORK: Create or update your resume
EDUCATION: Research a topic you're interested in
RECREATIONAL: Go to the gym
SOCIAL: Catch up with a friend over a lunch date
DIY: Find a DIY to do
CHARITY: Contribute code or a monetary donation to an open-source software project
COOKING: Create a meal plan for the coming week
RELAXATION: Take a bubble bath
MUSIC: Learn to play a new instrument

Beschäftigung: Sichern wichtiger Computerdateien
Bildung: Lernen Sie Express.js
Freizeit: Yoga machen
Soziales: Machen Sie eine Fotosession mit ein paar Freunden
DIY: Lernen Sie Holzbearbeitung
Wohltätigkeit: Leiste Freiwilligenarbeit in deiner lokalen Speisekammer
Kochen: Erstelle ein Kochbuch mit deinen Lieblingsrezepten
Entspannung: Sitzen Sie im Dunkeln und hören Sie Ihre Lieblingsmusik ohne Ablenkungen
Musik: Schreibe ein Lied!
```

What you need to bear in mind: Every request to Bored API returns different results. You can see that the results for English and German have been completely regenerated here. Since the `translate` module is already installed, if you want to have the same result translated in several languages, you could rewrite the programme and perform several translations in the main method. For me, this is not desirable as I want to generate random results each time.

## Customization:

```
# English without "translate" the categories
asyncio.run(main())

## Translations with category translation
# English to English translation
asyncio.run(main("en"))

# English to German translation
asyncio.run(main("de"))

# English to French translation
asyncio.run(main("fr"))

# English to Spanish translation
asyncio.run(main("es"))

## Translations without category translation
# As example English to Czech translation
asyncio.run(main("cz"))

## Translations with provider
# Azure AI translator using a secret_access_key (oAuth Access Token)
asyncio.run(main("de", "microsoft", "********"))

# translate MyMemory using a valid email address
asyncio.run(main("de", "mymemory", "********"))

# LibreTranslate using a secret_access_key (oAuth Access Token)
asyncio.run(main("de", "libretranslate", "********"))
```

Further informations [here](https://translate-python.readthedocs.io/en/latest/providers.html).

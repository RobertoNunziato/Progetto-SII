def reformat(survey):
    json = {}
    for key in survey:
        preferences = []
        for index in range(0,len(survey[key])):
            preferences.append(survey[key][index])
        json[str(key)] = preferences
    return json

def buildPreferences(preferences):
    list = []
    # Caso 1: ci sono piu' preferenze
    if "," in preferences:
        preferencesArray = preferences.split(",")
        for index in range(len(preferencesArray)):
            list.append(preferencesArray[index])
    # Caso 2: c'e' una sola preferenza
    else:
        list.append(preferences)

    return list

def buildPersonality(personality):
    list = []
    personalityArray = personality.split(",")
    for index in range(len(personalityArray)):
        list.append(personalityArray[index])

    return list
def estimate_state(features):


    buddhi = features["average_score"]


    smriti = features["revision_count"]


    dharana = features["total_time"]


    shila = features["consistency"]


    karma = min(
        features["activity_count"] / 20,
        1
    )


    viveka = (
        buddhi
        +
        shila
    ) / 2


    manasika = (
        dharana
        +
        shila
    ) / 2


    adaptability = (
        buddhi
        +
        karma
    ) / 2


    ruchi = (
        features["activity_count"] / 10
    )

    if ruchi > 1:
        ruchi = 1


    # Guna estimation

    sattva = (
        buddhi
        +
        shila
        +
        viveka
    ) / 3


    rajas = (
        karma
        +
        adaptability
    ) / 2


    tamas = 1 - (
        (sattva + rajas) / 2
    )


    if sattva >= rajas and sattva >= tamas:

        guna = "sattva"


    elif rajas >= sattva and rajas >= tamas:

        guna = "rajas"


    else:

        guna = "tamas"



    return {

        "buddhi": buddhi,

        "smriti": smriti,

        "dharana": dharana,

        "guna": guna,


        "sattva": sattva,

        "rajas": rajas,

        "tamas": tamas,


        "shila": shila,

        "karma": karma,

        "manasika": manasika,

        "viveka": viveka,

        "ruchi": ruchi,

        "adaptability": adaptability

    }
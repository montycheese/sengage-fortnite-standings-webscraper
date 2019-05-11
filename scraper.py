__author__ = 'montanawong'

import requests, json

BASE_URL = "https://5cyv1uh1f2.execute-api.us-east-1.amazonaws.com/Prod"
REGION_CODE_TO_REGION = {
    0 : "NAEAST",
    #1 : "NAWEST",
    #2 : "EUROPE",
    #3: "OCEANIA",
    #4: "ASIA",
    #5: "BRAZIL"
}

REGIONS = [
    "NAEAST",
    "NAWEST",
    "EUROPE",
    "OCEANIA",
    "ASIA",
    "BRAZIL"
]


def main():
    week = int(input("Input week to send >> "))
    solos = bool(input("Solo? True/False>> "))
    region_to_standings = dict()
    #all_standings = []
    for region in REGIONS:
        filename = "standings/week%d-%s.txt" % (week, region)
        with open(filename) as f:
            standings = json.loads(f.read())
            for standing in standings:
                standing["solos"] = solos
                standing["currencySymbol"] = "USD"
                standing["week"] = week
                standing["name1"] = standing["name"]
                standing["region"] = region
                standing.pop("name")
                # todo refactor other model for duos
            #region_to_standings[region] = standings
            requests.put("%s/standings" % BASE_URL, data=json.dumps({"standings" : standings}))

                #all_standings.append(standing)


if __name__ == "__main__":
    main()

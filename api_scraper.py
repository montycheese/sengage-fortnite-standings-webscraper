__author__ = 'montanawong'

import requests, json

URL_TEMPLATE = "https://www.epicgames.com/fortnite/competitive/api/leaderboard/epicgames_OnlineOpen_Week%d_%s/OnlineOpen_Week%d_%s_Event2"
SENGAGE_API_URL = "https://5cyv1uh1f2.execute-api.us-east-1.amazonaws.com/Prod"

REGION_CODE_TO_REGION = {
    "NAE": "NAEAST",
    "NAW": "NAWEST",
    "EU": "EUROPE",
    "OCE": "OCEANIA",
    "ASIA": "ASIA",
    "BR": "BRAZIL"
}


def main():
    week = int(input("Input week to send >> "))
    solos = input("Solo? True/False>> ") == "True"
    for k, v in REGION_CODE_TO_REGION.items():
        standings = []
        url = URL_TEMPLATE % (week, k, week, k)
        print("Fetching Standings from EPIC for Week %d, Region %s" % (week, v))
        request = requests.get(url)
        content = json.loads(request.text)
        entries = content["entries"]
        for entry in entries:
            standing = dict()
            standing["name1"] = entry["displayNames"][0]
            if solos == False:
                standing["name2"] = entry["displayNames"][1]
            standing["region"] = v
            standing["week"] = week
            standing["rank"] = int(entry["rank"])
            standing["solos"] = solos
            try:
                standing["prize"] = int(entry["payout"]["quantity"])
                standing["currencySymbol"] = entry["payout"]["value"]
            except KeyError:
                print("No payout for entry: " + str(entry["displayNames"]))
            standing["points"] = int(entry["pointsEarned"])
            standings.append(standing)
        print("Sending %d standings to server" % len(standings))
        requests.put("%s/standings" % SENGAGE_API_URL, data=json.dumps({"standings" : standings}))



if __name__ == "__main__":
    main()

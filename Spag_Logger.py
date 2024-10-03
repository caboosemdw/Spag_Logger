# Import Statements
import os
from dotenv import load_dotenv
from datetime import datetime
from datetime import timedelta
from urllib.request import Request, urlopen
import gspread
import json
import ssl

# Start of Main() Funcion
def main():
    # Initialize some variables
    timeshift = 5+(2/86400)
    now = datetime.now()+timedelta(hours=timeshift)
    prefix = now.strftime("%Y%m%d_%H%M%S")
    myDate = now.strftime("%Y%m%d")

    load_dotenv()
    APIkey = os.getenv('API')
    ServiceFile = os.getenv('SERVICE')
    Workbook = os.getenv('WB')
    MemberSheet = os.getenv('MemberDB')
    GuildSheet = os.getenv('GuildDB')

    # Pull the API Data and Guild Rankings Data
    ssl._create_default_https_context = ssl._create_unverified_context
    url2 = "https://lyrania.co.uk/api/rankings.php?cat=guilds"
    url4 = "https://lyrania.co.uk/api/guilds.php?type=all&api_code=" + str(APIkey) # Sketti

    response2 = urlopen(url2)
    guildRankings_json = json.loads(response2.read())
    guild_response = urlopen(url4)
    guild_data_json = json.loads(guild_response.read())

    # Parse the API Data into what needs to be kept
    membersJSON = guild_data_json['members']

    glevels = guildRankings_json[0]['level'][0] #guildname/level
    gbuildings = guildRankings_json[1]['buildings'][0] #guildname/buildings
    gboss = guildRankings_json[2]['highest_boss_killed'][0] #guildname/highest_boss_killed
    gdp = guildRankings_json[3]['dungeon_points'][0] #guildname/dungeon_points
    grp = guildRankings_json[4]['research_points'][0] #guildname/research_points
    amorbs = guildRankings_json[5]['amorbs'][0] #guildname/amorbs

    guildsToTrack = ['The Pantsless Guild','Anzac Cove','High Times','Phoenix','Dungeon Raiders','Erewhon','Spaghetti and Meatballs']
    guildsData = []
    for g in guildsToTrack:
        guildsData.append([myDate+'-'+g,myDate,g])

    tempData = []
    for y in range(len(guildsToTrack)):
        tempData.append(0)
    for x in glevels:
        if x['guildname'] == guildsToTrack[0]: tempData[0]=int(x['level'])
        if x['guildname'] == guildsToTrack[1]: tempData[1]=int(x['level'])
        if x['guildname'] == guildsToTrack[2]: tempData[2]=int(x['level'])
        if x['guildname'] == guildsToTrack[3]: tempData[3]=int(x['level'])
        if x['guildname'] == guildsToTrack[4]: tempData[4]=int(x['level'])
        if x['guildname'] == guildsToTrack[5]: tempData[5]=int(x['level'])
        if x['guildname'] == guildsToTrack[6]: tempData[6]=int(x['level'])

    for i in range(0,len(guildsToTrack)):
        guildsData[i].append(tempData[i])

    tempData = []
    for y in range(len(guildsToTrack)):
        tempData.append(0)
    for x in gbuildings:
        if x['guildname'] == guildsToTrack[0]: tempData[0]=int(x['buildings'])
        if x['guildname'] == guildsToTrack[1]: tempData[1]=int(x['buildings'])
        if x['guildname'] == guildsToTrack[2]: tempData[2]=int(x['buildings'])
        if x['guildname'] == guildsToTrack[3]: tempData[3]=int(x['buildings'])
        if x['guildname'] == guildsToTrack[4]: tempData[4]=int(x['buildings'])
        if x['guildname'] == guildsToTrack[5]: tempData[5]=int(x['buildings'])
        if x['guildname'] == guildsToTrack[6]: tempData[6]=int(x['buildings'])

    for i in range(0,len(guildsToTrack)):
        guildsData[i].append(tempData[i])

    tempData = []
    for y in range(len(guildsToTrack)):
        tempData.append(0)
    for x in gboss:
        if x['guildname'] == guildsToTrack[0]: tempData[0]=int(x['highest_boss_killed'])
        if x['guildname'] == guildsToTrack[1]: tempData[1]=int(x['highest_boss_killed'])
        if x['guildname'] == guildsToTrack[2]: tempData[2]=int(x['highest_boss_killed'])
        if x['guildname'] == guildsToTrack[3]: tempData[3]=int(x['highest_boss_killed'])
        if x['guildname'] == guildsToTrack[4]: tempData[4]=int(x['highest_boss_killed'])
        if x['guildname'] == guildsToTrack[5]: tempData[5]=int(x['highest_boss_killed'])
        if x['guildname'] == guildsToTrack[6]: tempData[6]=int(x['highest_boss_killed'])

    for i in range(0,len(guildsToTrack)):
        guildsData[i].append(tempData[i])

    tempData = []
    for y in range(len(guildsToTrack)):
        tempData.append(0)
    for x in gdp:
        if x['guildname'] == guildsToTrack[0]: tempData[0]=int(x['dungeon_points'])
        if x['guildname'] == guildsToTrack[1]: tempData[1]=int(x['dungeon_points'])
        if x['guildname'] == guildsToTrack[2]: tempData[2]=int(x['dungeon_points'])
        if x['guildname'] == guildsToTrack[3]: tempData[3]=int(x['dungeon_points'])
        if x['guildname'] == guildsToTrack[4]: tempData[4]=int(x['dungeon_points'])
        if x['guildname'] == guildsToTrack[5]: tempData[5]=int(x['dungeon_points'])
        if x['guildname'] == guildsToTrack[6]: tempData[6]=int(x['dungeon_points'])

    for i in range(0,len(guildsToTrack)):
        guildsData[i].append(tempData[i])

    tempData = []
    for y in range(len(guildsToTrack)):
        tempData.append(0)
    for x in grp:
        if x['guildname'] == guildsToTrack[0]: tempData[0]=int(x['research_points'])
        if x['guildname'] == guildsToTrack[1]: tempData[1]=int(x['research_points'])
        if x['guildname'] == guildsToTrack[2]: tempData[2]=int(x['research_points'])
        if x['guildname'] == guildsToTrack[3]: tempData[3]=int(x['research_points'])
        if x['guildname'] == guildsToTrack[4]: tempData[4]=int(x['research_points'])
        if x['guildname'] == guildsToTrack[5]: tempData[5]=int(x['research_points'])
        if x['guildname'] == guildsToTrack[6]: tempData[6]=int(x['research_points'])

    for i in range(0,len(guildsToTrack)):
        guildsData[i].append(tempData[i])

    tempData = []
    for y in range(len(guildsToTrack)):
        tempData.append(0)
    for x in amorbs:
        if x['guildname'] == guildsToTrack[0]: tempData[0]=int(x['amorbs'])
        if x['guildname'] == guildsToTrack[1]: tempData[1]=int(x['amorbs'])
        if x['guildname'] == guildsToTrack[2]: tempData[2]=int(x['amorbs'])
        if x['guildname'] == guildsToTrack[3]: tempData[3]=int(x['amorbs'])
        if x['guildname'] == guildsToTrack[4]: tempData[4]=int(x['amorbs'])
        if x['guildname'] == guildsToTrack[5]: tempData[5]=int(x['amorbs'])
        if x['guildname'] == guildsToTrack[6]: tempData[6]=int(x['amorbs'])

    for i in range(0,len(guildsToTrack)):
        guildsData[i].append(tempData[i])

    membersDB = []
    guildMembers = []
    newData = []
    for m in membersJSON:
        newData.append(myDate+'-'+m['id']) # unique id
        newData.append(myDate) # date
        newData.append(int(m['id'])) # id
        newData.append(m['username']) # username
        newData.append(int(m['area'])) # area
        newData.append(int(m['gdp']['dp_donated'])) # gdp
        newData.append(int(m['rp']['donated'])) # rp
        newData.append(int(m['kills']['kills'])) # kills
        newData.append(m['id']+'-'+m['area'])
        newData.append(int(m['dungeontreasury']['treasurytaxed']))
        newData.append(int(m['dungeontreasury']['treasurydonated']))
        newData.append(int(m['dungeontreasury']['treasury_payout_RP']))
        newData.append(int(m['dungeontreasury']['treasury_payout_GDP']))
        newData.append(int(m['dungeontreasury']['treasury_chest_gains_plat']))
        newData.append(int(m['dungeontreasury']['treasury_chest_gains_tokens']))
        membersDB.append(newData)
        newData = []

    # Start the Connection to the Google Sheet, Initialize the workbook/worksheet variables
    sa = gspread.service_account(ServiceFile)
    db = sa.open(Workbook)
    memDB = db.worksheet(MemberSheet)
    gldDB = db.worksheet(GuildSheet)
    logSheet = db.worksheet('Log')

    # Load the Parsed Data into the SNM Spreadsheets
    memDB.clear_basic_filter()
    memDB.append_rows(membersDB)
    memDB.set_basic_filter()
    gldDB.append_rows(guildsData)
    logSheet.append_row([prefix])

if __name__ == '__main__':
    main()

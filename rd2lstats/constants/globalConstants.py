
# Contains the current week match ID's to parse stats for
match_ids = ["6972609178", "6972653463", "6972608535", "6972668772", "6972609005", "6972641234", "6972611355", "6972661890", "6972610409", "6972658565", "6972613182", "6972662571", "6972616806", "6972658535", "6972608549", "6972645753"]
current_week = 1

# permissionkey location - added in manually
permissionkeyfile = "../permissionkey.txt"

# Used for fetching Hero icon images in embeds
steam_cdn = "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/"

# Dotabuff base URL
dotabuff_url = "https://www.dotabuff.com/matches/"

# Opendota API URL
opendota_api_players_url = "https://api.opendota.com/api/players/"
opendota_api_matches_url = "https://api.opendota.com/api/matches/"

# Stats multipliers, these are slightly modified from Dota's fantasy point calculation
fantasy_kill_multiplier = 0.5
fantasy_death_multiplier = -0.5
fantasy_assist_multiplier = 0.3
fantasy_lasthit_multiplier = 0.003
fantasy_gpm_multiplier = 0.002
fantasy_ts_multiplier = 1
fantasy_roshan_multiplier = 1
fantasy_wards_planted = 0.1
fantasy_wards_dewarded = 0.3
fantasy_camps_stacked = 0.4
fantasy_runes_grabbed = 0.2
fantasy_first_blood = 4
fantasy_stuns_multiplier = 0.05

# Pos 1 constants
pos1directory = "../pos1stats/"
pos1currentdirectory = "../current_week_stats/pos1stats/"
pos1gpmfile = "pos1gpmLeaderboard.csv"
pos1kdafile = "pos1kdaLeaderboard.csv"
pos1fantasyfile = "pos1fantasyLeaderboard.csv"

# Pos 2 constants
pos2directory = "../pos2stats/"
pos2currentdirectory = "../current_week_stats/pos2stats/"
pos2gpmfile = "pos2gpmLeaderboard.csv"
pos2kdafile = "pos2kdaLeaderboard.csv"
pos2fantasyfile = "pos2fantasyLeaderboard.csv"

# Pos 3 constants
pos3directory = "../pos3stats/"
pos3currentdirectory = "../current_week_stats/pos3stats/"
pos3gpmfile = "pos3gpmLeaderboard.csv"
pos3kdafile = "pos3kdaLeaderboard.csv"
pos3fantasyfile = "pos3fantasyLeaderboard.csv"

# Pos 4 constants
pos4directory = "../pos4stats/"
pos4currentdirectory = "../current_week_stats/pos4stats/"
pos4gpmfile = "pos4gpmLeaderboard.csv"
pos4kdafile = "pos4kdaLeaderboard.csv"
pos4fantasyfile = "pos4fantasyLeaderboard.csv"

# Pos 5 constants
pos5directory = "../pos5stats/"
pos5currentdirectory = "../current_week_stats/pos5stats/"
pos5gpmfile = "pos5gpmLeaderboard.csv"
pos5kdafile = "pos5kdaLeaderboard.csv"
pos5fantasyfile = "pos5fantasyLeaderboard.csv"

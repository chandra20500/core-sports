import json
import os

working_directory = os.getcwd()

f = open(working_directory + '\\schema\\put\\configuration.json',)
configuration_schema = json.load(f)

f = open(working_directory + '\\schema\\put\\drill_rating.json',)
drill_rating_schema = json.load(f)

f = open(working_directory + "\\schema\\put\\drill_tag.json",)
drill_tag_schema = json.load(f)

f = open(working_directory + '\\schema\\put\\drill.json',)
drill_schema = json.load(f)

f = open(working_directory + '\\schema\\put\\event_participants.json',)
event_participants_drill_result_schema = json.load(f)

f = open(working_directory + '\\schema\\put\\event.json',)
event_schema = json.load(f)

f = open(working_directory + r'\\schema\\put\\favorite_drill.json',)
favorite_drill_schema = json.load(f)

f = open(working_directory + r'\\schema\\put\\feedback.json',)
feedback_schema = json.load(f)

f = open(working_directory + '\\schema\\put\\goal.json',)
goal_schema = json.load(f)

f = open(working_directory + '\\schema\\put\\league.json',)
league_schema = json.load(f)

f = open(working_directory + r'\\schema\\put\\note.json',)
note_schema = json.load(f)

f = open(working_directory + '\\schema\\put\\player_drill_result.json',)
player_drill_result_schema = json.load(f)

f = open(working_directory + '\\schema\\put\\player_group.json',)
player_group_schema = json.load(f)

f = open(working_directory + '\\schema\\put\\practice_drill.json',)
practice_drill_schema = json.load(f)

f = open(working_directory + "\\schema\\put\\practice.json")
practice_schema = json.load(f)

f = open(working_directory + r'\\schema\\put\\roster.json',)
roster_schema = json.load(f)

f = open(working_directory + '\\schema\\put\\season_league.json',)
season_league_schema = json.load(f)

f = open(working_directory + '\\schema\\put\\season_team.json',)
season_team_schema = json.load(f)

f = open(working_directory + '\\schema\\put\\season.json',)
season_schema = json.load(f)

f = open(working_directory + r'\\schema\\put\\team.json',)
team_schema = json.load(f)

f = open(working_directory + r'\\schema\\put\\user.json',)
user_schema = json.load(f)

f = open(working_directory + r'\\schema\\put\\ui_segment.json',)
ui_segment_schema = json.load(f)

put_rel_schema_arr = [
    configuration_schema,
    drill_rating_schema,
    drill_tag_schema,
    drill_schema,
    event_participants_drill_result_schema,
    event_schema,
    favorite_drill_schema,
    feedback_schema,
    goal_schema,
    league_schema,
    note_schema,
    player_drill_result_schema,
    player_group_schema,
    practice_drill_schema,
    practice_schema,
    roster_schema,
    season_league_schema,
    season_team_schema,
    season_schema,
    team_schema,
    ui_segment_schema,
    user_schema 
 ]
import json
import os

working_directory = os.getcwd()

f = open(working_directory + '\\schema\\post\\configuration.json',)
configuration_schema = json.load(f)

f = open(working_directory + '\\schema\\post\\drill_rating.json',)
drill_rating_schema = json.load(f)

f = open(working_directory + "\\schema\\post\\drill_tag.json",)
drill_tag_schema = json.load(f)

f = open(working_directory + '\\schema\\post\\drill.json',)
drill_schema = json.load(f)

f = open(working_directory + '\\schema\\post\\event_participants.json',)
event_participants_drill_result_schema = json.load(f)

f = open(working_directory + '\\schema\\post\\event.json',)
event_schema = json.load(f)

f = open(working_directory + r'\\schema\\post\\favorite_drill.json',)
favorite_drill_schema = json.load(f)

f = open(working_directory + r'\\schema\\post\\feedback.json',)
feedback_schema = json.load(f)

f = open(working_directory + '\\schema\\post\\goal.json',)
goal_schema = json.load(f)

f = open(working_directory + '\\schema\\post\\league.json',)
league_schema = json.load(f)

f = open(working_directory + r'\\schema\\post\\note.json',)
note_schema = json.load(f)

f = open(working_directory + '\\schema\\post\\player_drill_result.json',)
player_drill_result_schema = json.load(f)

f = open(working_directory + '\\schema\\post\\player_group.json',)
player_group_schema = json.load(f)

f = open(working_directory + '\\schema\\post\\practice_drill.json',)
practice_drill_schema = json.load(f)

f = open(working_directory + "\\schema\\post\\practice.json")
practice_schema = json.load(f)

f = open(working_directory + r'\\schema\\post\\roster.json',)
roster_schema = json.load(f)

f = open(working_directory + '\\schema\\post\\season_league.json',)
season_league_schema = json.load(f)

f = open(working_directory + '\\schema\\post\\season_team.json',)
season_team_schema = json.load(f)

f = open(working_directory + '\\schema\\post\\season.json',)
season_schema = json.load(f)

f = open(working_directory + r'\\schema\\post\\team.json',)
team_schema = json.load(f)

f = open(working_directory + r'\\schema\\post\\user.json',)
user_schema = json.load(f)

f = open(working_directory + r'\\schema\\post\\ui_segment.json',)
ui_segment_schema = json.load(f)

post_schema_arr = [ 
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
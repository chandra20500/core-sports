from schema.post.post_schema import post_schema_arr
from schema.put.put_schema import put_rel_schema_arr
import os

post_script = post_schema_arr
put_script = put_rel_schema_arr
put_obj_names = [
    "configuration",
    "drill_rating",
    "drill_tag",
    "drill",
    "event_participants",
    "event",
    "favorite_drill",
    "feedback",
    "goal",
    "league",
    "note",
    "player_drill_result",
    "player_group",
    "practice_drill",
    "practice",
    "roster",
    "season_league",
    "season_team",
    "season",
    "team",
    "ui_segment",
    "user"
]
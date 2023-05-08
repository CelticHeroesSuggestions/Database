# Yuletide 2013: Frost Items (Frostgloves, Frostboots, etc)

* What: Spawn points for the Yuletide 2013 gear quest
* Why: This gear was surprisingly good for its time, and would make a nice re-entrance.
* Notes: The gear quest NPCs are at Southern Road, inauthentically placed.
* Changes:
```
# Sergeant Cairn (Frost Items quest)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13521, 93, 1, -7.48, 0, 0.66, "stand", "807,1", 1, 45, 2, 0, 0, 0);

# the dialogue for this NPC was removed by OTM, so you will need to patch in Database/events/conversation/cv_winter2013_wyvern_defector_quest_giver.xml

# add the dialogue to conversation_lookup.txt, as an example I am using ID 1007

# update the NPC conversation
UPDATE ch_live_unitydatadb.mob_templates SET conversation_id = 1007 WHERE mob_template_id = 807;
```

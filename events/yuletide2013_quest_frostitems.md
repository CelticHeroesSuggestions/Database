# Yuletide 2013: Frost Items (Frostgloves, Frostboots, etc)

* What: Spawn points for the Yuletide 2013 gear quest
* Why: This gear was surprisingly good for its time, and would make a nice re-entrance.
* Notes: The gear quest NPCs are at Southern Road, inauthentically placed.
* Changes:
```
# Sergeant Cairn (Frost Gloves/Boots quest)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13521, 93, 1, -7.48, 0, 0.66, "stand", "807,1", 1, 45, 2, 0, 0, 0);

# the dialogue for this NPC was removed by OTM, so you will need to patch in Database/events/conversation/cv_winter2013_wyvern_defector_quest_giver.xml

# add the dialogue to conversation_lookup.txt, as an example I am using ID 1007

# update the NPC conversation
UPDATE ch_live_unitydatadb.mob_templates SET conversation_id = 1007 WHERE mob_template_id = 807;


# Ulfhidr the Artisan (Frost Helm quest)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13530, 93, 50, -5.88, 0, 1.37, "stand", "806,1", 1, 345, 50, 0, 0, 0);

# like Sergeant Carn, the dialogue for this NPC was removed by OTM, so you will need to patch in Database/events/conversation/cv_winter2013_wyvern_defector_quest_giver.xml

# add the dialogue to conversation_lookup.txt, as an example I am using ID 1007

# update the NPC conversation
UPDATE ch_live_unitydatadb.mob_templates SET conversation_id = 1004 WHERE mob_template_id = 806;
```

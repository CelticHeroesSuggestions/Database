# Yuletide 2013: Candycanes and Snowmen

* What: Spawn points for the Yuletide 2013 Candycane quest, which includes Gloomgaze, Snowmen, and Frost Spirits
* Why: The candycanes are fun, Gloomgaze dropped a cool consumable, and the snowmen dropped snowballs. It would be cool to introduce them again.
* Notes: I placed Gloomgaze near Highshore where he originally spawned. I placed three snowmen around Lirs Reach. I placed the Frost Spirits near Gloomgaze (inauthentic, but it's nice keeping the themes together).
* Changes:
```
# Iona (Candy Cane quest)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13520, 93, 1, -9.38, 0, -0.43, "stand", "808,1", 1, 45, 2, 0, 0, 0);

# Iona's dialogue is missing, so you will need to patch in Database/events/conversation/cv_winter2013_fun_weapon_quest_giver.xml

# add the dialogue to conversation_lookup.txt, I suggest ID 1005
conv 1005 cv_winter2013_fun_weapon_quest_giver

# update Iona's conversation
UPDATE ch_live_unitydatadb.mob_templates SET conversation_id = 1005 WHERE mob_template_id = 808;

# there were two versions of this quest, the first gave more powerful candycanes however was patched
# I suggest making a second NPC for the old version, and patching in Database/events/conversation/cv_winter2013_fun_weapon_quest_giver_op.xml 

# as before, add the dialogue to conversation_lookup.txt, I suggest ID 1006
conv 1006 cv_winter2013_fun_weapon_quest_giver_op

# Gloomgaze
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13501, 2, 600, -147.87, 0, -18.94, "random 15 0 0 1", "100139,1", 1, 0, 660, 0, 0, 0);

# Snowmen
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13502, 2, 15, -157.2, 0, 49.39, "stand", "100141,1", 1, 260, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13503, 2, 15, -232.05, 0, 3.94, "stand", "100141,1", 1, 260, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13504, 2, 15, 263.08, 0, -263.33, "stand", "100141,1", 1, 165, 30, 0, 0, 0);

# Frost Spirits
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13505, 2, 600, -147.87, 0, -18.94, "random 15 0 0 1", "70678,1", 1, 0, 660, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13506, 2, 600, -147.87, 0, -18.94, "random 15 0 0 1", "70678,1", 1, 0, 660, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13507, 2, 600, -147.87, 0, -18.94, "random 15 0 0 1", "70678,1", 1, 0, 660, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13508, 2, 600, -147.87, 0, -18.94, "random 15 0 0 1", "70678,1", 1, 0, 660, 0, 0, 0);
```
# Yuletide 2013: Frost Items (Frostgloves, Frostboots, etc)

* What: Spawn points for the Yuletide 2013 gear quest
* Why: This gear was surprisingly good for its time, and would make a nice re-entrance.
* Notes: The gear quest NPCs are at Southern Road, inauthentically placed.
* Changes:
```
# Sergeant Cairn (Frost Items quest)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13521, 93, 1, -7.48, 0, 0.66, "stand", "807,1", 1, 45, 2, 0, 0, 0);

# the dialogue for this NPC was removed by OTM, so you will need to patch in Database/events/conversation/cv_winter2013_bear_quest_giver.xml

# add the dialogue to conversation_lookup.txt, as an example I am using ID 1004

# update the NPC conversation
UPDATE ch_live_unitydatadb.mob_templates SET conversation_id = 1004 WHERE mob_template_id = 807;


```

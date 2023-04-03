# Huntsman Masks

* What: Spawn points for the Samhain 2013 2012 event hat quest NPCs and items.
* Why: This is a legacy event hat quest that is of high demand would make a nice re-entrance to the game.
* Table: `ch_live_unitydatadb.spawn_points`, `ch_live_unitydatadb.quest_templates`.
* Notes: I placed the quest NPC (The Huntsman) in Highshore (near the blacksmith), and placed the witches in front of him.
* Changes:
```
# The Huntsman
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13400, 2, 50, -130.76, 0, 45.60, "stand", "391,1", 1, 200, 50, 0, 0, 0);

# Move the quests to Lirs Reach
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 770;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 771;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 772;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 773;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 774;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 775;

# Fix the quest names (it seems that after the event they were changed to dev names); unfortunately this does not change the quest names on the client
UPDATE ch_live_unitydatadb.quest_templates SET quest_name = "Mask of the Huntsman" WHERE quest_id = 770;
UPDATE ch_live_unitydatadb.quest_templates SET quest_name = "Mask of the Stalker" WHERE quest_id = 771;
UPDATE ch_live_unitydatadb.quest_templates SET quest_name = "Mask of the Huntmaster" WHERE quest_id = 772;
UPDATE ch_live_unitydatadb.quest_templates SET quest_name = "Mask of the Huntsman" WHERE quest_id = 773;
UPDATE ch_live_unitydatadb.quest_templates SET quest_name = "Mask of the Stalker" WHERE quest_id = 774;
UPDATE ch_live_unitydatadb.quest_templates SET quest_name = "Mask of the Huntmaster" WHERE quest_id = 775;

# Fix the quest rewards (by default it doesn't give a reward for some reason)
UPDATE ch_live_unitydatadb.quest_rewards SET reward_type = 1 WHERE quest_id = 770;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1745 WHERE quest_id = 770;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_type = 1 WHERE quest_id = 771;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1746 WHERE quest_id = 771;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_type = 1 WHERE quest_id = 772;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1747 WHERE quest_id = 772;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_type = 1 WHERE quest_id = 773;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1745 WHERE quest_id = 773;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_type = 1 WHERE quest_id = 774;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1746 WHERE quest_id = 774;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_type = 1 WHERE quest_id = 775;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1747 WHERE quest_id = 775;

# Balance the quest rewards so higher spooky chance and equal chance at all colors
UPDATE ch_live_unitydatadb.loot_table_items SET weight = 1 WHERE loot_table_id = 1745;
UPDATE ch_live_unitydatadb.loot_table_items SET weight = 1 WHERE loot_table_id = 1746;
UPDATE ch_live_unitydatadb.loot_table_items SET weight = 1 WHERE loot_table_id = 1747;

# Add a few Samhain Witches for style
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13412, 2, 15, -137.74, 0, 46.60, "random 15 0 0 1", "100000,1", 1, 45, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13413, 2, 15, -139.11, 0, 52.06, "random 15 0 0 1", "100000,1", 1, 170, 30, 0, 0, 0);

# Add the Wandering Spirits
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13401, 2, 15, -137.74, 0, 46.60, "random 5 0 0 1", "100001,1", 1, 200, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13402, 2, 15, -139.11, 0, 52.06, "random 5 0 0 1", "100001,1", 1, 200, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13403, 2, 15, -134.78, 0, 51.07, "random 5 0 0 1", "100001,1", 1, 200, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13404, 2, 15, -131.99, 0, 56.03, "random 5 0 0 1", "100001,1", 1, 200, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13405, 2, 15, -130.81, 0, 58.48, "random 5 0 0 1", "100001,1", 1, 200, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13406, 2, 15, -133.69, 0, 54.86, "random 5 0 0 1", "100001,1", 1, 200, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13407, 2, 15, -137.76, 0, 57.32, "random 5 0 0 1", "100001,1", 1, 200, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13408, 2, 15, -136.36, 0, 62.34, "random 5 0 0 1", "100001,1", 1, 200, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13409, 2, 15, -144.45, 0, 64.52, "random 5 0 0 1", "100001,1", 1, 200, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13410, 2, 15, -137.74, 0, 46.60, "random 5 0 0 1", "100001,1", 1, 200, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13411, 2, 15, -149.08, 0, 59.32, "random 5 0 0 1", "100001,1", 1, 200, 30, 0, 0, 0);

```

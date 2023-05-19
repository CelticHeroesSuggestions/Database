# Yule 2019 Cooking: Candy Canes

* What: Spawn points for Yuletide 2019 cooking NPC and quest mobs.
* Why: Yuletide candy was fun but shortlived.
* Notes: The main NPC (Gel Fiorun) is located in the Tavern.
* Changes:
```
# Gel Fiorun
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (19500, 9, 50, 24.27, 0, 20.64, "stand", "142110,1", 1, 275, 50, 0, 0, 0);

# Greedy Goblin (in the Tavern Basement)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (19501, 9, 15, 25.44, -10, -16.84, "random 3 50 2 10", "142108,1", 1, 275, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (19502, 9, 15, 12.78, -10, -12.83, "random 3 50 2 10", "142108,1", 1, 275, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (19503, 9, 15, 20.23, -10, -16.78, "random 3 50 2 10", "142108,1", 1, 275, 30, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (19504, 9, 15, 17.89, -10, -20.03, "random 3 50 2 10", "142108,1", 1, 275, 30, 0, 0, 0);

# adjust the Greedy Goblin loot tables 110356 (3067), 110350 (3061), 110347 (3058)
DELETE ch_live_unitydatadb.loot_table_items WHERE loot_table_id = 3067 AND item_template_id = 0;  # candy canes
UPDATE ch_live_unitydatadb.loot_table_items SET weight = 20 WHERE loot_table_id = 3061 AND item_template_id = 0;  # rare presents
UPDATE ch_live_unitydatadb.loot_table_items SET amount = 7 WHERE loot_table_id = 3058;  # common presents
```

When a player has a candy cane, Gel Fiorun bypasses his intro text. Patch in `conversation/cv_Winter2019_recipe.xml` for an improved conversation.

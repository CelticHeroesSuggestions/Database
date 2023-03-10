# Coven Hats

* What: Spawn points for the Samhain 2012 event hat quest NPCs and items.
* Why: This is a legacy event hat quest that is of high demand would make a nice re-entrance to the game.
* Table: `ch_live_unitydatadb.spawn_points`, `ch_live_unitydatadb.item_spawns`.
* Notes: I placed the NPCs roughly where the instructions say they are (except Anika, who is in Lirs). I also limited the pumpkins to Crookback Hollow instead of Lirs Reach, as I think having the pumpkins together in a less-used area would be a nicer experience. Also, I labeled the spawn IDS in the `124XX` series: year 2012, and Samhain is event 4 in the usual series (Ostara, Birthday, Beltane, Samhain, Yuletide).
* Changes:
```
# Remove prerequisites as they are old and no longer available
DELETE FROM ch_live_unitydatadb.quest_prerequesits WHERE quest_id=367

# Anika the Witch
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12401, 2, 50, -187.06, 34, 64.23, "stand", "221,1", 1, 180, 50, 0, 0, 0);

# Whysten the Witch
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12402, 2, 50, -97.94, 34, -24.63, "stand", "222,1", 1, 200, 50, 0, 0, 0);

# Bryarnia the Witch
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12403, 2, 50, -25.34, 34, -100.17, "stand", "223,1", 1, 335, 50, 0, 0, 0);

# Starspin the Witch
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12404, 4, 50, 81.41, 34, -104.75, "stand", "224,1", 1, 75, 50, 0, 0, 0);

# Emberta the Witch
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12405, 9, 50, 11.3, 34, -7.53, "stand", "225,1", 1, 190, 50, 0, 0, 0);

# Betsy the Witch
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12406, 5, 50, 11.22, 34, -113.9, "stand", "226,1", 1, 260, 50, 0, 0, 0);

# Crypstig the Witch
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12407, 2, 50, 210.71, 34, -38.75, "stand", "227,1", 1, 170, 50, 0, 0, 0);

# Pumpkins
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12401, 4, 60, 95.01, -10, -78.49, "17534,100", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12402, 4, 60, 130.57, -10, -45.02, "17534,100", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12403, 4, 60, 101.5, -10, -33.32, "17534,100", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12404, 4, 60, 130.82, -10, -17.31, "17534,100", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12405, 4, 60, 75.17, -10, 2.79, "17534,100", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12406, 4, 60, 74.36, -10, 16.86, "22106,100", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12407, 4, 60, 62.31, -10, -22.37, "22106,100", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12408, 4, 60, 75.32, -10, -36.88, "22106,100", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12409, 4, 60, 61.39, -10, -38.45, "22106,100", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12410, 4, 60, 75, -10, -63.26, "22106,100", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12411, 4, 60, 63.61, -10, -73.49, "17534,100", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12412, 4, 60, 31.72, -10, -76.18, "17534,100", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12413, 4, 60, 22.85, -10, -61.8, "17534,100", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12414, 4, 60, -41.96, -10, -43.19, "17534,100", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12415, 4, 60, -41.84, -10, -26.27, "17534,100", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12416, 4, 60, -3.23, -10, -27.78, "17534,100", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12417, 4, 60, 10.31, -10, -40.55, "17534,100", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12418, 4, 60, 6.28, -10, -43.40, "17534,100", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12419, 4, 60, 18.13, 0, 115.68, "17534,100", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12420, 4, 60, 30.48, -10, 76.96, "17534,100", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12421, 4, 60, 19.25, -10, 57.31, "17534,100", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12422, 4, 60, 31.82, -10, 41.58, "17534,100", 90);
```

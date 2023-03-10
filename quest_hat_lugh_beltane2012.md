# Lugh Masks

* What: Spawn points for the Beltane (Midsummer) 2012 event hat quest NPCs and items.
* Why: This is a legacy event hat quest that is of high demand would make a nice re-entrance to the game.
* Table: `ch_live_unitydatadb.spawn_points`, `ch_live_unitydatadb.item_spawns`, `ch_live_unitydatadb.quest_templates`.
* Notes: I placed the NPC (Bragen the Druid) at the Western Road leystone, and scattered the Sunstones around that region of Lirs Reach. I used the ID convention 123XX for spawn points to avoid conflicts.
* Changes:

```
# Remove prerequisites as they are old and no longer available
#DELETE FROM ch_live_unitydatadb.quest_prerequesits WHERE quest_id=367

# Bragen the Druid
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12301, 2, 50, -230.99, 15, -145.41, "stand", "207,1", 1, 230, 50, 0, 0, 0);

# Sunstone Spawns
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12300, 2, 60, -236.43, 20, -152.69, "20968,1", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12301, 2, 60, -244.7, 20, -143.08, "20968,1", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12302, 2, 60, -244.61, 20, -148.60, "20968,1", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12303, 2, 60, -251.03, 20, -150, "20968,1", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12304, 2, 60, -258.63, 20, -144.1, "20968,1", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12305, 2, 60, -252.22, 20, -147.62, "20968,1", 90);

INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12306, 2, 60, -228.93, 20, -153.59, "20969,1", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12307, 2, 60, -224.95, 20, -145.55, "20969,1", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12308, 2, 60, -217.9, 20, -144.19, "20969,1", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12309, 2, 60, -202.13, 20, -156.72, "20969,1", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12310, 2, 60, -192.75, 20, -140.36, "20969,1", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12311, 2, 60, -176.78, 20, -128.91, "20969,1", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12312, 2, 60, -153.56, 20, -193.94, "20969,1", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12313, 2, 60, -165.70, 20, -158.62, "20969,1", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12314, 2, 60, -158.58, 20, -173.39, "20969,1", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12315, 2, 60, -175.22, 20, -195.94, "20969,1", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12316, 2, 60, -173.04, 20, -202.72, "20969,1", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12317, 2, 60, -180.98, 20, -212.3, "20969,1", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12318, 2, 60, -201.09, 20, -199.13, "20969,1", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12319, 2, 60, -217.73, 20, -216.36, "20969,1", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12320, 2, 60, -254.59, 20, -175.46, "20969,1", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12321, 2, 60, -257.76, 20, -187.5, "20969,1", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12322, 2, 60, -262.9, 20, -202.63, "20969,1", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12323, 2, 60, -264.08, 20, -196.29, "20969,1", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12324, 2, 60, -247.84, 20, -205.1, "20969,1", 90);
INSERT INTO ch_live_unitydatadb.item_spawns (item_spawn_id, zone_id, respawn_time, position_x, position_y, position_z, item_list, max_respawn_time)
VALUES (12325, 2, 60, -247.56, 20, -221.01, "20969,1", 90);
```

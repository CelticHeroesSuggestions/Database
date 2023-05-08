# Sunflower Wand

* What: Spawn points for the Beltane (Midsummer) 2012 event wand quest NPCs and items.
* Why: Sunflower wands are cute and would be a welcome return to the game.
* Notes: I placed the NPC (Elsya the Shaper) at the Temple of Belenus leystone, and placed the Stinkroot Faeries approximately where the quest instructions state they are.
* Changes:

```
# Elsya the Shaper
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12330, 2, 50, -25.52, 0, -135.55, "stand", "208,1", 1, 160, 50, 0, 0, 0);

# move the quest to Lirs Reach
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 348;

# Stinkroot Faeries
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12331, 2, 30, -9.26, 0, -62.09, "random 5 0 0 1", "71368,1", 1, 180, 60, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12332, 22, 30, -303.62, 0, 331.04, "random 5 0 0 1", "71369,1", 1, 180, 60, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12333, 2, 30, -254.54, 0, -195.87, "random 5 0 0 1", "71370,1", 1, 180, 60, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12334, 2, 30, -58.33, 0, -202.37, "random 5 0 0 1", "71371,1", 1, 180, 60, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12335, 2, 30, 189.28, 0, -10.54, "random 5 0 0 1", "71372,1", 1, 180, 60, 0, 0, 0);
```

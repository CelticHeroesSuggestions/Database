# Yuletide 2014: Event Wand Quest (winterstave)

* What: Spawn point for the Yuletide 2014 event quest.
* Why: This quest was very popular and would be a nice revival for the game.
* Table: `ch_live_unitydatadb.spawn_points`, `ch_live_unitydatadb.shop_stock`.
* Notes: I placed the NPC at Farcrag's parapets, to give more content there.
* Changes:
```
# Serena of the Ice

# Insert the spawn point
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (14504, 93, 50, 25.18, 0, -85.88, "stand", "101133,1", 1, 40, 12, 0, 0, 0);

# move the quests to Farcrag
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1673;
```

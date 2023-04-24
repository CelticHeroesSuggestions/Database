# Yuletide 2015: Event Quests

* What: Spawn point for the Yuletide 2015 event quests.
* Why: These quests were very popular and would be a nice revival for the game.
* Notes: I placed the NPCs at Farcrag Castle's fountain.
* Changes:
```
# Tira Snowfeld (kite quest)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15502, 93, 50, 0.47, 0, -36.54, "stand", "140025,1", 1, 225, 12, 0, 0, 0);

# move her quests to Farcrag
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 2342;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 2343;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 2344;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 2345;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 2346;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 2347;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 2348;


# Jalen Gaylewynd (eagle crest quest)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (15503, 93, 50, -2.38, 0, -36.65, "stand", "101130,1", 1, 135, 12, 0, 0, 0);

# move his quests to Farcrag
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1669;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1668;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1667;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1666;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1665;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1664;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1663;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1662;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1661;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1660;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1659;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1658;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1657;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1656;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1655;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1654;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1653;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1652;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1651;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1650;

# TODO: need a way to obtain Cranfir Crackers (57378), originally from SlateGrit mobs (138921-138931, 140021-140023, 140038, 140040)
```

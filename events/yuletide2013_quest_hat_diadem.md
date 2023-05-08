# Diadems of Ice

* What: Spawn points for the Yuletide 2013 event hat quest NPCs and items.
* Why: Diadems were a challenging quest to complete and would be a nice readdition.
* Notes: I placed the quest NPC near the Farcrag Fountain.
* Changes:

```
# INCOMPLETE Not sure what NPC to use
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13530, 93, 50, -5.88, 0, 1.37, "stand", ",1", 1, 345, 50, 0, 0, 0);

# as with other Yuletide 2013 NPCs, the conversation was deleted. Patch in Database/events/conversation/

# update conversation_lookup.txt, I used 1008

# move the quests to Farcrag Castle (they should already be there by default)
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1307;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1308;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1309;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1310;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1307;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1311;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1312;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1313;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1314;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1315;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1316;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1317;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1318;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1319;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1320;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1321;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1322;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1323;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1324;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1325;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 1326;

# the dialogue for this quest was removed by OTM, so it would need reconstruction. I could not find a Youtube video on this quest.
```

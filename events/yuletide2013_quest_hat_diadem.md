# Diadems of Ice

* What: Spawn points for the Yuletide 2013 event hat quest NPCs and items.
* Why: Diadems were a challenging quest to complete and would be a nice readdition.
* Notes: I placed the quest NPC near the Farcrag Fountain.
* Changes:

```
# spawn in the Yulefather, used in the Yuletide 2012 event.
# as with other Yuletide 2013 NPCs, the conversation was deleted. Patch in Database/events/conversation/cv_yulefather.xml

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

# fix the quest rewards, by default they give battleskewers (Samhain 2013) instead of Diadems
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1796 WHERE quest_id = 1307;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1797 WHERE quest_id = 1308;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1798 WHERE quest_id = 1309;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1799 WHERE quest_id = 1310;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1800 WHERE quest_id = 1311;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1801 WHERE quest_id = 1312;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1802 WHERE quest_id = 1313;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1803 WHERE quest_id = 1314;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1804 WHERE quest_id = 1315;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1085 WHERE quest_id = 1316;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1796 WHERE quest_id = 1317;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1797 WHERE quest_id = 1318;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1798 WHERE quest_id = 1319;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1799 WHERE quest_id = 1320;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1800 WHERE quest_id = 1321;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1801 WHERE quest_id = 1322;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1802 WHERE quest_id = 1323;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1803 WHERE quest_id = 1324;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1804 WHERE quest_id = 1325;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 1805 WHERE quest_id = 1326;

# change which items the quest uses
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '53341,5' WHERE quest_id = 1307 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '53341,5' WHERE quest_id = 1307 AND stage_id = 1;

UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,10' WHERE quest_id = 1308 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,10' WHERE quest_id = 1308 AND stage_id = 1;

UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,20' WHERE quest_id = 1309 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,20' WHERE quest_id = 1309 AND stage_id = 1;

UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,30' WHERE quest_id = 1310 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,30' WHERE quest_id = 1310 AND stage_id = 1;

UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,40' WHERE quest_id = 1311 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,40' WHERE quest_id = 1311 AND stage_id = 1;

UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,50' WHERE quest_id = 1312 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,50' WHERE quest_id = 1312 AND stage_id = 1;

UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,60' WHERE quest_id = 1313 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,60' WHERE quest_id = 1313 AND stage_id = 1;

UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,70' WHERE quest_id = 1314 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,70' WHERE quest_id = 1314 AND stage_id = 1;

UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,100' WHERE quest_id = 1315 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,100' WHERE quest_id = 1315 AND stage_id = 1;

UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,150' WHERE quest_id = 1316 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,150' WHERE quest_id = 1316 AND stage_id = 1;

UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '53341,5' WHERE quest_id = 1317 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '53341,5' WHERE quest_id = 1317 AND stage_id = 1;

UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,10' WHERE quest_id = 1318 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,10' WHERE quest_id = 1318 AND stage_id = 1;

UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,20' WHERE quest_id = 1319 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,20' WHERE quest_id = 1319 AND stage_id = 1;

UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,30' WHERE quest_id = 1320 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,30' WHERE quest_id = 1320 AND stage_id = 1;

UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,40' WHERE quest_id = 1321 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,40' WHERE quest_id = 1321 AND stage_id = 1;

UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,50' WHERE quest_id = 1322 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,50' WHERE quest_id = 1322 AND stage_id = 1;

UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,60' WHERE quest_id = 1323 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,60' WHERE quest_id = 1323 AND stage_id = 1;

UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,70' WHERE quest_id = 1324 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,70' WHERE quest_id = 1324 AND stage_id = 1;

UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,100' WHERE quest_id = 1325 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,100' WHERE quest_id = 1325 AND stage_id = 1;

UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,150' WHERE quest_id = 1326 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '22588,150' WHERE quest_id = 1326 AND stage_id = 1;
```

Also update the `text.db` file by patching the following:
```
# change which items the quest uses
UPDATE quest_stage_templates SET stage_desc = 'Gather 5 Red Yuletide Presents. You can find them in Farcrag Castle.' WHERE quest_id = 1307 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '53341,5' WHERE quest_id = 1307 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '53341,5' WHERE quest_id = 1307 AND stage_id = 1;

UPDATE quest_stage_templates SET stage_desc = 'Gather 10 Green Yuletide Presents. You can find them in Farcrag Castle.' WHERE quest_id = 1308 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,10' WHERE quest_id = 1308 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,10' WHERE quest_id = 1308 AND stage_id = 1;

UPDATE quest_stage_templates SET stage_desc = 'Gather 20 Green Yuletide Presents. You can find them in Farcrag Castle.' WHERE quest_id = 1309 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,20' WHERE quest_id = 1309 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,20' WHERE quest_id = 1309 AND stage_id = 1;

UPDATE quest_stage_templates SET stage_desc = 'Gather 30 Green Yuletide Presents. You can find them in Farcrag Castle.' WHERE quest_id = 1310 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,30' WHERE quest_id = 1310 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,30' WHERE quest_id = 1310 AND stage_id = 1;

UPDATE quest_stage_templates SET stage_desc = 'Gather 40 Green Yuletide Presents. You can find them in Farcrag Castle.' WHERE quest_id = 1311 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,40' WHERE quest_id = 1311 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,40' WHERE quest_id = 1311 AND stage_id = 1;

UPDATE quest_stage_templates SET stage_desc = 'Gather 50 Green Yuletide Presents. You can find them in Farcrag Castle.' WHERE quest_id = 1312 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,50' WHERE quest_id = 1312 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,50' WHERE quest_id = 1312 AND stage_id = 1;

UPDATE quest_stage_templates SET stage_desc = 'Gather 60 Green Yuletide Presents. You can find them in Farcrag Castle.' WHERE quest_id = 1313 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,60' WHERE quest_id = 1313 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,60' WHERE quest_id = 1313 AND stage_id = 1;

UPDATE quest_stage_templates SET stage_desc = 'Gather 70 Green Yuletide Presents. You can find them in Farcrag Castle.' WHERE quest_id = 1314 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,70' WHERE quest_id = 1314 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,70' WHERE quest_id = 1314 AND stage_id = 1;

UPDATE quest_stage_templates SET stage_desc = 'Gather 100 Green Yuletide Presents. You can find them in Farcrag Castle.' WHERE quest_id = 1315 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,100' WHERE quest_id = 1315 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,100' WHERE quest_id = 1315 AND stage_id = 1;

UPDATE quest_stage_templates SET stage_desc = 'Gather 150 Green Yuletide Presents. You can find them in Farcrag Castle.' WHERE quest_id = 1316 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,150' WHERE quest_id = 1316 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,150' WHERE quest_id = 1316 AND stage_id = 1;

UPDATE quest_stage_templates SET stage_desc = 'Gather 5 Red Yuletide Presents. You can find them in Farcrag Castle.' WHERE quest_id = 1317 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '53341,5' WHERE quest_id = 1317 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '53341,5' WHERE quest_id = 1317 AND stage_id = 1;

UPDATE quest_stage_templates SET stage_desc = 'Gather 10 Green Yuletide Presents. You can find them in Farcrag Castle.' WHERE quest_id = 1318 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,10' WHERE quest_id = 1318 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,10' WHERE quest_id = 1318 AND stage_id = 1;

UPDATE quest_stage_templates SET stage_desc = 'Gather 20 Green Yuletide Presents. You can find them in Farcrag Castle.' WHERE quest_id = 1319 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,20' WHERE quest_id = 1319 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,20' WHERE quest_id = 1319 AND stage_id = 1;

UPDATE quest_stage_templates SET stage_desc = 'Gather 30 Green Yuletide Presents. You can find them in Farcrag Castle.' WHERE quest_id = 1320 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,30' WHERE quest_id = 1320 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,30' WHERE quest_id = 1320 AND stage_id = 1;

UPDATE quest_stage_templates SET stage_desc = 'Gather 40 Green Yuletide Presents. You can find them in Farcrag Castle.' WHERE quest_id = 1321 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,40' WHERE quest_id = 1321 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,40' WHERE quest_id = 1321 AND stage_id = 1;

UPDATE quest_stage_templates SET stage_desc = 'Gather 50 Green Yuletide Presents. You can find them in Farcrag Castle.' WHERE quest_id = 1322 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,50' WHERE quest_id = 1322 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,50' WHERE quest_id = 1322 AND stage_id = 1;

UPDATE quest_stage_templates SET stage_desc = 'Gather 60 Green Yuletide Presents. You can find them in Farcrag Castle.' WHERE quest_id = 1323 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,60' WHERE quest_id = 1323 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,60' WHERE quest_id = 1323 AND stage_id = 1;

UPDATE quest_stage_templates SET stage_desc = 'Gather 70 Green Yuletide Presents. You can find them in Farcrag Castle.' WHERE quest_id = 1324 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,70' WHERE quest_id = 1324 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,70' WHERE quest_id = 1324 AND stage_id = 1;

UPDATE quest_stage_templates SET stage_desc = 'Gather 100 Green Yuletide Presents. You can find them in Farcrag Castle.' WHERE quest_id = 1325 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,100' WHERE quest_id = 1325 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,100' WHERE quest_id = 1325 AND stage_id = 1;

UPDATE quest_stage_templates SET stage_desc = 'Gather 150 Green Yuletide Presents. You can find them in Farcrag Castle.' WHERE quest_id = 1326 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,150' WHERE quest_id = 1326 AND stage_id = 0;
UPDATE quest_stage_templates SET completion_details = '22588,150' WHERE quest_id = 1326 AND stage_id = 1;
```

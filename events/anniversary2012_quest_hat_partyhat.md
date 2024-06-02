# Party Hats

* What: Spawn points for the Anniversary 2012 event hat quest NPCs and items.
* Why: This is a legacy event hat quest that is of high demand would make a nice re-entrance to the game.
* Table: `ch_live_unitydatadb.spawn_points`, `ch_live_unitydatadb.item_spawns`.
* Notes: I placed Hamish the Hatter by the tavern. Since lots of hat quests use presents, this quest is set to (inauthentically) use the Anniversary 2013 presents. ALSO, due to Hamish the Hatter being recycled for the 2013 anniversary hat quest (party crowns), this quest is not available unless the hatman's XML file is modified.
* Changes:
```
# Hamish the Hatter
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (12202, 2, 50, 254.30, 0, -250.58, "stand", "379,1", 1, 300, 50, 0, 0, 0);

# Move the quests to Lirs Reach
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 328;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 330;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 331;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 332;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 333;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 334;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 335;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 2 WHERE quest_id = 336;

# Change the quests to use 2013 presents
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35274,5' WHERE quest_id = 328 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35274,5' WHERE quest_id = 328 AND stage_id = 1;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,10' WHERE quest_id = 330 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,10' WHERE quest_id = 330 AND stage_id = 1;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,20' WHERE quest_id = 331 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,20' WHERE quest_id = 331 AND stage_id = 1;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,50' WHERE quest_id = 332 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,50' WHERE quest_id = 332 AND stage_id = 1;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,100' WHERE quest_id = 333 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,100' WHERE quest_id = 333 AND stage_id = 1;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,150' WHERE quest_id = 334 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,150' WHERE quest_id = 334 AND stage_id = 1;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,250' WHERE quest_id = 335 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,250' WHERE quest_id = 335 AND stage_id = 1;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,500' WHERE quest_id = 336 AND stage_id = 0;
UPDATE ch_live_unitydatadb.quest_stage_templates SET completion_details = '35275,500' WHERE quest_id = 336 AND stage_id = 1;

# Red Present Spawns (Farcrag): see the `anniversary2013_hat_quest_partycrowns.md` file for spawning these items

# Green Present Spawns (Lirs): see the `anniversary2013_hat_quest_partycrowns.md` file for spawning these items
```

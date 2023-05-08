# Yuletide 2011: Yulestave and Snowman Hat Quests

* What: Spawn points for the Yuletide 2011 event wand quest NPC.
* Why: This is a legacy event wand quest that is of high demand would make a nice re-entrance to the game.
* Table: `ch_live_unitydatadb.spawn_points``.
* Notes: I placed the NPCs in Farcrag.
* Changes:
```
# Albin Fireheart
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (11501, 93, 10, 5.87, 0, -15.66, "stand", "143,1", 1, 90, 50, 0, 0, 0);

# Snowdrop the Faerie
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (11502, 93, 10, 4.6, 0, -14.19, "stand", "142,1", 1, 165, 50, 0, 0, 0);

# Move the quests to Farcrag Castle
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 118;
UPDATE ch_live_unitydatadb.quest_templates SET zone = 93 WHERE quest_id = 119;

# Correct the quest rewards
UPDATE ch_live_unitydatadb.quest_templates SET item_reward = '17607,0' WHERE quest_id = 118;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 17607 WHERE quest_id = 118;
UPDATE ch_live_unitydatadb.quest_templates SET item_reward = '17603,0' WHERE quest_id = 119;
UPDATE ch_live_unitydatadb.quest_rewards SET reward_id = 17603 WHERE quest_id = 119;

# Spawn Frost Spirits (wand quest)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (11510, 2, 10, -235.41, 0, 49.68, "random 20 0 0 1", "70678,1", 1, 165, 20, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (11511, 2, 10, -235.41, 0, 40.68, "random 20 0 0 1", "70678,1", 1, 165, 20, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (11512, 2, 10, -229.41, 0, 44.68, "random 20 0 0 1", "70678,1", 1, 165, 20, 0, 0, 0);

# Spawn Snowstorm Golems (wand quest)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (11513, 2, 10, -244.79, 0, 42.61, "stand", "70682,1", 1, 100, 20, 0, 0, 0);

# Spawn Queen Midwinter (hat quest)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (11514, 2, 10, -245.93, 0, 12.85, "stand", "70684,1", 1, 135, 20, 0, 0, 0);

# Spawn Midwinter Faeries (hat quest)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (11515, 2, 10, -242.93, 0, 16.85, "random 10 0 0 1", "70677,1", 1, 135, 20, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (11516, 2, 10, -240.93, 0, 18.85, "random 10 0 0 1", "70677,1", 1, 135, 20, 0, 0, 0);
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (11517, 2, 10, -244.93, 0, 16.85, "random 10 0 0 1", "70677,1", 1, 135, 20, 0, 0, 0);

# update the model scale of the golems
UPDATE ch_live_unitydatadb.mob_templates SET model_scale = 0.01 WHERE mob_template_id = 70682;
```

Edit `mob_data.txt`: change the Snowstorm Golems from tiny snowmen to actual blue golems
```
...
70682,50322,3,[*****] Snowstorm Golem,1800,3,12,5,0,12,0.5,.1,0,0,1
...
```

Execute SQL queries to `text_patched.db`
```
UPDATE quest_stage_templates SET stage_desc = "Search for the Frost Spirits, who can be found in the east of Lir's Reach, and recover ten Frost Spirit Gems from them." WHERE quest_id = 119 AND stage_id = 0;
UPDATE quest_stage_templates SET stage_desc = "Return the Frost Spirit Gems to Albin Fireheart." WHERE quest_id = 119 AND stage_id = 1;
```

Replace Albin Coldheart's dialogue (`cv_albin_coldheart.xml`)
```
<!-- Albin Coldheart -->

<xml>

<start>
<startCondition>QUEST_COMPLETE 119</startCondition>
<startGoto>POSTCOMP</startGoto>
</start>

<start>
<startCondition>STAGE_AVAILABLE 119 3</startCondition>
<startGoto>GOT_STUFF_SNOW</startGoto>
</start>

<start>
<startCondition>STAGE_AVAILABLE 119 2</startCondition>
<startGoto>CURRENT_SNOW</startGoto>
</start>

<start>
<startCondition>STAGE_AVAILABLE 119 1</startCondition>
<startCondition>HAVE_ITEM 17601 5</startCondition>
<startGoto>GOT_STUFF_GOBLINS</startGoto>
</start>

<start>
<startCondition>STAGE_AVAILABLE 119 0</startCondition>
<startGoto>CURRENT_GOBLINS</startGoto>
</start>

<start>
<startCondition>QUEST_AVAILABLE 119</startCondition>
<startGoto>OPEN_QUEST</startGoto>
</start>

<line>
<lineTag>OPEN_QUEST</lineTag>
<lineText>I am Albin Fireheart, an emissary of the Winter goddess Brigid, who makes sure that Spring always follows Winter. Every year Brigid and her followers must do battle with the minions of Callech, the cold winter goddess who is set upon casting the lands into eternal Winter. I am here to ensure that Callech is not victorious, and I am looking for allies in my struggle.</lineText>
<choice>
<choiceOptions>[Q]</choiceOptions>
<choiceText>The Defence of Winter.</choiceText>
<choiceAction> </choiceAction>
<choiceGoto>QUEST</choiceGoto>
</choice>
<choice>
<choiceOptions>[X]</choiceOptions>
<choiceText>Goodbye.</choiceText>
<choiceAction> </choiceAction>
<choiceGoto>-1</choiceGoto>
</choice>
</line>

<line>
<lineTag>QUEST</lineTag>
<lineText>Callech has sent her minions, the Frost Spirits, to Lir's Reach with 'Frost Spirit Gems' that are infused with a portion of her power. I fear they intend to use the Snowflake Gems for some grand and evil sorcery. I need you to recover ten of these gems and bring them back to me, so we can stop Callech before it is too late!</lineText>
<choice>
<choiceOptions>[Y]</choiceOptions>
<choiceText>I'll get the gems.</choiceText>
<choiceAction>QUEST_ADD 119</choiceAction>
<choiceGoto>-1</choiceGoto>
</choice>
<choice>
<choiceOptions>[N]</choiceOptions>
<choiceText>I can't help right now.</choiceText>
<choiceAction> </choiceAction>
<choiceGoto>-1</choiceGoto>
</choice>
</line>

<line>
<lineTag>GOT_STUFF_GOBLINS</lineTag>
<lineText>You're back, [name]. Have you recovered the Frost Spirit Gems?</lineText>
<choice>
<choiceOptions>[C]</choiceOptions>
<choiceText>Yes, I have.</choiceText>
<choiceAction>STAGE_COMPLETE 119 1</choiceAction>
<choiceGoto>GOT_STUFF_2_GOBLINS</choiceGoto>
</choice>
</line>

<line>
<lineTag>GOT_STUFF_2_GOBLINS</lineTag>
<lineText>This is good, but alas, my friend, I fear it is already too late! The Frost Spirits have summoned a host of Snowstorm Golems! These monstrous creatures can create a blizzard of such titanic proportions that will cause all of Lir's Reach to freeze over - we must destroy at least two of the beasts before they turn the whole region to ice!</lineText>
<choice>
<choiceOptions>[Y]</choiceOptions>
<choiceText>I'll defeat the Snowmen.</choiceText>
<choiceAction> </choiceAction>
<choiceGoto>-1</choiceGoto>
</choice>
</line>

<line>
<lineTag>GOT_STUFF_SNOW</lineTag>
<lineText>Do you bring good news, [name]? Have you defeated the Snowstorm Golems?</lineText>
<choice>
<choiceOptions>[C]</choiceOptions>
<choiceText>Yes, I have.</choiceText>
<choiceAction>STAGE_COMPLETE 119 3</choiceAction>
<choiceGoto>GOT_STUFF_2_SNOW</choiceGoto>
</choice>
</line>

<line>
<lineTag>GOT_STUFF_2_SNOW</lineTag>
<lineText>I am glad. With the Frost Spirit Gems in our grasp and the Snowstorm Golems defeated, the minions of Callech will not be able to freeze Lir's Reach, and Spring will come again once Winter is over. We have much to thank you for, [name]. Here, take this Yulestave - it is a weapon wielded by all of Brigid's most trusted allies, and fires magical snowballs at your foes. Please accept it as a gift from Brigid, and a memento of your heroic actions in her name.</lineText>
<choice>
<choiceOptions>[X]</choiceOptions>
<choiceText>Thank you. Farewell.</choiceText>
<choiceAction> </choiceAction>
<choiceGoto>-1</choiceGoto>
</choice>
</line>

<line>
<lineTag>CURRENT_GOBLINS</lineTag>
<lineText>I need you to recover ten Frost Spirit Gems, [name]. You can find them on Frost Spirits, which can be found all over Lir's Reach.</lineText>
<choice>
<choiceOptions>[X]</choiceOptions>
<choiceText>Goodbye.</choiceText>
<choiceAction> </choiceAction>
<choiceGoto>-1</choiceGoto>
</choice>
</line>

<line>
<lineTag>CURRENT_SNOW</lineTag>
<lineText>You need to defeat two Snowstorm Golems, [name], before they freeze the land itself and turn Lir's Reach into a block of ice!</lineText>
<choice>
<choiceOptions>[X]</choiceOptions>
<choiceText>Goodbye.</choiceText>
<choiceAction> </choiceAction>
<choiceGoto>-1</choiceGoto>
</choice>
</line>

<line>
<lineTag>POSTCOMP</lineTag>
<lineText>You have the thanks of Brigid and all her followers, [name]. I hope the turning wheels of the seasons will cause our paths to cross again.</lineText>
<choice>
<choiceOptions>[X]</choiceOptions>
<choiceText>Farewell.</choiceText>
<choiceAction> </choiceAction>
<choiceGoto>-1</choiceGoto>
</choice>
</line>
</xml>
```

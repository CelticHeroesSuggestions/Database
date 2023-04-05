# Difinitus: Shadowed Doch Gul Armor

* What: An NPC to award Shadowed Doch Gul armor, which has textures in the game files but is not currently an item. From what I understand about how CH works, I have tried to make it easy for DECA Games to add this NPC to the game.
* Why: It would be nice to have an additional armor set in the game.
* Table: various.
* Notes: I named the NPC Difinitus just out of convenience, but any Celtic name would fit. I placed the NPC in Lir's Reach, by the Tavern.
* Changes:

Add a new Dialogue (patchserver): `cv_leif_difinitus.xml`
```
<xml>
<line>
<lineTag>OPEN</lineTag>
<lineText>The wardens told me I would find you here, [class].  I am Difinitus.  Many years ago I was a servant of Crom Cruach, however the wardens showed me the corruption in Crom's ways.\n\nWhen I fled Crom's unholy prison, I weakened him by taking his treasured armor chest. The armor within is the only set capable of defeating him.\n\nIf you prove yourself, I will gift you a piece.
</lineText>

<choice>
<choiceCondition>CLASS DRUID</choiceCondition>
<choiceCondition>QUEST_AVAILABLE 369</choiceCondition>
<choiceOptions>[Q]</choiceOptions>
<choiceText>Shadowed Doch Gul</choiceText>
<choiceAction></choiceAction>
<choiceGoto>QUEST_PIECE</choiceGoto>
</choice>

<choice>
<choiceCondition>CLASS DRUID</choiceCondition>
<choiceCondition>QUEST_CURRENT 369</choiceCondition>
<choiceOptions></choiceOptions>
<choiceText>Lanterns?</choiceText>
<choiceAction></choiceAction>
<choiceGoto>QUEST_HOWTO</choiceGoto>
</choice>

<choice>
<choiceCondition>CLASS DRUID</choiceCondition>
<choiceCondition>STAGE_AVAILABLE 369 1</choiceCondition>
<choiceOptions>[C]</choiceOptions>
<choiceText>Shadowed Doch Gul</choiceText>
<choiceAction>STAGE_COMPLETE 369 1</choiceAction>
<choiceGoto>GOT_PIECE</choiceGoto>
</choice>

<choice>
<choiceOptions>[X]</choiceOptions>
<choiceText>Goodbye.</choiceText>
<choiceAction> </choiceAction>
<choiceGoto>-1</choiceGoto>
</choice>
</line>

<line>
<lineTag>QUEST_HOWTO</lineTag>
<lineText>The lanterns are held by Crom Cruach's sentinels. Find and defeat them to pry the lanterns from their grasp.</lineText>
<choice>
<choiceOptions>[X]</choiceOptions>
<choiceText>Will do.</choiceText>
<choiceAction></choiceAction>
<choiceGoto>-1</choiceGoto>
</choice>
</line>

<line>
<lineTag>QUEST_PIECE</lineTag>
<lineText>Only the most powerful [class]s can withstand the power coursing through Shadowed Doch Gul. If you bring me 3 Soulbourne Lanterns I will reward you with a piece.</lineText>
<choice>
<choiceCondition>QUEST_AVAILABLE 369</choiceCondition>
<choiceOptions>[Y]</choiceOptions>
<choiceText>I'll get the items.</choiceText>
<choiceAction>QUEST_ADD 369</choiceAction>
<choiceGoto>-1</choiceGoto>
</choice>
<choice>
<choiceOptions>[X]</choiceOptions>
<choiceText>Goodbye.</choiceText>
<choiceAction> </choiceAction>
<choiceGoto>-1</choiceGoto>
</choice>
</line>

<line>
<lineTag>GOT_PIECE</lineTag>
<lineText>How fared your journey, [name]? Do you have the lanterns?\n\nAh, I can feel the tormented souls begging for release. Give me the lanterns, I will ensure their souls can pass to the next world, free from Crom's grasp. Here is a piece of Shadowed Doch Gul armor, may you use it to slay the god once and for all.</lineText>
<choice>
<choiceOptions>[X]</choiceOptions>
<choiceText>Thank you.</choiceText>
<choiceAction></choiceAction>
<choiceGoto>-1</choiceGoto>
</choice>
</line>
</xml>
```

Add a new Model (patchserver): `modelids_list.txt`: this creates a new asset model using the DG armor as a base and Dark DG textures
```
# Druid Robe
2,100001,2,0,0,1,0,0
1519,3767,1,0,2,0,1,699,3766,2,111,0.5
1542,3781,2,0,2,0,1,699,3780,2,111,0.5
# Druid Legs
3,100003,2,0,0,1,0,0
1517,3758,1,0,2,0,1,699,3757,2,111,0.5
1539,3758,2,0,2,0,1,699,3757,2,111,0.5
# Druid Helm
1,100004,2,0,0,1,0,0
1520,3758,1,0,2,0,1,699,3757,2,111,0.5
1541,3769,2,0,2,0,1,699,3768,2,111,0.5
# Druid Boots
4,100005,2,0,0,1,0,0
1518,3752,1,0,2,0,1,699,3751,2,111,0.5
1540,3752,2,0,2,0,1,699,3751,2,111,0.5
# Druid Gloves
6,100006,2,0,0,1,0,0
1516,3754,1,0,2,0,1,699,3753,2,111,0.5
1538,3754,2,0,2,0,1,699,3753,2,111,0.5
```

Add a new Item (patchserver): `item_list.txt`
Note: `ID|?|armor|slot:2=robe|weight|atkspeed|itemsubtype|3dmodelid|iconid|?|?|?||3^heat;4^cold;5^magic||classreq:2=druid|skillid|skilllvl|attackrange|missilespeed|reportbacktimemale|reportbacktimefemale|blocksslots|procskillid|procskilllvl|procskillchance|equipskillid|equipskilllevel|uniqueid:0|boe:1=yes||1^dex;2^foc;3^vit|10^natmagic||skill_bonus?|max_charges?|destroy_on_no_charges?|?|?|?|1^spellevade;3^woundevade||`
```
...
# Druid items
100001|0|40|2|15|0|4|100001|9417|7909|1|76||3^300;4^300;5^300||2|0|0|0|-1|0|0|0|0|0|0|0|0|0|0||1^300;2^1000;3^300|10^5000||9999|0|-1|0|0|1|1^3000;3^3000||
100002|0|40|2|15|0|4|100001|9412|7909|1|76||3^300;4^300;5^300||2|0|0|0|-1|0|0|0|0|0|0|0|0|0|0||1^300;2^1000;3^300|10^5000||9999|0|-1|0|0|1|1^3000;3^3000||
100003|0|40|3|15|0|4|100003|9416|7909|1|76||3^300;4^300;5^300||2|0|0|0|-1|0|0|0|0|0|0|0|0|0|0||1^300;2^1000;3^300|10^5000||9999|0|-1|0|0|1|1^3000;3^3000||
100004|0|40|1|15|0|4|100004|9415|7909|1|76||3^300;4^300;5^300||2|0|0|0|-1|0|0|0|0|0|0|0|0|0|0||1^300;2^1000;3^300|10^5000||9999|0|-1|0|0|1|1^3000;3^3000||
100005|0|40|4|15|0|4|100005|9413|7909|1|76||3^300;4^300;5^300||2|0|0|0|-1|0|0|0|0|0|0|0|0|0|0||1^300;2^1000;3^300|10^5000||9999|0|-1|0|0|1|1^3000;3^3000||
100006|0|40|6|15|0|4|100006|9414|7909|1|76||3^300;4^300;5^300||2|0|0|0|-1|0|0|0|0|0|0|0|0|0|0||1^300;2^1000;3^300|10^5000||9999|0|-1|0|0|1|1^3000;3^3000||
(end of file)
```

Add a new Item (patchserver): `text.db`
```
INSERT INTO item_templates (item_id, item_name, item_description)
VALUES (100001, "Shadowed Doch Gul Robe of Myth", "This Robe was hoarded by Crom Cruach himself, out of fear for the devastating power it holds. This doesn't break Exalted Aura, nor Doch Gul Aura, and when worn as a full set also gives up to +720 healing to Natures Touch and +1080 damage to Lightning Strike.");

INSERT INTO item_templates (item_id, item_name, item_description)
VALUES (100003, "Shadowed Doch Gul Leggings of Myth", "These Leggings were hoarded by Crom Cruach himself, out of fear for the devastating power it holds. This doesn't break Exalted Aura, nor Doch Gul Aura, and when worn as a full set also gives up to +720 healing to Natures Touch and +1080 damage to Lightning Strike.");

INSERT INTO item_templates (item_id, item_name, item_description)
VALUES (100004, "Shadowed Doch Gul Circlet of Myth", "This Circlet was hoarded by Crom Cruach himself, out of fear for the devastating power it holds. This doesn't break Exalted Aura, nor Doch Gul Aura, and when worn as a full set also gives up to +720 healing to Natures Touch and +1080 damage to Lightning Strike.");

INSERT INTO item_templates (item_id, item_name, item_description)
VALUES (100005, "Shadowed Doch Gul Sandals of Myth", "These Sandals were hoarded by Crom Cruach himself, out of fear for the devastating power it holds. This doesn't break Exalted Aura, nor Doch Gul Aura, and when worn as a full set also gives up to +720 healing to Natures Touch and +1080 damage to Lightning Strike.");

INSERT INTO item_templates (item_id, item_name, item_description)
VALUES (100006, "Shadowed Doch Gul Wristguards of Myth", "These Wristguards were hoarded by Crom Cruach himself, out of fear for the devastating power it holds. This doesn't break Exalted Aura, nor Doch Gul Aura, and when worn as a full set also gives up to +720 healing to Natures Touch and +1080 damage to Lightning Strike.");
```

Add a new Conversation (patchserver): `conversation_lookup.txt`
```
...
conv 1001 cv_leif_difinitus
END_FILE
```

Add a new Mob (patchserver): `mob_data.txt`
```
...
200002,101746,0.3,Difinitus,0,0,1,-1,20,0,1,1.9,0,0,1
(end of file)
```


Add a new Item (server):
```
INSERT INTO ch_live_unitydatadb.item_templates (item_id, item_name, stackable, armour, equipment_slot, buy_price, sell_price, weight, attack_speed, item_sub_type, no_trade, damage_list, bonus_list, requirement_list, class_requirement_list, skill_id, skill_level, attack_range, missile_speed, report_back_time_male, report_back_time_female, blocks_slots, proc_skill_id, proc_skill_level, proc_skill_chance, equip_skill_id, equip_skill_level, unique_id, bind_on_equip, stat_bonus, ability_bonus, skill_bonus, max_charges, destroy_on_no_charges, avoidance_bonuses, immunity_list, damage_reductions_list)
VALUES (100001, 'Shadowed Doch Gul Robe of Myth', 0, 40, 2, 0, 0, 15, 0, 4, 1, NULL, '3^300;4^300;5^300', NULL, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '1^300;2^1000;3^300', '10^5000', NULL, 0, 0, '1^3000;3^3000', NULL, NULL);

INSERT INTO ch_live_unitydatadb.item_templates (item_id, item_name, stackable, armour, equipment_slot, buy_price, sell_price, weight, attack_speed, item_sub_type, no_trade, damage_list, bonus_list, requirement_list, class_requirement_list, skill_id, skill_level, attack_range, missile_speed, report_back_time_male, report_back_time_female, blocks_slots, proc_skill_id, proc_skill_level, proc_skill_chance, equip_skill_id, equip_skill_level, unique_id, bind_on_equip, stat_bonus, ability_bonus, skill_bonus, max_charges, destroy_on_no_charges, avoidance_bonuses, immunity_list, damage_reductions_list)
VALUES (100003, 'Shadowed Doch Gul Leggings of Myth', 0, 40, 3, 0, 0, 15, 0, 4, 1, NULL, '3^300;4^300;5^300', NULL, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '1^300;2^1000;3^300', '10^5000', NULL, 0, 0, '1^3000;3^3000', NULL, NULL);

INSERT INTO ch_live_unitydatadb.item_templates (item_id, item_name, stackable, armour, equipment_slot, buy_price, sell_price, weight, attack_speed, item_sub_type, no_trade, damage_list, bonus_list, requirement_list, class_requirement_list, skill_id, skill_level, attack_range, missile_speed, report_back_time_male, report_back_time_female, blocks_slots, proc_skill_id, proc_skill_level, proc_skill_chance, equip_skill_id, equip_skill_level, unique_id, bind_on_equip, stat_bonus, ability_bonus, skill_bonus, max_charges, destroy_on_no_charges, avoidance_bonuses, immunity_list, damage_reductions_list)
VALUES (100004, 'Shadowed Doch Gul Circlet of Myth', 0, 40, 1, 0, 0, 15, 0, 4, 1, NULL, '3^300;4^300;5^300', NULL, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '1^300;2^1000;3^300', '10^5000', NULL, 0, 0, '1^3000;3^3000', NULL, NULL);

INSERT INTO ch_live_unitydatadb.item_templates (item_id, item_name, stackable, armour, equipment_slot, buy_price, sell_price, weight, attack_speed, item_sub_type, no_trade, damage_list, bonus_list, requirement_list, class_requirement_list, skill_id, skill_level, attack_range, missile_speed, report_back_time_male, report_back_time_female, blocks_slots, proc_skill_id, proc_skill_level, proc_skill_chance, equip_skill_id, equip_skill_level, unique_id, bind_on_equip, stat_bonus, ability_bonus, skill_bonus, max_charges, destroy_on_no_charges, avoidance_bonuses, immunity_list, damage_reductions_list)
VALUES (100005, 'Shadowed Doch Gul Sandals of Myth', 0, 40, 4, 0, 0, 15, 0, 4, 1, NULL, '3^300;4^300;5^300', NULL, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '1^300;2^1000;3^300', '10^5000', NULL, 0, 0, '1^3000;3^3000', NULL, NULL);

INSERT INTO ch_live_unitydatadb.item_templates (item_id, item_name, stackable, armour, equipment_slot, buy_price, sell_price, weight, attack_speed, item_sub_type, no_trade, damage_list, bonus_list, requirement_list, class_requirement_list, skill_id, skill_level, attack_range, missile_speed, report_back_time_male, report_back_time_female, blocks_slots, proc_skill_id, proc_skill_level, proc_skill_chance, equip_skill_id, equip_skill_level, unique_id, bind_on_equip, stat_bonus, ability_bonus, skill_bonus, max_charges, destroy_on_no_charges, avoidance_bonuses, immunity_list, damage_reductions_list)
VALUES (100006, 'Shadowed Doch Gul Wristguards of Myth', 0, 40, 6, 0, 0, 15, 0, 4, 1, NULL, '3^300;4^300;5^300', NULL, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '1^300;2^1000;3^300', '10^5000', NULL, 0, 0, '1^3000;3^3000', NULL, NULL);

```


Add a new Mob (server):
```
INSERT INTO ch_live_unitydatadb.mob_templates (mob_template_id, mob_name, aggro_range, follow_range, faction_id, opinion_base, level, hitpoints, loot_table, min_coins, max_coins, kills_per_level, conversation_id, attack, defence, attack_speed, energy, skill_list, radius, armour_value, model_scale, damage_list, resistance_list, mob_power, max_attack_range, mob_race, missile_speed, report_back_time, ai_template_id, xp, num_drops, perm_status_effects, blocks_attacks, avoidance_ratings, spot_hidden, immunity_list, damage_reductions_list, no_ability_test, mob_type)
VALUES (200002, 'Difinitus', 0, 0, 1, 51, 0, 100, NULL, 0, 0, NULL, 1002, 0, 0, 0, 0, NULL, .3, 5, 1, NULL, NULL, 0, 1, 20, 0, 0, 0, 0, 1, NULL, 0, NULL, 0, NULL, '7,1.00', 0, 0);

INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (100002, 2, 20, 236.14, 5, -245.70, 'stand', '200002,1', 1, 200, 90, 0, 0, 0);
```

```

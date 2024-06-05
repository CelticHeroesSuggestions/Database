## Crafting

Possible steps to make crafting:

### Adding the vendors

Create the Forge, Crafting Table, and Cauldron mobs, can use IDs 922, 144, and 228. Copy from the Oven mob:
```
# Forging, replace ID 922
DELETE FROM `mob_templates` WHERE `mob_template_id`=922;
INSERT INTO `mob_templates` (`mob_template_id`, `mob_name`, `aggro_range`, `follow_range`, `faction_id`, `opinion_base`, `level`, `hitpoints`, `loot_table`, `min_coins`, `max_coins`, `kills_per_level`, `conversation_id`, `attack`, `defence`, `attack_speed`, `energy`, `skill_list`, `radius`, `armour_value`, `model_scale`, `damage_list`, `resistance_list`, `mob_power`, `max_attack_range`, `mob_race`, `missile_speed`, `report_back_time`, `ai_template_id`, `xp`, `num_drops`, `perm_status_effects`, `blocks_attacks`, `avoidance_ratings`, `spot_hidden`, `immunity_list`, `damage_reductions_list`, `no_ability_test`, `mob_type`) VALUES (922, 'Forge', 0, 0, 3, 51, 0, 200, '', 0, 0, NULL, 737, 0, 0, 0, 0, '', 0.7, 5, 1, '', '', 0, 1, 20, 0, 0, 0, 0, 1, '', b'0', '', 0, '', '', b'0', 0);

# Crafting, replace ID 144
DELETE FROM `mob_templates` WHERE `mob_template_id`=144;
INSERT INTO `mob_templates` (`mob_template_id`, `mob_name`, `aggro_range`, `follow_range`, `faction_id`, `opinion_base`, `level`, `hitpoints`, `loot_table`, `min_coins`, `max_coins`, `kills_per_level`, `conversation_id`, `attack`, `defence`, `attack_speed`, `energy`, `skill_list`, `radius`, `armour_value`, `model_scale`, `damage_list`, `resistance_list`, `mob_power`, `max_attack_range`, `mob_race`, `missile_speed`, `report_back_time`, `ai_template_id`, `xp`, `num_drops`, `perm_status_effects`, `blocks_attacks`, `avoidance_ratings`, `spot_hidden`, `immunity_list`, `damage_reductions_list`, `no_ability_test`, `mob_type`) VALUES (144, 'Workbench', 0, 0, 3, 51, 0, 200, '', 0, 0, NULL, 1009, 0, 0, 0, 0, '', 0.7, 5, 1, '', '', 0, 1, 20, 0, 0, 0, 0, 1, '', b'0', '', 0, '', '', b'0', 0);

# Alchemy, replace ID 228
DELETE FROM `mob_templates` WHERE `mob_template_id`=228;
INSERT INTO `mob_templates` (`mob_template_id`, `mob_name`, `aggro_range`, `follow_range`, `faction_id`, `opinion_base`, `level`, `hitpoints`, `loot_table`, `min_coins`, `max_coins`, `kills_per_level`, `conversation_id`, `attack`, `defence`, `attack_speed`, `energy`, `skill_list`, `radius`, `armour_value`, `model_scale`, `damage_list`, `resistance_list`, `mob_power`, `max_attack_range`, `mob_race`, `missile_speed`, `report_back_time`, `ai_template_id`, `xp`, `num_drops`, `perm_status_effects`, `blocks_attacks`, `avoidance_ratings`, `spot_hidden`, `immunity_list`, `damage_reductions_list`, `no_ability_test`, `mob_type`) VALUES (228, 'Cauldron', 0, 0, 3, 51, 0, 200, '', 0, 0, NULL, 1010, 0, 0, 0, 0, '', 0.7, 5, 1, '', '', 0, 1, 20, 0, 0, 0, 0, 1, '', b'0', '', 0, '', '', b'0', 0);

# Alchemist trainer
DELETE FROM `mob_templates` WHERE `mob_template_id`=140771;
INSERT INTO `mob_templates` (`mob_template_id`, `mob_name`, `aggro_range`, `follow_range`, `faction_id`, `opinion_base`, `level`, `hitpoints`, `loot_table`, `min_coins`, `max_coins`, `kills_per_level`, `conversation_id`, `attack`, `defence`, `attack_speed`, `energy`, `skill_list`, `radius`, `armour_value`, `model_scale`, `damage_list`, `resistance_list`, `mob_power`, `max_attack_range`, `mob_race`, `missile_speed`, `report_back_time`, `ai_template_id`, `xp`, `num_drops`, `perm_status_effects`, `blocks_attacks`, `avoidance_ratings`, `spot_hidden`, `immunity_list`, `damage_reductions_list`, `no_ability_test`, `mob_type`) VALUES (140771, 'Charlotte the Alchemist', 0, 0, 1, 51, 0, 100, '', 0, 0, NULL, 1014, 0, 0, 0, 0, '', 0.3, 5, 1.15, '', '', 0, 1, 20, 0, 0, 0, 0, 1, '', b'0', '', 0, '', '', b'0', 0);

```

Add the conversations to the `conversation_lookup.txt` file

```
...
conv 737 cv_forging_station_npc
...
conv 1009 cv_crafting_station_npc
conv 1010 cv_alchemy_station_npc
conv 1011 cv_crafting_master
conv 1012 cv_forging_master
conv 1013 cv_alchemy_master
conv 1014 cv_crafting_charlotte_alchemist
```

Add the mobs to mob_data.txt:
```
...
228,258,0.3,Cauldron,0,0,1,-1,20,0,0.9,1.7,0,-5,2

229,131,0.3,[Master Craftswoman] Haileigh the Acute,1000,3,1,-1,20,0,1,1.8,0,0,1
230,76,0.3,[Master Craftsman] Leif the Inventor,1000,3,1,-1,20,0,1,1.8,0,0,1
267,76,0.3,[Master Craftsman] Bob the Builder,1000,3,1,-1,20,0,1,1.8,0,0,1
10011,76,0.3,[Master Craftsman] Daniel the Crafty,1000,3,1,-1,20,0,1,1.8,0,0,1
70070,76,0.3,[Master Craftsman] Pak the Curious,1000,3,1,-1,20,0,1,1.8,0,0,1

269,76,0.3,[Master Alchemist] Sawyer the Alchemist,1000,3,1,-1,20,0,1,1.8,0,0,1
70084,76,0.3,[Master Alchemist] Iggy the Alchemist,1000,3,1,-1,20,0,1,1.8,0,0,1
70103,76,0.3,[Master Alchemist] Aiden the Alchemist,1000,3,1,-1,20,0,1,1.8,0,0,1
70104,76,0.3,[Master Alchemist] Tron the Alchemist,1000,3,1,-1,20,0,1,1.8,0,0,1
70105,76,0.3,[Master Alchemist] Era the Alchemist,1000,3,1,-1,20,0,1,1.8,0,0,1

70980,76,0.3,[Master Blacksmith] Nyna the Blacksmith,1000,3,1,-1,20,0,1,1.8,0,0,1
70981,76,0.3,[Master Blacksmith] Toothy the Blacksmith,1000,3,1,-1,20,0,1,1.8,0,0,1
70982,76,0.3,[Master Blacksmith] Shaem the Blacksmith,1000,3,1,-1,20,0,1,1.8,0,0,1
70983,76,0.3,[Master Blacksmith] The Honoured One,1000,3,1,-1,20,0,1,1.8,0,0,1
70984,76,0.3,[Master Blacksmith] Ernie the Blacksmith,1000,3,1,-1,20,0,1,1.8,0,0,1
70984,76,0.3,[Master Blacksmith] Furyion the Blacksmith,1000,3,1,-1,20,0,1,1.8,0,0,1
```

Add the mobs to the database:
```
# Cauldron
DELETE FROM `mob_templates` WHERE `mob_template_id`=228;
INSERT INTO `mob_templates` (`mob_template_id`, `mob_name`, `aggro_range`, `follow_range`, `faction_id`, `opinion_base`, `level`, `hitpoints`, `loot_table`, `min_coins`, `max_coins`, `kills_per_level`, `conversation_id`, `attack`, `defence`, `attack_speed`, `energy`, `skill_list`, `radius`, `armour_value`, `model_scale`, `damage_list`, `resistance_list`, `mob_power`, `max_attack_range`, `mob_race`, `missile_speed`, `report_back_time`, `ai_template_id`, `xp`, `num_drops`, `perm_status_effects`, `blocks_attacks`, `avoidance_ratings`, `spot_hidden`, `immunity_list`, `damage_reductions_list`, `no_ability_test`, `mob_type`) VALUES (228, 'Cauldron', 0, 0, 3, 51, 0, 200, '', 0, 0, NULL, 1010, 0, 0, 0, 0, '', 0.3, 5, 1, '', '', 0, 1, 20, 0, 0, 0, 0, 1, '', b'0', '', 0, '', '', b'0', 0);

# Craftsmen
DELETE FROM `mob_templates` WHERE `mob_template_id`=229;
INSERT INTO `mob_templates` (`mob_template_id`, `mob_name`, `aggro_range`, `follow_range`, `faction_id`, `opinion_base`, `level`, `hitpoints`, `loot_table`, `min_coins`, `max_coins`, `kills_per_level`, `conversation_id`, `attack`, `defence`, `attack_speed`, `energy`, `skill_list`, `radius`, `armour_value`, `model_scale`, `damage_list`, `resistance_list`, `mob_power`, `max_attack_range`, `mob_race`, `missile_speed`, `report_back_time`, `ai_template_id`, `xp`, `num_drops`, `perm_status_effects`, `blocks_attacks`, `avoidance_ratings`, `spot_hidden`, `immunity_list`, `damage_reductions_list`, `no_ability_test`, `mob_type`) VALUES (229, '[Master Craftswoman] Alice the Acute', 0, 40, 0, 51, 0, 100, '', 0, 0, NULL, 1011, 100, 100, 1000, 100, '', 0.3, 100, 1, '', '', 0, 1, 20, 0, 0, 0, 100, 1, '', b'0', '', 0, '', '7,1.00', b'0', 0);
DELETE FROM `mob_templates` WHERE `mob_template_id`=230;
INSERT INTO `mob_templates` (`mob_template_id`, `mob_name`, `aggro_range`, `follow_range`, `faction_id`, `opinion_base`, `level`, `hitpoints`, `loot_table`, `min_coins`, `max_coins`, `kills_per_level`, `conversation_id`, `attack`, `defence`, `attack_speed`, `energy`, `skill_list`, `radius`, `armour_value`, `model_scale`, `damage_list`, `resistance_list`, `mob_power`, `max_attack_range`, `mob_race`, `missile_speed`, `report_back_time`, `ai_template_id`, `xp`, `num_drops`, `perm_status_effects`, `blocks_attacks`, `avoidance_ratings`, `spot_hidden`, `immunity_list`, `damage_reductions_list`, `no_ability_test`, `mob_type`) VALUES (230, '[Master Craftsman] Leif the Inventor', 0, 40, 0, 51, 0, 100, '', 0, 0, NULL, 1011, 100, 100, 1000, 100, '', 0.3, 100, 1, '', '', 0, 1, 20, 0, 0, 0, 100, 1, '', b'0', '', 0, '', '7,1.00', b'0', 0);
DELETE FROM `mob_templates` WHERE `mob_template_id`=267;
INSERT INTO `mob_templates` (`mob_template_id`, `mob_name`, `aggro_range`, `follow_range`, `faction_id`, `opinion_base`, `level`, `hitpoints`, `loot_table`, `min_coins`, `max_coins`, `kills_per_level`, `conversation_id`, `attack`, `defence`, `attack_speed`, `energy`, `skill_list`, `radius`, `armour_value`, `model_scale`, `damage_list`, `resistance_list`, `mob_power`, `max_attack_range`, `mob_race`, `missile_speed`, `report_back_time`, `ai_template_id`, `xp`, `num_drops`, `perm_status_effects`, `blocks_attacks`, `avoidance_ratings`, `spot_hidden`, `immunity_list`, `damage_reductions_list`, `no_ability_test`, `mob_type`) VALUES (267, '[Master Craftsman] Bob the Builder', 0, 40, 0, 51, 0, 100, '', 0, 0, NULL, 1011, 100, 100, 1000, 100, '', 0.3, 100, 1, '', '', 0, 1, 20, 0, 0, 0, 100, 1, '', b'0', '', 0, '', '7,1.00', b'0', 0);
DELETE FROM `mob_templates` WHERE `mob_template_id`=10011;
INSERT INTO `mob_templates` (`mob_template_id`, `mob_name`, `aggro_range`, `follow_range`, `faction_id`, `opinion_base`, `level`, `hitpoints`, `loot_table`, `min_coins`, `max_coins`, `kills_per_level`, `conversation_id`, `attack`, `defence`, `attack_speed`, `energy`, `skill_list`, `radius`, `armour_value`, `model_scale`, `damage_list`, `resistance_list`, `mob_power`, `max_attack_range`, `mob_race`, `missile_speed`, `report_back_time`, `ai_template_id`, `xp`, `num_drops`, `perm_status_effects`, `blocks_attacks`, `avoidance_ratings`, `spot_hidden`, `immunity_list`, `damage_reductions_list`, `no_ability_test`, `mob_type`) VALUES (10011, '[Master Craftsman] Steven the Crafty', 0, 40, 0, 51, 0, 100, '', 0, 0, NULL, 1011, 100, 100, 1000, 100, '', 0.3, 100, 1, '', '', 0, 1, 20, 0, 0, 0, 100, 1, '', b'0', '', 0, '', '7,1.00', b'0', 0);
DELETE FROM `mob_templates` WHERE `mob_template_id`=70070;
INSERT INTO `mob_templates` (`mob_template_id`, `mob_name`, `aggro_range`, `follow_range`, `faction_id`, `opinion_base`, `level`, `hitpoints`, `loot_table`, `min_coins`, `max_coins`, `kills_per_level`, `conversation_id`, `attack`, `defence`, `attack_speed`, `energy`, `skill_list`, `radius`, `armour_value`, `model_scale`, `damage_list`, `resistance_list`, `mob_power`, `max_attack_range`, `mob_race`, `missile_speed`, `report_back_time`, `ai_template_id`, `xp`, `num_drops`, `perm_status_effects`, `blocks_attacks`, `avoidance_ratings`, `spot_hidden`, `immunity_list`, `damage_reductions_list`, `no_ability_test`, `mob_type`) VALUES (70070, '[Master Craftsman] Deepak the Curious', 0, 40, 0, 51, 0, 100, '', 0, 0, NULL, 1011, 100, 100, 1000, 100, '', 0.3, 100, 1, '', '', 0, 1, 20, 0, 0, 0, 100, 1, '', b'0', '', 0, '', '7,1.00', b'0', 0);

# alchemists
DELETE FROM `mob_templates` WHERE `mob_template_id`=269;
INSERT INTO `mob_templates` (`mob_template_id`, `mob_name`, `aggro_range`, `follow_range`, `faction_id`, `opinion_base`, `level`, `hitpoints`, `loot_table`, `min_coins`, `max_coins`, `kills_per_level`, `conversation_id`, `attack`, `defence`, `attack_speed`, `energy`, `skill_list`, `radius`, `armour_value`, `model_scale`, `damage_list`, `resistance_list`, `mob_power`, `max_attack_range`, `mob_race`, `missile_speed`, `report_back_time`, `ai_template_id`, `xp`, `num_drops`, `perm_status_effects`, `blocks_attacks`, `avoidance_ratings`, `spot_hidden`, `immunity_list`, `damage_reductions_list`, `no_ability_test`, `mob_type`) VALUES (269, '[Master Alchemist] Sawyer the Alchemist', 0, 40, 0, 51, 0, 100, '', 0, 0, NULL, 1013, 100, 100, 1000, 100, '', 0.3, 100, 1, '', '', 0, 1, 20, 0, 0, 0, 100, 1, '', b'0', '', 0, '', '7,1.00', b'0', 0);
DELETE FROM `mob_templates` WHERE `mob_template_id`=70084;
INSERT INTO `mob_templates` (`mob_template_id`, `mob_name`, `aggro_range`, `follow_range`, `faction_id`, `opinion_base`, `level`, `hitpoints`, `loot_table`, `min_coins`, `max_coins`, `kills_per_level`, `conversation_id`, `attack`, `defence`, `attack_speed`, `energy`, `skill_list`, `radius`, `armour_value`, `model_scale`, `damage_list`, `resistance_list`, `mob_power`, `max_attack_range`, `mob_race`, `missile_speed`, `report_back_time`, `ai_template_id`, `xp`, `num_drops`, `perm_status_effects`, `blocks_attacks`, `avoidance_ratings`, `spot_hidden`, `immunity_list`, `damage_reductions_list`, `no_ability_test`, `mob_type`) VALUES (70084, '[Master Alchemist] Iggy the Alchemist', 0, 40, 0, 51, 0, 100, '', 0, 0, NULL, 1013, 100, 100, 1000, 100, '', 0.3, 100, 1, '', '', 0, 1, 20, 0, 0, 0, 100, 1, '', b'0', '', 0, '', '7,1.00', b'0', 0);
DELETE FROM `mob_templates` WHERE `mob_template_id`=70103;
INSERT INTO `mob_templates` (`mob_template_id`, `mob_name`, `aggro_range`, `follow_range`, `faction_id`, `opinion_base`, `level`, `hitpoints`, `loot_table`, `min_coins`, `max_coins`, `kills_per_level`, `conversation_id`, `attack`, `defence`, `attack_speed`, `energy`, `skill_list`, `radius`, `armour_value`, `model_scale`, `damage_list`, `resistance_list`, `mob_power`, `max_attack_range`, `mob_race`, `missile_speed`, `report_back_time`, `ai_template_id`, `xp`, `num_drops`, `perm_status_effects`, `blocks_attacks`, `avoidance_ratings`, `spot_hidden`, `immunity_list`, `damage_reductions_list`, `no_ability_test`, `mob_type`) VALUES (70103, '[Master Alchemist] Aiden the Alchemist', 0, 40, 0, 51, 0, 100, '', 0, 0, NULL, 1013, 100, 100, 1000, 100, '', 0.3, 100, 1, '', '', 0, 1, 20, 0, 0, 0, 100, 1, '', b'0', '', 0, '', '7,1.00', b'0', 0);
DELETE FROM `mob_templates` WHERE `mob_template_id`=70104;
INSERT INTO `mob_templates` (`mob_template_id`, `mob_name`, `aggro_range`, `follow_range`, `faction_id`, `opinion_base`, `level`, `hitpoints`, `loot_table`, `min_coins`, `max_coins`, `kills_per_level`, `conversation_id`, `attack`, `defence`, `attack_speed`, `energy`, `skill_list`, `radius`, `armour_value`, `model_scale`, `damage_list`, `resistance_list`, `mob_power`, `max_attack_range`, `mob_race`, `missile_speed`, `report_back_time`, `ai_template_id`, `xp`, `num_drops`, `perm_status_effects`, `blocks_attacks`, `avoidance_ratings`, `spot_hidden`, `immunity_list`, `damage_reductions_list`, `no_ability_test`, `mob_type`) VALUES (70104, '[Master Alchemist] Tron the Alchemist', 0, 40, 0, 51, 0, 100, '', 0, 0, NULL, 1013, 100, 100, 1000, 100, '', 0.3, 100, 1, '', '', 0, 1, 20, 0, 0, 0, 100, 1, '', b'0', '', 0, '', '7,1.00', b'0', 0);
DELETE FROM `mob_templates` WHERE `mob_template_id`=70105;
INSERT INTO `mob_templates` (`mob_template_id`, `mob_name`, `aggro_range`, `follow_range`, `faction_id`, `opinion_base`, `level`, `hitpoints`, `loot_table`, `min_coins`, `max_coins`, `kills_per_level`, `conversation_id`, `attack`, `defence`, `attack_speed`, `energy`, `skill_list`, `radius`, `armour_value`, `model_scale`, `damage_list`, `resistance_list`, `mob_power`, `max_attack_range`, `mob_race`, `missile_speed`, `report_back_time`, `ai_template_id`, `xp`, `num_drops`, `perm_status_effects`, `blocks_attacks`, `avoidance_ratings`, `spot_hidden`, `immunity_list`, `damage_reductions_list`, `no_ability_test`, `mob_type`) VALUES (70105, '[Master Alchemist] Era the Alchemist', 0, 40, 0, 51, 0, 100, '', 0, 0, NULL, 1013, 100, 100, 1000, 100, '', 0.3, 100, 1, '', '', 0, 1, 20, 0, 0, 0, 100, 1, '', b'0', '', 0, '', '7,1.00', b'0', 0);

# blacksmiths
DELETE FROM `mob_templates` WHERE `mob_template_id`=70980;
INSERT INTO `mob_templates` (`mob_template_id`, `mob_name`, `aggro_range`, `follow_range`, `faction_id`, `opinion_base`, `level`, `hitpoints`, `loot_table`, `min_coins`, `max_coins`, `kills_per_level`, `conversation_id`, `attack`, `defence`, `attack_speed`, `energy`, `skill_list`, `radius`, `armour_value`, `model_scale`, `damage_list`, `resistance_list`, `mob_power`, `max_attack_range`, `mob_race`, `missile_speed`, `report_back_time`, `ai_template_id`, `xp`, `num_drops`, `perm_status_effects`, `blocks_attacks`, `avoidance_ratings`, `spot_hidden`, `immunity_list`, `damage_reductions_list`, `no_ability_test`, `mob_type`) VALUES (70980, '[Master Blacksmith] Nyna the Blacksmith', 0, 40, 0, 51, 0, 100, '', 0, 0, NULL, 1012, 100, 100, 1000, 100, '', 0.3, 100, 1, '', '', 0, 1, 20, 0, 0, 0, 100, 1, '', b'0', '', 0, '', '7,1.00', b'0', 0);
DELETE FROM `mob_templates` WHERE `mob_template_id`=70981;
INSERT INTO `mob_templates` (`mob_template_id`, `mob_name`, `aggro_range`, `follow_range`, `faction_id`, `opinion_base`, `level`, `hitpoints`, `loot_table`, `min_coins`, `max_coins`, `kills_per_level`, `conversation_id`, `attack`, `defence`, `attack_speed`, `energy`, `skill_list`, `radius`, `armour_value`, `model_scale`, `damage_list`, `resistance_list`, `mob_power`, `max_attack_range`, `mob_race`, `missile_speed`, `report_back_time`, `ai_template_id`, `xp`, `num_drops`, `perm_status_effects`, `blocks_attacks`, `avoidance_ratings`, `spot_hidden`, `immunity_list`, `damage_reductions_list`, `no_ability_test`, `mob_type`) VALUES (70981, '[Master Blacksmith] Toothy the Blacksmith', 0, 40, 0, 51, 0, 100, '', 0, 0, NULL, 1012, 100, 100, 1000, 100, '', 0.3, 100, 1, '', '', 0, 1, 20, 0, 0, 0, 100, 1, '', b'0', '', 0, '', '7,1.00', b'0', 0);
DELETE FROM `mob_templates` WHERE `mob_template_id`=70982;
INSERT INTO `mob_templates` (`mob_template_id`, `mob_name`, `aggro_range`, `follow_range`, `faction_id`, `opinion_base`, `level`, `hitpoints`, `loot_table`, `min_coins`, `max_coins`, `kills_per_level`, `conversation_id`, `attack`, `defence`, `attack_speed`, `energy`, `skill_list`, `radius`, `armour_value`, `model_scale`, `damage_list`, `resistance_list`, `mob_power`, `max_attack_range`, `mob_race`, `missile_speed`, `report_back_time`, `ai_template_id`, `xp`, `num_drops`, `perm_status_effects`, `blocks_attacks`, `avoidance_ratings`, `spot_hidden`, `immunity_list`, `damage_reductions_list`, `no_ability_test`, `mob_type`) VALUES (70982, '[Master Blacksmith] Shaim the Blacksmith', 0, 40, 0, 51, 0, 100, '', 0, 0, NULL, 1012, 100, 100, 1000, 100, '', 0.3, 100, 1, '', '', 0, 1, 20, 0, 0, 0, 100, 1, '', b'0', '', 0, '', '7,1.00', b'0', 0);
DELETE FROM `mob_templates` WHERE `mob_template_id`=70983;
INSERT INTO `mob_templates` (`mob_template_id`, `mob_name`, `aggro_range`, `follow_range`, `faction_id`, `opinion_base`, `level`, `hitpoints`, `loot_table`, `min_coins`, `max_coins`, `kills_per_level`, `conversation_id`, `attack`, `defence`, `attack_speed`, `energy`, `skill_list`, `radius`, `armour_value`, `model_scale`, `damage_list`, `resistance_list`, `mob_power`, `max_attack_range`, `mob_race`, `missile_speed`, `report_back_time`, `ai_template_id`, `xp`, `num_drops`, `perm_status_effects`, `blocks_attacks`, `avoidance_ratings`, `spot_hidden`, `immunity_list`, `damage_reductions_list`, `no_ability_test`, `mob_type`) VALUES (70983, '[Master Blacksmith] The Honoured One', 0, 40, 0, 51, 0, 100, '', 0, 0, NULL, 1012, 100, 100, 1000, 100, '', 0.3, 100, 1, '', '', 0, 1, 20, 0, 0, 0, 100, 1, '', b'0', '', 0, '', '7,1.00', b'0', 0);
DELETE FROM `mob_templates` WHERE `mob_template_id`=70984;
INSERT INTO `mob_templates` (`mob_template_id`, `mob_name`, `aggro_range`, `follow_range`, `faction_id`, `opinion_base`, `level`, `hitpoints`, `loot_table`, `min_coins`, `max_coins`, `kills_per_level`, `conversation_id`, `attack`, `defence`, `attack_speed`, `energy`, `skill_list`, `radius`, `armour_value`, `model_scale`, `damage_list`, `resistance_list`, `mob_power`, `max_attack_range`, `mob_race`, `missile_speed`, `report_back_time`, `ai_template_id`, `xp`, `num_drops`, `perm_status_effects`, `blocks_attacks`, `avoidance_ratings`, `spot_hidden`, `immunity_list`, `damage_reductions_list`, `no_ability_test`, `mob_type`) VALUES (70984, '[Master Blacksmith] Ernie the Blacksmith', 0, 40, 0, 51, 0, 100, '', 0, 0, NULL, 1012, 100, 100, 1000, 100, '', 0.3, 100, 1, '', '', 0, 1, 20, 0, 0, 0, 100, 1, '', b'0', '', 0, '', '7,1.00', b'0', 0);
DELETE FROM `mob_templates` WHERE `mob_template_id`=70985;
INSERT INTO `mob_templates` (`mob_template_id`, `mob_name`, `aggro_range`, `follow_range`, `faction_id`, `opinion_base`, `level`, `hitpoints`, `loot_table`, `min_coins`, `max_coins`, `kills_per_level`, `conversation_id`, `attack`, `defence`, `attack_speed`, `energy`, `skill_list`, `radius`, `armour_value`, `model_scale`, `damage_list`, `resistance_list`, `mob_power`, `max_attack_range`, `mob_race`, `missile_speed`, `report_back_time`, `ai_template_id`, `xp`, `num_drops`, `perm_status_effects`, `blocks_attacks`, `avoidance_ratings`, `spot_hidden`, `immunity_list`, `damage_reductions_list`, `no_ability_test`, `mob_type`) VALUES (70985, '[Master Blacksmith] Furyion the Blacksmith', 0, 40, 0, 51, 0, 100, '', 0, 0, NULL, 1012, 100, 100, 1000, 100, '', 0.3, 100, 1, '', '', 0, 1, 20, 0, 0, 0, 100, 1, '', b'0', '', 0, '', '7,1.00', b'0', 0);
```

Spawn the mobs:
```
# Forge Farcrag
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20500;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20500, 93, 15, 5.22, -111, 122, 'stand', '922,1', 1, 0, 20, 0, 0, 0);
# Blacksmith Farcrag
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20600;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20600, 93, 15, 8.4, -111, 118.85, 'stand', '70980,1', 1, 300, 20, 0, 0, 0);
# Forge Shalemont
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20501;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20501, 6, 15, 53, 0, 6.75, 'stand', '922,1', 1, 0, 20, 0, 0, 0);
# Blacksmith Shalemont
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20601;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20601, 6, 15, 53.13, 0, 11.27, 'stand', '70981,1', 1, 280, 20, 0, 0, 0);
# Forge Stonevale
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20502;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20502, 3, 15, 32.8, 0, -20.38, 'stand', '922,1', 1, 0, 20, 0, 0, 0);
# Blacksmith Stonevale
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20602;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20602, 3, 15, 34.82, 0, -19.08, 'stand', '70982,1', 1, 237, 20, 0, 0, 0);
# Forge Otherworld
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20503;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20503, 7, 15, -616.75, 0, 138, 'stand', '922,1', 1, 0, 20, 0, 0, 0);
# Blacksmith Otherworld
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20603;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20603, 7, 15, -619.35, 0, 137.25, 'stand', '70985,1', 1, 165, 20, 0, 0, 0);
# Forge Carrowmore
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20504;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20504, 10, 15, -28.65, 0, -35.95, 'stand', '922,1', 1, 0, 20, 0, 0, 0);
# Blacksmith Carrowmore
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20604;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20604, 10, 15, -28.54, 0, -32.32, 'stand', '70984,1', 1, 85, 20, 0, 0, 0);
# Forge Tower
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20505;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20505, 15, 15, -226.28, 27, 41.6, 'stand', '922,1', 1, 0, 20, 0, 0, 0);
# Blacksmith Tower
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20605;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20605, 15, 15, -222.77, 27, 40.08, 'stand', '70983,1', 1, 320, 20, 0, 0, 0);

# Crafting Table Crookback
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20506;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20506, 4, 15, 92.8, -10, -68, 'stand', '144,1', 1, 0, 20, 0, 0, 0);
# Crafting Master Crookback
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20606;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20606, 4, 15, 89.78, -10, -68.57, 'stand', '229,1', 1, 40, 20, 0, 0, 0);
# Crafting Table Fingals
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20508;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20508, 11, 15, 836.5, 0, 331.5, 'stand', '144,1', 1, 0, 20, 0, 0, 0);
# Crafting Master Fingals
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20608;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20608, 11, 15, 838.9, 0, 329.25, 'stand', '230,1', 1, 168, 20, 0, 0, 0);
# Crafting Table Sewers
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20509;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20509, 12, 15, 5.3, 0, 399, 'stand', '144,1', 1, 0, 20, 0, 0, 0);
# Crafting Master Sewers
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20609;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20609, 12, 15, 2.76, 0, 399.6, 'stand', '70070,1', 1, 170, 10, 0, 0, 0);
# Crafting Table Carrowmore
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20510;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20510, 10, 15, -355, 0, 469, 'stand', '144,1', 1, 0, 20, 0, 0, 0);
# Crafting Master Carrowmore
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20610;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20610, 10, 15, -353.5, 0, 472, 'stand', '267,1', 1, 45, 20, 0, 0, 0);
# Crafting Table Gardens
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20511;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20511, 24, 15, -89.6, 65, 62.96, 'stand', '144,1', 1, 0, 20, 0, 0, 0);
# Crafting Master Gardens
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20611;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20611, 24, 15, -90.6, 66, 60.74, 'stand', '10011,1', 1, 85, 20, 0, 0, 0);

# Cauldron Dustwither
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20512;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20512, 5, 15, 1.58, 0, -65.8, 'stand', '228,1', 1, 0, 20, 0, 0, 0);
# Alchemist Dustwither
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20612;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20612, 5, 15, -.83, 0, -65.77, 'stand', '70084,1', 1, 45, 50, 0, 0, 0);
# Cauldron Tavern
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20513;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20513, 9, 15, -11.42, 0, 32.34, 'stand', '228,1', 1, 0, 20, 0, 0, 0);
# Alchemist Tavern
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20613;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20613, 9, 15, -12.09, 0, 29.98, 'stand', '269,1', 1, 135, 20, 0, 0, 0);
# Cauldron Otherworld
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20514;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20514, 7, 15, 290.46, 0, -231.5, 'stand', '228,1', 1, 0, 20, 0, 0, 0);
# Alchemist Otherworld
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20614;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20614, 7, 15, 293.41, 0, -230.62, 'stand', '70105,1', 1, 210, 20, 0, 0, 0);
# Cauldron Carrowmore
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20515;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20515, 10, 15, 238.3, 0, 825.73, 'stand', '228,1', 1, 210, 20, 0, 0, 0);
# Alchemist Carrowmore
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20615;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20615, 10, 15, 240.3, 0, 825.98, 'stand', '70103,1', 1, 210, 20, 0, 0, 0);
# Cauldron Gardens
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20516;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20516, 24, 15, -65.74, 0, 43.18, 'stand', '228,1', 1, 0, 20, 0, 0, 0);
# Alchemist Gardens
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20616;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20616, 24, 15, -66.99, 0, 44.82, 'stand', '70104,1', 1, 10, 20, 0, 0, 0);
```

Add the vendors to the `token_vendors` SQL table:

```
DELETE FROM `token_vendors` WHERE `token_vendor_id` >= 484 AND `token_vendor_id` <= 499;
INSERT INTO `token_vendors` (`token_vendor_id`, `token_vendor_name`, `zone_id`, `npc_id`, `faction_id`, `faction_level`) VALUES (484, 'Crafting Crookback', 4, 144, 0, 0);
INSERT INTO `token_vendors` (`token_vendor_id`, `token_vendor_name`, `zone_id`, `npc_id`, `faction_id`, `faction_level`) VALUES (485, 'Crafting Fingals', 11, 144, 0, 0);
INSERT INTO `token_vendors` (`token_vendor_id`, `token_vendor_name`, `zone_id`, `npc_id`, `faction_id`, `faction_level`) VALUES (486, 'Crafting Sewers', 12, 144, 0, 0);
INSERT INTO `token_vendors` (`token_vendor_id`, `token_vendor_name`, `zone_id`, `npc_id`, `faction_id`, `faction_level`) VALUES (487, 'Crafting Carrowmore', 10, 144, 0, 0);
INSERT INTO `token_vendors` (`token_vendor_id`, `token_vendor_name`, `zone_id`, `npc_id`, `faction_id`, `faction_level`) VALUES (488, 'Crafting Gardens', 24, 144, 0, 0);
INSERT INTO `token_vendors` (`token_vendor_id`, `token_vendor_name`, `zone_id`, `npc_id`, `faction_id`, `faction_level`) VALUES (489, 'Alchemy Dustwither', 5, 228, 0, 0);
INSERT INTO `token_vendors` (`token_vendor_id`, `token_vendor_name`, `zone_id`, `npc_id`, `faction_id`, `faction_level`) VALUES (490, 'Alchemy Tavern', 9, 228, 0, 0);
INSERT INTO `token_vendors` (`token_vendor_id`, `token_vendor_name`, `zone_id`, `npc_id`, `faction_id`, `faction_level`) VALUES (491, 'Alchemy Otherworld', 7, 228, 0, 0);
INSERT INTO `token_vendors` (`token_vendor_id`, `token_vendor_name`, `zone_id`, `npc_id`, `faction_id`, `faction_level`) VALUES (492, 'Alchemy Carrowmore', 10, 228, 0, 0);
INSERT INTO `token_vendors` (`token_vendor_id`, `token_vendor_name`, `zone_id`, `npc_id`, `faction_id`, `faction_level`) VALUES (493, 'Alchemy Gardens', 24, 228, 0, 0);
INSERT INTO `token_vendors` (`token_vendor_id`, `token_vendor_name`, `zone_id`, `npc_id`, `faction_id`, `faction_level`) VALUES (494, 'Forging Farcrag', 93, 922, 0, 0);
INSERT INTO `token_vendors` (`token_vendor_id`, `token_vendor_name`, `zone_id`, `npc_id`, `faction_id`, `faction_level`) VALUES (495, 'Forging Shalemont', 6, 922, 0, 0);
INSERT INTO `token_vendors` (`token_vendor_id`, `token_vendor_name`, `zone_id`, `npc_id`, `faction_id`, `faction_level`) VALUES (496, 'Forging Stonevale', 3, 922, 0, 0);
INSERT INTO `token_vendors` (`token_vendor_id`, `token_vendor_name`, `zone_id`, `npc_id`, `faction_id`, `faction_level`) VALUES (497, 'Forging Otherworld', 7, 922, 0, 0);
INSERT INTO `token_vendors` (`token_vendor_id`, `token_vendor_name`, `zone_id`, `npc_id`, `faction_id`, `faction_level`) VALUES (498, 'Forging Carrowmore', 10, 922, 0, 0);
INSERT INTO `token_vendors` (`token_vendor_id`, `token_vendor_name`, `zone_id`, `npc_id`, `faction_id`, `faction_level`) VALUES (499, 'Forging Tower', 15, 922, 0, 0);
```

Add sand on ground for pickup.

```
# Lir's Sand
DELETE FROM `item_spawns` WHERE `item_spawn_id` >= 7000 and `item_spawn_id` <= 7009;
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7000, 2, 30, 242, 0, 56, '17075,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7001, 2, 30, 257, 0, 52, '17075,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7002, 2, 30, 268.5, 0, 41, '17075,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7003, 2, 30, 282.5, 0, 32.5, '17075,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7004, 2, 30, 294, 0, 17.5, '17075,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7005, 2, 30, 265, 0, -196.5, '17075,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7006, 2, 30, 275, 0, -195, '17075,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7007, 2, 30, 275.1, 0, -186.3, '17075,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7008, 2, 30, 273, 0, -177, '17075,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7009, 2, 30, 276, 0, -165.5, '17075,100', 30);

# Stonevale Sand
DELETE FROM `item_spawns` WHERE `item_spawn_id` >= 7010 and `item_spawn_id` <= 7019;
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7010, 3, 30, 163, 0, 36.5, '17076,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7011, 3, 30, 155, 0, 36.2, '17076,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7012, 3, 30, 115, 0, 33.6, '17076,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7013, 3, 30, 147, 0, 37.8, '17076,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7014, 3, 30, 138, 0, 32.78, '17076,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7015, 3, 30, 134.2, 0, 37.6, '17076,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7016, 3, 30, 126.5, 0, 33.4, '17076,100', 30);

# Cave Sand
DELETE FROM `item_spawns` WHERE `item_spawn_id` >= 7020 and `item_spawn_id` <= 7029;
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7020, 11, 30, 930.5, 0, 267.5, '17077,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7021, 11, 30, 940.5, 0, 267, '17077,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7022, 11, 30, 927.9, 0, 257.9, '17077,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7023, 11, 30, 919.5, 0, 220, '17077,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7024, 11, 30, 923.8, 0, 208, '17077,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7025, 11, 30, 905.5, 0, 208, '17077,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7026, 11, 30, 997.5, 0, 235, '17077,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7027, 11, 30, 982.1, 0, 234.7, '17077,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7028, 11, 30, 980.5, 0, 241.5, '17077,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7029, 11, 30, 1013, 0, 241, '17077,100', 30);

# Otherworld Sand and Dragon Eggs
DELETE FROM `item_spawns` WHERE `item_spawn_id` >= 7030 and `item_spawn_id` <= 7070;
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7030, 7, 30, -246, 0, 44.66, '17078,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7031, 7, 30, -237.7, 0, 47.38, '17078,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7032, 7, 30, -202.72, 0, 43.80, '17078,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7033, 7, 30, -202.3, 0, 27.14, '17078,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7034, 7, 30, -193.66, 0, 10.88, '17078,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7035, 7, 30, -177, 0, 2.9, '17078,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7036, 7, 30, -173.74, 0, -15.81, '17078,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7037, 7, 30, -149.76, 0, -9.65, '17078,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7038, 7, 30, -154.82, 0, 5.63, '17078,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7039, 7, 30, -160.5, 0, 24.8, '17078,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7040, 7, 30, -158.5, 0, 46.58, '17078,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7041, 7, 30, -176.69, 0, 44.57, '17078,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7042, 7, 30, -193.7, 0, 44.2, '17078,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7043, 7, 30, -136.2, 0, 16.37, '17078,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7044, 7, 30, -126.7, 0, 25.35, '17078,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7045, 7, 30, -103.8, 0, 24.14, '17078,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7046, 7, 30, -108, 0, 7.12, '17078,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7047, 7, 30, -89.31, 0, 2.03, '17078,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7048, 7, 30, -71.5, 0, -2.96, '17078,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7049, 7, 30, -56.83, 0, -8.3, '17078,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7050, 7, 30, -54.76, 0, 15.11, '17078,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7051, 7, 30, -24.99, 0, -13.35, '17078,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7052, 7, 30, -11.32, 0, 25.23, '17078,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7053, 7, 30, -1.53, 0, -46.44, '17078,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7054, 7, 30, -15.22, 0, -29.14, '17078,100', 30);
# Cobalt Dragon Eggs
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7055, 7, 30, -457, 0, 190, '58500,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7056, 7, 30, -419, 0, 174.3, '58500,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7057, 7, 30, -401, 0, 193.5, '58500,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7058, 7, 30, -383.3, 0, 194, '58500,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7059, 7, 30, -348, 0, 203.5, '58500,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7060, 7, 30, -321.4, 0, 181.11, '58500,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7061, 7, 30, -298.3, 0, 224.07, '58500,100', 30);
# Sand Dragon Eggs
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7062, 7, 30, -240.6, 0, 38.83, '58501,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7063, 7, 30, -208.5, 0, 36.41, '58501,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7064, 7, 30, -188.96, 0, 40.83, '58501,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7065, 7, 30, -160.9, 0, 11.86, '58501,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7066, 7, 30, -134.11, 0, 32, '58501,100', 30);
INSERT INTO `item_spawns` (`item_spawn_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `item_list`, `max_respawn_time`) VALUES (7067, 7, 30, -88.34, 0, 11.05, '58501,100', 30);
```

Add the crafting items to the database:

```
DELETE FROM `item_templates` WHERE `item_id`=31;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (31, 'Empty Potion', b'1', 0, -1, 0, 1, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=32;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (32, 'Empty Elixir', b'1', 0, -1, 0, 1, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=33;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (33, 'Scroll Binding Band', b'1', 0, -1, 0, 1, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=34;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (34, 'Book Trimmings', b'1', 0, -1, 0, 1, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17017;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17017, 'Common Ring Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17018;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17018, 'Common Bracelet Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17019;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17019, 'Common Necklace Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17020;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17020, 'Common Charm Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17021;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17021, 'Enchanted Ring Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17022;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17022, 'Enchanted Bracelet Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17023;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17023, 'Enchanted Necklace Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17024;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17024, 'Enchanted Charm Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17025;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17025, 'Ancient Ring Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17026;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17026, 'Ancient Bracelet Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17027;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17027, 'Ancient Charm Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '5', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17028;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17028, 'Ancient Charm Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17029;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17029, 'Arcane Ring Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '5', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17030;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17030, 'Arcane Necklace Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '5', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17031;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17031, 'Arcane Necklace Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '5', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17032;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17032, 'Arcane Charm Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '5', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17033;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17033, 'Legendary Ring Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17034;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17034, 'Legendary Necklace Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17035;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17035, 'Legendary Necklace Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17036;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17036, 'Spirited Ring Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17037;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17037, 'Spirited Ring Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17038;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17038, 'Spirited Bracelet Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17039;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17039, 'Spirited Necklace Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17040;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17040, 'Spirited Charm Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17041;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17041, 'Bonecursed Ring Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17042;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17042, 'Bonecursed Bracelet Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17043;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17043, 'Bonecursed Necklace Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17044;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17044, 'Bonecursed Charm Mould', b'0', 0, -1, 0, 0, 0, 0, 0, b'0', NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17045;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17045, 'Iron Baubles', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17046;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17046, 'Silver Baubles', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17047;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17047, 'Gold Baubles', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17048;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17048, 'Shadowy Baubles', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17049;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17049, 'Shining Baubles', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17050;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17050, 'Spirited Baubles', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17051;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17051, 'Enchanted Baubles', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17052;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17052, 'Soultrapped Baubles', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17053;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17053, 'Cursed Baubles', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17054;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17054, 'Ethereal Baubles', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17055;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17055, 'Iron Fastenings', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17056;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17056, 'Silver Fastenings', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17057;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17057, 'Gold Fastenings', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17058;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17058, 'Shadowy Fastenings', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17059;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17059, 'Shining Fastenings', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17060;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17060, 'Spirited Fastenings', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17061;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17061, 'Enchanted Fastenings', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17062;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17062, 'Soultrapped Fastenings', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17063;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17063, 'Cursed Fastenings', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17064;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17064, 'Ethereal Fastenings', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17065;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17065, 'Iron Core', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17066;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17066, 'Silver Core', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17067;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17067, 'Gold Core', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17069;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17069, 'Shining Core', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17068;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17068, 'Shadowy Core', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17070;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17070, 'Spirited Core', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17071;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17071, 'Enchanted Core', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17072;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17072, 'Soultrapped Core', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17073;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17073, 'Cursed Core', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17074;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17074, 'Ethereal Core', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17075;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17075, 'Lirs Sand', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17076;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17076, 'Stonevale Sand', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17077;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17077, 'Cave Sand', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
DELETE FROM `item_templates` WHERE `item_id`=17078;
INSERT INTO `item_templates` (`item_id`, `item_name`, `stackable`, `armour`, `equipment_slot`, `buy_price`, `sell_price`, `weight`, `attack_speed`, `item_sub_type`, `no_trade`, `damage_list`, `bonus_list`, `requirement_list`, `class_requirement_list`, `skill_id`, `skill_level`, `attack_range`, `missile_speed`, `report_back_time_male`, `report_back_time_female`, `blocks_slots`, `proc_skill_id`, `proc_skill_level`, `proc_skill_chance`, `equip_skill_id`, `equip_skill_level`, `unique_id`, `bind_on_equip`, `stat_bonus`, `ability_bonus`, `skill_bonus`, `max_charges`, `destroy_on_no_charges`, `avoidance_bonuses`, `immunity_list`, `damage_reductions_list`) VALUES (17078, 'Otherworld Sand', b'1', 0, -1, 0, 0, 0, 0, 0, b'0', '', '', '', '', 0, 0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 0, b'0', '', '', '', 0, b'0', '', '', '');
```

Also replace the crafting items to the clientside `item_list.txt`
```
...
31|1|0|-1|0|0|61|1028|80|-1|0|76|||||1|0|81|-1|0|0|0|0|0|0|0|0|1|1|||||9999|0|-1|0|0|0|||
32|1|0|-1|0|0|61|1028|80|-1|0|76|||||1|0|81|-1|0|0|0|0|0|0|0|0|1|1|||||9999|0|-1|0|0|0|||
33|1|0|-1|0|0|61|1028|80|-1|0|76|||||1|0|83|-1|0|0|0|0|0|0|0|0|1|1|||||9999|0|-1|0|0|0|||
34|1|0|-1|0|0|61|1028|80|-1|0|76|||||1|0|83|-1|0|0|0|0|0|0|0|0|1|1|||||9999|0|-1|0|0|0|||
...
17017|0|0|-1|0|0|0|4117|10027|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17018|0|0|-1|0|0|0|4117|10048|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17019|0|0|-1|0|0|0|4117|10034|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17020|0|0|-1|0|0|0|4117|10041|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17021|0|0|-1|0|0|0|4117|10028|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17022|0|0|-1|0|0|0|4117|10049|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17023|0|0|-1|0|0|0|4117|10035|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17024|0|0|-1|0|0|0|4117|10042|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17025|0|0|-1|0|0|0|4117|10029|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17026|0|0|-1|0|0|0|4117|10050|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17027|0|0|-1|0|0|0|4117|10036|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17028|0|0|-1|0|0|0|4117|10043|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17029|0|0|-1|0|0|0|4117|10030|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17030|0|0|-1|0|0|0|4117|10051|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17031|0|0|-1|0|0|0|4117|10037|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17032|0|0|-1|0|0|0|4117|10044|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17033|0|0|-1|0|0|0|4117|10031|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17034|0|0|-1|0|0|0|4117|10052|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17035|0|0|-1|0|0|0|4117|10038|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17036|0|0|-1|0|0|0|4117|10045|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17037|0|0|-1|0|0|0|4117|10032|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17038|0|0|-1|0|0|0|4117|10053|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17039|0|0|-1|0|0|0|4117|10039|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17040|0|0|-1|0|0|0|4117|10046|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17041|0|0|-1|0|0|0|4117|10033|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17042|0|0|-1|0|0|0|4117|10054|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17043|0|0|-1|0|0|0|4117|10040|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17044|0|0|-1|0|0|0|76|10047|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17045|0|0|-1|0|0|0|76|10075|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17046|0|0|-1|0|0|0|76|10076|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17047|0|0|-1|0|0|0|76|10077|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17048|0|0|-1|0|0|0|76|10078|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17049|0|0|-1|0|0|0|76|10079|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17050|0|0|-1|0|0|0|76|10080|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17051|0|0|-1|0|0|0|76|10081|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17052|0|0|-1|0|0|0|76|10082|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17053|0|0|-1|0|0|0|76|10083|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17054|0|0|-1|0|0|0|76|10084|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17055|0|0|-1|0|0|0|76|10055|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17056|0|0|-1|0|0|0|76|10056|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17057|0|0|-1|0|0|0|76|10057|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17058|0|0|-1|0|0|0|76|10058|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17059|0|0|-1|0|0|0|76|10059|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17060|0|0|-1|0|0|0|76|10060|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17061|0|0|-1|0|0|0|76|10061|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17062|0|0|-1|0|0|0|76|10062|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17063|0|0|-1|0|0|0|76|10063|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17064|0|0|-1|0|0|0|76|10064|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17065|0|0|-1|0|0|0|76|10065|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17066|0|0|-1|0|0|0|76|10066|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17067|0|0|-1|0|0|0|76|10067|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17068|0|0|-1|0|0|0|76|10068|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17069|0|0|-1|0|0|0|76|10069|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17070|0|0|-1|0|0|0|76|10070|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17071|0|0|-1|0|0|0|76|10071|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17072|0|0|-1|0|0|0|76|10072|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17073|0|0|-1|0|0|0|76|10073|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17074|0|0|-1|0|0|0|76|10074|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17075|1|0|-1|0|0|0|76|7563|-1|0|221|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17076|1|0|-1|0|0|0|76|7565|-1|0|221|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17077|1|0|-1|0|0|0|76|7568|-1|0|221|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17078|1|0|-1|0|0|0|76|7566|-1|0|221|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17079|1|0|-1|0|0|0|76|10025|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|2|0|0|0|||
17080|1|0|-1|0|0|0|76|10025|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|3|0|0|0|||
17081|1|0|-1|0|0|0|76|10025|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|4|0|0|0|||
17082|1|0|-1|0|0|0|76|10025|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|5|0|0|0|||
17083|1|0|-1|0|0|0|76|10026|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|2|0|0|0|||
17084|1|0|-1|0|0|0|76|10026|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|3|0|0|0|||
17085|1|0|-1|0|0|0|76|10026|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|4|0|0|0|||
17086|1|0|-1|0|0|0|76|10026|-1|0|76|||||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|5|0|0|0|||
17087|0|2|6|1|0|5|500|106|-1|0|76||54^11^30;12^10|||0|0|0|0|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17088|0|3|4|1|0|5|1097|5529|-1|0|76||53^11^1000;12^20|||0|0|0|0|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17091|0|4|1|1|0|4|1188|244|-1|0|76||53^11^5;12^30|||0|0|0|0|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17092|0|5|3|1|0|5|1182|244|-1|0|76||12^40|||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
17093|0|6|2|1|0|5|1181|243|-1|0|76||12^50|||0|0|0|-1|0|0|0|0|0|0|0|0|0|0|||||9999|0|-1|0|0|0|||
...
```

Add the crafting icons to the client's `icon_list.txt`
```
...
10027,icon_crafting_mould_ring_common.png
10028,icon_crafting_mould_ring_enchanted.png
10029,icon_crafting_mould_ring_ancient.png
10030,icon_crafting_mould_ring_arcane.png
10031,icon_crafting_mould_ring_legendary.png
10032,icon_crafting_mould_ring_spirited.png
10033,icon_crafting_mould_ring_bonecursed.png
10034,icon_crafting_mould_necklace_common.png
10035,icon_crafting_mould_necklace_enchanted.png
10036,icon_crafting_mould_necklace_ancient.png
10037,icon_crafting_mould_necklace_arcane.png
10038,icon_crafting_mould_necklace_legendary.png
10039,icon_crafting_mould_necklace_spirited.png
10040,icon_crafting_mould_necklace_bonecursed.png
10041,icon_crafting_mould_charm_common.png
10042,icon_crafting_mould_charm_enchanted.png
10043,icon_crafting_mould_charm_ancient.png
10044,icon_crafting_mould_charm_arcane.png
10045,icon_crafting_mould_charm_legendary.png
10046,icon_crafting_mould_charm_spirited.png
10047,icon_crafting_mould_charm_bonecursed.png
10048,icon_crafting_mould_brace_common.png
10049,icon_crafting_mould_brace_enchanted.png
10050,icon_crafting_mould_brace_ancient.png
10051,icon_crafting_mould_brace_arcane.png
10052,icon_crafting_mould_brace_legendary.png
10053,icon_crafting_mould_brace_spirited.png
10054,icon_crafting_mould_brace_bonecursed.png
10055,icon_crafting_fastenings_iron.png
10056,icon_crafting_fastenings_silver.png
10057,icon_crafting_fastenings_gold.png
10058,icon_crafting_fastenings_shadowy.png
10059,icon_crafting_fastenings_shining.png
10060,icon_crafting_fastenings_spirited.png
10061,icon_crafting_fastenings_enchanted.png
10062,icon_crafting_fastenings_soultrapped.png
10063,icon_crafting_fastenings_cursed.png
10064,icon_crafting_fastenings_ethereal.png
10065,icon_crafting_core_iron.png
10066,icon_crafting_core_silver.png
10067,icon_crafting_core_gold.png
10068,icon_crafting_core_shadowy.png
10069,icon_crafting_core_shining.png
10070,icon_crafting_core_spirited.png
10071,icon_crafting_core_enchanted.png
10072,icon_crafting_core_soultrapped.png
10073,icon_crafting_core_cursed.png
10074,icon_crafting_core_ethereal.png
10075,icon_crafting_baubles_iron.png
10076,icon_crafting_baubles_silver.png
10077,icon_crafting_baubles_gold.png
10078,icon_crafting_baubles_shadowy.png
10079,icon_crafting_baubles_shining.png
10080,icon_crafting_baubles_spirited.png
10081,icon_crafting_baubles_enchanted.png
10082,icon_crafting_baubles_soultrapped.png
10083,icon_crafting_baubles_cursed.png
10084,icon_crafting_baubles_ethereal.png
```

### Adding the abilities

Add the mob to mob_list.txt, copy from Oven mob.

```
144,258,0.3,Workbench,0,0,1,-1,20,0,0.9,1.7,0,-5,2
...
228,258,0.3,Cauldron,0,0,1,-1,20,0,0.9,1.7,0,-5,2
...
922,258,0.3,Forge,0,0,1,-1,20,0,0.9,1.7,0,-5,2
```

Copy the cv_cooking_station_npc.txt conversation to cv_forging_station_npc.txt, change the content to be forging themed, use `FORGING` instead of `COOKING` and maybe remove the quest.
Add the conversation to the conversation_lookup.txt
Spawn the forge mob near blacksmith in castle.
Add abilities Forging:60, Craftmanship:61, Alchemy:62

To the SQL `abilities` database:
```
INSERT INTO abilities (ability_id, ability_name, base_chance, level_modifier, class_restriction) VALUES (60, 'Forging', 1, 1, 31);
INSERT INTO abilities (ability_id, ability_name, base_chance, level_modifier, class_restriction) VALUES (61, 'Craftsmanship', 1, 1, 31);
INSERT INTO abilities (ability_id, ability_name, base_chance, level_modifier, class_restriction) VALUES (62, 'Alchemy', 1, 1, 31);
```

To the clientside `ability_list.txt`
```
60,Forging
61,Craftsmanship
62,Alchemy
```

Add the forging abilities to the server CraftingType enum.

Patch the conversation_lookup.txt, mob_list.txt, conversation_lookup.txt, ability_list.txt.

### Adding recipes

To parse a CSV file from a spreadsheet, see `generate_recipes.py`.

To add recipes manually:

Add recipes to the `recipes` table in SQL, can overwrite some DNU ones, for example `71-86`. The below adds recipes for connacht armor
```
UPDATE recipes set recipe_name = "Vanquisher Gauntlets", difficulty = 1, failure_item_reward = 1, success_min_chance = 100, success_item_reward = 17608, critical_max_chance = 0, critical_item_reward = 1, master_max_chance = 0, master_item_reward = 1, cost_id = 910 WHERE recipe_id = 71;
UPDATE recipes set recipe_name = "Vanquisher Boots", difficulty = 1, failure_item_reward = 1, success_min_chance = 100, success_item_reward = 17609, critical_max_chance = 0, critical_item_reward = 1, master_max_chance = 0, master_item_reward = 1, cost_id = 911 WHERE recipe_id = 72;
UPDATE recipes set recipe_name = "Vanquisher Helm", difficulty = 1, failure_item_reward = 1, success_min_chance = 100, success_item_reward = 17610, critical_max_chance = 0, critical_item_reward = 1, master_max_chance = 0, master_item_reward = 1, cost_id = 912 WHERE recipe_id = 73;
UPDATE recipes set recipe_name = "Vanquisher Greaves", difficulty = 1, failure_item_reward = 1, success_min_chance = 100, success_item_reward = 17611, critical_max_chance = 0, critical_item_reward = 1, master_max_chance = 0, master_item_reward = 1, cost_id = 913 WHERE recipe_id = 74;
UPDATE recipes set recipe_name = "Vanquisher Breastplate", difficulty = 1, failure_item_reward = 1, success_min_chance = 100, success_item_reward = 17612, critical_max_chance = 0, critical_item_reward = 1, master_max_chance = 0, master_item_reward = 1, cost_id = 914 WHERE recipe_id = 75;
UPDATE recipes set recipe_name = "Pathfinder Bracers", difficulty = 1, failure_item_reward = 1, success_min_chance = 100, success_item_reward = 17613, critical_max_chance = 0, critical_item_reward = 1, master_max_chance = 0, master_item_reward = 1, cost_id = 915 WHERE recipe_id = 76;
UPDATE recipes set recipe_name = "Pathfinder Boots", difficulty = 1, failure_item_reward = 1, success_min_chance = 100, success_item_reward = 17614,critical_max_chance = 0, critical_item_reward = 1, master_max_chance = 0, master_item_reward = 1, cost_id = 916 WHERE recipe_id = 77;
UPDATE recipes set recipe_name = "Pathfinder Helm", difficulty = 1, failure_item_reward = 1, success_min_chance = 100, success_item_reward = 17615, critical_max_chance = 0, critical_item_reward = 1, master_max_chance = 0, master_item_reward = 1, cost_id = 917 WHERE recipe_id = 78;
UPDATE recipes set recipe_name = "Pathfiner Breeches", difficulty = 1, failure_item_reward = 1, success_min_chance = 100, success_item_reward = 17616, critical_max_chance = 0, critical_item_reward = 1, master_max_chance = 0, master_item_reward = 1, cost_id = 918 WHERE recipe_id = 79;
UPDATE recipes set recipe_name = "Pathfinder Cuirass", difficulty = 1, failure_item_reward = 1, success_min_chance = 100, success_item_reward = 17617, critical_max_chance = 0, critical_item_reward = 1, master_max_chance = 0, master_item_reward = 1, cost_id = 919 WHERE recipe_id = 80;
UPDATE recipes set recipe_name = "Magus Gloves", difficulty = 1, failure_item_reward = 1, success_min_chance = 100, success_item_reward = 17618, critical_max_chance = 0, critical_item_reward = 1, master_max_chance = 0, master_item_reward = 1, cost_id = 920 WHERE recipe_id = 81;
UPDATE recipes set recipe_name = "Magus Shoes", difficulty = 1, failure_item_reward = 1, success_min_chance = 100, success_item_reward = 17619, critical_max_chance = 0, critical_item_reward = 1, master_max_chance = 0, master_item_reward = 1, cost_id = 921 WHERE recipe_id = 82;
UPDATE recipes set recipe_name = "Magus Helm", difficulty = 1, failure_item_reward = 1, success_min_chance = 100, success_item_reward = 17620, critical_max_chance = 0, critical_item_reward = 1, master_max_chance = 0, master_item_reward = 1, cost_id = 922 WHERE recipe_id = 83;
UPDATE recipes set recipe_name = "Magus Skirt", difficulty = 1, failure_item_reward = 1, success_min_chance = 100, success_item_reward = 17621, critical_max_chance = 0, critical_item_reward = 1, master_max_chance = 0, master_item_reward = 1, cost_id = 923 WHERE recipe_id = 84;
UPDATE recipes set recipe_name = "Magus Robe", difficulty = 1, failure_item_reward = 1, success_min_chance = 100, success_item_reward = 17622, critical_max_chance = 0, critical_item_reward = 1, master_max_chance = 0, master_item_reward = 1, cost_id = 924 WHERE recipe_id = 85;
UPDATE recipes set recipe_name = "Vanquisher Shield", difficulty = 1, failure_item_reward = 1, success_min_chance = 100, success_item_reward = 17623, critical_max_chance = 0, critical_item_reward = 1, master_max_chance = 0, master_item_reward = 1, cost_id = 925 WHERE recipe_id = 86;
```
Update the recipe cost in the `token_vendor_costs` SQL table, for example:
```
# remove the existing costs
DELETE FROM token_vendor_cost WHERE (token_vendor_cost_id >= 910 AND token_vendor_cost_id <= 925);
# add the costs
# connacht gloves: 10 armor, 1 weapon
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (910, 16679, 10);
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (910, 17291, 1);  # connacht sword
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (915, 16679, 10);
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (915, 17289, 1);  # connacht bow
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (920, 16679, 10);
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (920, 17293, 1);  # connacht wand
# connacht boots: 5 armor, 5 chainmail, 1 weapon
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (911, 16679, 5);
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (911, 16682, 5);
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (911, 17291, 1);  # connacht sword
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (916, 16679, 5);
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (916, 16682, 5);
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (916, 17289, 1);  # connacht bow
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (921, 16679, 5);
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (921, 16682, 5);
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (921, 17293, 1);  # connacht wand
# connacht helm: 10 chainmail, 1 weapon
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (912, 16682, 10);
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (912, 17291, 1);  # connacht sword
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (917, 16682, 10);
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (917, 17289, 1);  # connacht bow
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (922, 16682, 10);
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (922, 17293, 1);  # connacht wand
# connacht greaves: 5 chainmail, 5 tunic, 1 weapon
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (913, 16682, 5);
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (913, 16678, 5);
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (913, 17291, 1);  # connacht sword
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (918, 16682, 5);
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (918, 16678, 5);
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (918, 17289, 1);  # connacht bow
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (923, 16682, 5);
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (923, 16678, 5);
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (923, 17293, 1);  # connacht wand
# connacht chestpiece: 10 tunic, 1 weapon
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (914, 16678, 10);
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (914, 17291, 1);  # connacht sword
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (919, 16678, 10);
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (919, 17289, 1);  # connacht bow
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (924, 16678, 10);
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (924, 17293, 1);  # connacht wand
# connacht shield: 10 armor, 10 chainmail
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (925, 16679, 10);
INSERT INTO token_vendor_cost (token_vendor_cost_id, item_template_id, quantity) VALUES (925, 16682, 10);
# INSERT more costs here
```
Add the items to the `token_vendor_stock` SQL table:
```
DELETE FROM token_vendor_stock WHERE (token_vendor_cost_id >= 910 AND token_vendor_cost_id <= 925);
# connacht armor/shield
INSERT INTO token_vendor_stock (token_vendor_id, item_template_id, token_vendor_cost_id) VALUES (486, 17608, 910);
INSERT INTO token_vendor_stock (token_vendor_id, item_template_id, token_vendor_cost_id) VALUES (486, 17609, 911);
INSERT INTO token_vendor_stock (token_vendor_id, item_template_id, token_vendor_cost_id) VALUES (487, 17610, 912);
INSERT INTO token_vendor_stock (token_vendor_id, item_template_id, token_vendor_cost_id) VALUES (487, 17611, 913);
INSERT INTO token_vendor_stock (token_vendor_id, item_template_id, token_vendor_cost_id) VALUES (488, 17612, 914);
INSERT INTO token_vendor_stock (token_vendor_id, item_template_id, token_vendor_cost_id) VALUES (488, 17613, 915);
INSERT INTO token_vendor_stock (token_vendor_id, item_template_id, token_vendor_cost_id) VALUES (489, 17614, 916);
INSERT INTO token_vendor_stock (token_vendor_id, item_template_id, token_vendor_cost_id) VALUES (489, 17615, 917);
INSERT INTO token_vendor_stock (token_vendor_id, item_template_id, token_vendor_cost_id) VALUES (490, 17616, 918);
INSERT INTO token_vendor_stock (token_vendor_id, item_template_id, token_vendor_cost_id) VALUES (490, 17617, 919);
INSERT INTO token_vendor_stock (token_vendor_id, item_template_id, token_vendor_cost_id) VALUES (491, 17618, 920);
INSERT INTO token_vendor_stock (token_vendor_id, item_template_id, token_vendor_cost_id) VALUES (491, 17619, 921);
INSERT INTO token_vendor_stock (token_vendor_id, item_template_id, token_vendor_cost_id) VALUES (221, 17620, 922);
INSERT INTO token_vendor_stock (token_vendor_id, item_template_id, token_vendor_cost_id) VALUES (221, 17621, 923);
INSERT INTO token_vendor_stock (token_vendor_id, item_template_id, token_vendor_cost_id) VALUES (221, 17622, 924);
INSERT INTO token_vendor_stock (token_vendor_id, item_template_id, token_vendor_cost_id) VALUES (221, 17623, 925);

```
Add the recipes to the clientside `recipes.txt`, note that the recipe rewards are sent by the server so they do not matter in this file. The name is what shows up when cooking the recipe.
```
Vanquisher Gauntlets,100,100,0,20,0,2,0,50,20,70,60580,60650,60720,60790,9,71,910,61253,2
Vanquisher Boots,100,100,1,20,0,2,0,50,20,70,60581,60581,17612,17612,9,72,911,61253,2
Vanquisher Helm,60,100,1,20,0,2,0,50,20,70,60581,60651,60721,60791,9,73,912,61253,1
Vanquisher Greaves,50,100,1,20,0,2,0,100,25,150,60582,60652,60722,60792,9,74,913,61253,1
Vanquisher Breastplate,50,100,1,20,0,2,0,150,30,250,60583,60653,60723,60793,9,75,914,61253,1
Pathfinder Bracers,50,100,1,20,0,2,0,200,35,350,60584,60654,60724,60794,9,76,915,61253,1
Pathfinder Boots,50,100,1,20,0,2,0,250,40,450,60585,60655,60725,60795,9,77,916,61253,1
Pathfinder Helm,50,100,1,20,0,2,100,300,50,650,60586,60656,60726,60796,9,78,917,61253,1
Pathfinder Breeches,50,100,1,20,0,2,200,300,60,850,60587,60657,60727,60797,9,79,918,61253,1
Pathfinder Cuirass,50,100,1,20,0,2,300,300,70,1050,60588,60658,60728,60798,9,80,919,61254,1
Magus Gloves,50,100,1,20,0,2,400,300,80,1250,60589,60659,60729,60799,9,81,920,61254,1
Magus Shoes,50,100,1,20,0,2,500,300,90,1450,60590,60660,60730,60800,9,82,921,61254,1
Magus Helm,50,100,1,20,0,2,600,300,100,1650,60591,60661,60731,60801,9,83,922,61254,1
Magus Skirt,50,100,1,20,0,2,700,300,110,1850,60592,60662,60732,60802,9,84,923,61255,1
Magus Robe,50,100,1,20,0,2,800,300,120,2050,60593,60663,60733,60803,9,85,924,61255,1
Vanquisher Shield,50,100,1,20,0,2,900,300,130,2250,60594,60664,60734,60804,9,86,925,61255,1
```

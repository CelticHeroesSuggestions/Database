## Crafting

Possible steps to make crafting:

### Adding the vendors

Create the Forge, Crafting Table, and Cauldron mobs, can use IDs 922, 144, and 228. Copy from the Oven mob:
```
# Forging, replace ID 922
DELETE FROM `mob_templates` WHERE `mob_template_id`=922;
INSERT INTO `mob_templates` (`mob_template_id`, `mob_name`, `aggro_range`, `follow_range`, `faction_id`, `opinion_base`, `level`, `hitpoints`, `sloot_table`, `min_coins`, `max_coins`, `kills_per_level`, `conversation_id`, `attack`, `defence`, `attack_speed`, `energy`, `skill_list`, `radius`, `armour_value`, `model_scale`, `damage_list`, `resistance_list`, `mob_power`, `max_attack_range`, `mob_race`, `missile_speed`, `report_back_time`, `ai_template_id`, `xp`, `num_drops`, `perm_status_effects`, `blocks_attacks`, `avoidance_ratings`, `spot_hidden`, `immunity_list`, `damage_reductions_list`, `no_ability_test`, `mob_type`) VALUES (922, 'Forge', 0, 0, 3, 51, 0, 200, '', 0, 0, NULL, 737, 0, 0, 0, 0, '', 0.3, 5, 4, '', '', 0, 1, 20, 0, 0, 0, 0, 1, '', b'0', '', 0, '', '', b'0', 0);

# Crafting, replace ID 144
DELETE FROM `mob_templates` WHERE `mob_template_id`=144;
INSERT INTO `mob_templates` (`mob_template_id`, `mob_name`, `aggro_range`, `follow_range`, `faction_id`, `opinion_base`, `level`, `hitpoints`, `loot_table`, `min_coins`, `max_coins`, `kills_per_level`, `conversation_id`, `attack`, `defence`, `attack_speed`, `energy`, `skill_list`, `radius`, `armour_value`, `model_scale`, `damage_list`, `resistance_list`, `mob_power`, `max_attack_range`, `mob_race`, `missile_speed`, `report_back_time`, `ai_template_id`, `xp`, `num_drops`, `perm_status_effects`, `blocks_attacks`, `avoidance_ratings`, `spot_hidden`, `immunity_list`, `damage_reductions_list`, `no_ability_test`, `mob_type`) VALUES (144, 'Workbench', 0, 0, 3, 51, 0, 200, '', 0, 0, NULL, 737, 0, 0, 0, 0, '', 0.3, 5, 4, '', '', 0, 1, 20, 0, 0, 0, 0, 1, '', b'0', '', 0, '', '', b'0', 0);

# Alchemy, replace ID 228
DELETE FROM `mob_templates` WHERE `mob_template_id`=228;
INSERT INTO `mob_templates` (`mob_template_id`, `mob_name`, `aggro_range`, `follow_range`, `faction_id`, `opinion_base`, `level`, `hitpoints`, `loot_table`, `min_coins`, `max_coins`, `kills_per_level`, `conversation_id`, `attack`, `defence`, `attack_speed`, `energy`, `skill_list`, `radius`, `armour_value`, `model_scale`, `damage_list`, `resistance_list`, `mob_power`, `max_attack_range`, `mob_race`, `missile_speed`, `report_back_time`, `ai_template_id`, `xp`, `num_drops`, `perm_status_effects`, `blocks_attacks`, `avoidance_ratings`, `spot_hidden`, `immunity_list`, `damage_reductions_list`, `no_ability_test`, `mob_type`) VALUES (228, 'Cauldron', 0, 0, 3, 51, 0, 200, '', 0, 0, NULL, 737, 0, 0, 0, 0, '', 0.3, 5, 4, '', '', 0, 1, 20, 0, 0, 0, 0, 1, '', b'0', '', 0, '', '', b'0', 0);
```

Spawn the mobs:
```
# Forge Farcrag
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20500;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20500, 93, 15, 5.22, -111, 122, 'stand', '922,1', 1, 0, 20, 0, 0, 0);
# Forge Shalemont
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20501;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20501, 6, 15, 53, 0, 6.75, 'stand', '922,1', 1, 0, 20, 0, 0, 0);
# Forge Stonevale
DELETE FROM `spawn_points` WHERE `spawn_point_id`=20502;
INSERT INTO `spawn_points` (`spawn_point_id`, `zone_id`, `respawn_time`, `position_x`, `position_y`, `position_z`, `patrol`, `monster_list`, `patrol_speed`, `init_y_angle`, `max_respawn_time`, `min_despawn_time`, `max_despawn_time`, `despawn`) VALUES (20502, 3, 15, 30.93, 0, -19.38, 'stand', '922,1', 1, 0, 20, 0, 0, 0);

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

### Adding the abilities

Add the mob to mob_list.txt, copy from Oven mob.
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

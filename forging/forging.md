## Forging

Possible steps to make forging:

1. Rename mob ID 922 to Forge, copy everything from the Oven mob but change conversation ID to 737.
2. Add the mob to mob_list.txt, copy from Oven mob.
3. Copy the cv_cooking_station_npc.txt conversation to cv_forging_station_npc.txt, change the content to be forging themed, use `FORGING` instead of `COOKING` and maybe remove the quest.
4. Add the conversation to the conversation_lookup.txt
5. Spawn the forge mob near blacksmith in castle.
6. Add abilities Forging:60, Craftmanship:61, Alchemy:62

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

7. Add the forging abilities to the server CraftingType enum
8. Patch the conversation_lookup.txt, mob_list.txt, conversation_lookup.txt, ability_list.txt
9. Add recipes to the SQL, can overwrite some DNU ones
```
UPDATE recipes set recipe_name = "Connacht Vanquisher Breastplate", difficulty = 1, failure_item_reward = 17612, success_item_reward = 17612, critical_item_reward = 17612, master_item_reward = 17612, cost_id = 910 WHERE recipe_id = 71;
```
10. Update the recipe cost in the `token_vendor_costs` SQL table
11. Add the recipe to the clientside `recipes.txt`
10. Enjoy!

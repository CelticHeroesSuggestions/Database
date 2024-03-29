# Druid Balancing: Skill and Gear Changes

* What: Update druid skills and gear to fix minor issues
* Why: Druids have some questionable gear and skills, that would be easy to update for immediate improvements.
* Notes: This does not include a comprehensive staff redo, which is sorely needed. My idea for staffs is to make them superior to druid totem/offhands for casters (so totem have a place for melee-assisted DPS), giving regen/stats/skill points.
* Changes:
```
# allow Druids to use Lure of Magic tome
UPDATE ch_live_unitydatadb.item_templates SET class_requirement_list = '2,3' WHERE item_id = 17968;
# allow Druids to use Energy Boost tome
UPDATE ch_live_unitydatadb.item_templates SET class_requirement_list = '2,3' WHERE item_id = 1056;

# add Energy Boost tome to druid skill shop
INSERT INTO ch_live_unitydatadb.shop_stock (shop_id, zone_id, item_id, stock_level, sort_order)
VALUES (6, 93, 1056, -1, 1);

# increase duration of Nature's Embrace
UPDATE ch_live_unitydatadb.status_effect_levels SET duration = 300 WHERE status_effect_template_id = 15;
# increase duration of Shield of Bark
UPDATE ch_live_unitydatadb.status_effect_levels SET duration = 600 WHERE status_effect_template_id = 14;
# increase duration of Bless
UPDATE ch_live_unitydatadb.status_effect_levels SET duration = 600 WHERE status_effect_template_id = 140;
# increase duration of Abundance
UPDATE ch_live_unitydatadb.status_effect_levels SET duration = 600 WHERE status_effect_template_id = 13;
```

Update the spell tomes in `item_list.txt`
```
...
1056|0|0|-1|0|0|61|16191|7868|-1|0|76||||3;4|1|0|1056|-1|0|0|0|0|0|0|0|0|1|1|||||9999|0|-1|0|0|0|||
...
17968|0|0|-1|0|0|61|16175|7852|-1|0|76||||3;4|1|0|1137|-1|0|0|0|0|0|0|0|0|1|1|||||9999|0|-1|0|0|0|||
...
```

Update Strangling Vine's skill effect in `status_effects_list.txt`
```
...
3^100^Strangling Vines^8^You are surrounded by constricting vines that crush the life out of you, causing damage for 30 seconds.^3
0,2.1,60,3,0
0,2.1,60,3,1
1,3.4,60,5,0
1,3.4,60,5,1
2,4.9,60,7,0
2,4.9,60,7,1
3,6.4,60,9,0
3,6.4,60,9,1
4,8.1,60,11,0
4,8.1,60,11,1
5,9.7,60,13,0
5,9.7,60,13,1
6,11.5,60,15,0
6,11.5,60,15,1
7,13.3,60,17,0
7,13.3,60,17,1
8,15.2,60,19,0
8,15.2,60,19,1
9,17.2,60,21,0
9,17.2,60,21,1
10,19.3,60,23,0
10,19.3,60,23,1
11,21.4,60,25,0
11,21.4,60,25,1
12,23.6,60,27,0
12,23.6,60,27,1
13,25.9,60,29,0
13,25.9,60,29,1
14,28.3,60,31,0
14,28.3,60,31,1
15,60.7,60,33,0
15,60.7,60,33,1
16,33.2,60,35,0
16,33.2,60,35,1
17,35.8,60,37,0
17,35.8,60,37,1
18,38.5,60,39,0
18,38.5,60,39,1
19,41.2,60,41,0
19,41.2,60,41,1
20,44,60,43,0
20,44,60,43,1
21,46.9,60,45,0
21,46.9,60,45,1
22,49.9,60,47,0
22,49.9,60,47,1
23,52.9,60,49,0
23,52.9,60,49,1
24,56,60,51,0
24,56,60,51,1
25,59.2,60,53,0
25,59.2,60,53,1
26,62.4,60,55,0
26,62.4,60,55,1
27,65.8,60,57,0
27,65.8,60,57,1
28,69.2,60,59,0
28,69.2,60,59,1
29,72.7,60,61,0
29,72.7,60,61,1
30,76.2,60,63,0
30,76.2,60,63,1
31,79.9,60,65,0
31,79.9,60,65,1
32,83.6,60,67,0
32,83.6,60,67,1
33,87.4,60,69,0
33,87.4,60,69,1
34,91.2,60,71,0
34,91.2,60,71,1
35,95.2,60,73,0
35,95.2,60,73,1
36,99.2,60,75,0
36,99.2,60,75,1
37,103.3,60,77,0
37,103.3,60,77,1
38,107.4,60,79,0
38,107.4,60,79,1
39,111.7,60,81,0
39,111.7,60,81,1
40,116,60,83,0
40,116,60,83,1
41,120.3,60,85,0
41,120.3,60,85,1
42,124.8,60,87,0
42,124.8,60,87,1
43,129.3,60,89,0
43,129.3,60,89,1
44,134,60,91,0
44,134,60,91,1
45,138.6,60,93,0
45,138.6,60,93,1
46,143.4,60,95,0
46,143.4,60,95,1
47,148.2,60,97,0
47,148.2,60,97,1
48,153.1,60,99,0
48,153.1,60,99,1
49,158.1,60,101,0
49,158.1,60,101,1
...
141^100^Stinging Swarm^128^You are being targeted by a swarm of stinging insects, dealing damage over time.^3
0,2,60,2,0
0,2,60,2,1
1,2.6,60,5,0
1,2.6,60,5,1
2,3.2,60,8,0
2,3.2,60,8,1
3,3.8,60,11,0
3,3.8,60,11,1
4,4.4,60,14,0
4,4.4,60,14,1
5,5,60,17,0
5,5,60,17,1
6,5.7,60,60,0
6,5.7,60,60,1
7,6.4,60,23,0
7,6.4,60,23,1
8,7.1,60,26,0
8,7.1,60,26,1
9,7.8,60,29,0
9,7.8,60,29,1
10,8.5,60,32,0
10,8.5,60,32,1
11,9.3,60,35,0
11,9.3,60,35,1
12,10.1,60,38,0
12,10.1,60,38,1
13,10.9,60,41,0
13,10.9,60,41,1
14,11.7,60,44,0
14,11.7,60,44,1
15,12.5,60,47,0
15,12.5,60,47,1
16,13.4,60,50,0
16,13.4,60,50,1
17,14.3,60,53,0
17,14.3,60,53,1
18,15.2,60,56,0
18,15.2,60,56,1
19,16.1,60,59,0
19,16.1,60,59,1
20,17,60,62,0
20,17,60,62,1
21,18,60,65,0
21,18,60,65,1
22,19,60,68,0
22,19,60,68,1
23,60,60,71,0
23,60,60,71,1
24,21,60,74,0
24,21,60,74,1
25,22,60,77,0
25,22,60,77,1
26,23.1,60,80,0
26,23.1,60,80,1
27,24.2,60,83,0
27,24.2,60,83,1
28,25.3,60,86,0
28,25.3,60,86,1
29,26.4,60,89,0
29,26.4,60,89,1
30,27.5,60,92,0
30,27.5,60,92,1
31,28.7,60,95,0
31,28.7,60,95,1
32,29.9,60,98,0
32,29.9,60,98,1
33,31.1,60,101,0
33,31.1,60,101,1
34,32.3,60,104,0
34,32.3,60,104,1
35,33.5,60,107,0
35,33.5,60,107,1
36,34.8,60,110,0
36,34.8,60,110,1
37,36.1,60,113,0
37,36.1,60,113,1
38,37.4,60,116,0
38,37.4,60,116,1
39,38.7,60,119,0
39,38.7,60,119,1
40,40,60,122,0
40,40,60,122,1
41,41.4,60,125,0
41,41.4,60,125,1
42,42.8,60,128,0
42,42.8,60,128,1
43,44.2,60,131,0
43,44.2,60,131,1
44,45.6,60,134,0
44,45.6,60,134,1
45,47,60,137,0
45,47,60,137,1
46,48.5,60,140,0
46,48.5,60,140,1
47,50,60,143,0
47,50,60,143,1
48,51.5,60,146,0
48,51.5,60,146,1
49,53,60,149,0
49,53,60,149,1
...
```

Update `text.db`
```
UPDATE item_templates SET item_name = 'Mighty Bloodfang Helm of Rejuvenation' WHERE item_id = 63590;
UPDATE item_templates SET item_name = 'Majestic Bloodfang Helm of Rejuvenation' WHERE item_id = 63591;
UPDATE item_templates SET item_name = 'Royal Bloodfang Helm of Rejuvenation' WHERE item_id = 63592;
UPDATE item_templates SET item_name = 'Imperial Bloodfang Helm of Rejuvenation' WHERE item_id = 63593;
UPDATE item_templates SET item_name = 'Godly Bloodfang Helm of Rejuvenation' WHERE item_id = 63594;

UPDATE item_templates SET item_description = "The culmination of Dian Cecht's knowledge on harnessing the Storm. This has been passed to those few worthy Druid within the Wardens over time. +400 to Storm Touch, +200 to Lightning Strike, and +500 to Aetheric Renewal." WHERE item_id = 64765;
UPDATE item_templates SET item_description = "The culmination of Dian Cecht's knowledge on harnessing the Storm. This has been passed to those few worthy Druid within the Wardens over time. +450 to Storm Touch, +225 to Lightning Strike, and +750 to Aetheric Renewal." WHERE item_id = 64766;
UPDATE item_templates SET item_description = "The culmination of Dian Cecht's knowledge on harnessing the Storm. This has been passed to those few worthy Druid within the Wardens over time. +500 to Storm Touch, +250 to Lightning Strike, and +1000 to Aetheric Renewal." WHERE item_id = 64767;
```

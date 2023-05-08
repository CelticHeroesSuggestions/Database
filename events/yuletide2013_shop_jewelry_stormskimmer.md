# Yuletide 2013: Luxury Shop

* What: Spawn points for the Yuletide 2013 seasonal shop
* Why: Old luxury shops are always a welcome season addition.
* Notes: I placed the NPC near the Farcrag Fountain.
* Changes:
```
# Braith the Explorer (Stormskimmer)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13540, 93, 1, -6.11, 0, -0.88, "stand", "805,1", 1, 190, 2, 0, 0, 0);

# this mob's conversation was removed from the game, so you will need to patch in Database/events/conversation/cv_winter_2013_lux_vendor.xml

# add the conversation to conversation_lookup.txt, I will use the ID 1003 (which shouldn't conflict with anything else)

# update the NPC's conversation
UPDATE ch_live_unitydatadb.mob_templates SET conversation_id = 1003 WHERE mob_template_id = 805;
```

# Yuletide 2013: Luxury Shop

* What: Spawn points for the Yuletide 2013 seasonal shop
* Why: Old luxury shops are always a welcome season addition.
* Notes: I placed the NPC near the Farcrag Fountain.
* Changes:
```
# Braith the Explorer (Stormskimmer)
INSERT INTO ch_live_unitydatadb.spawn_points (spawn_point_id, zone_id, respawn_time, position_x, position_y, position_z, patrol, monster_list, patrol_speed, init_y_angle, max_respawn_time, min_despawn_time, max_despawn_time, despawn)
VALUES (13540, 93, 1, -6.11, 0, -0.88, "stand", "805,1", 1, 190, 2, 0, 0, 0);

# update the conversation to the new dialogue we will make
UPDATE ch_live_unitydatadb.mob_templates SET conversation_id = 1003 WHERE mob_template_id = 805;

# create the AssetBundles and update the patchManifest.txt to include the new files
TextAsset_cv_leif_yuletide2013_braith
TextAsset_conversation_lookup.unity3d
```

Create a new dialogue for Braith: `cv_leif_yuletide2013_braith.txt`
```
<xml>
<line>
<lineTag>OPEN_SHOP</lineTag>
<lineText>Hail! I am the renowned [00CC00]]Braith the Explorer[-]! This year I traveled across the lands of trolls and dragons, and have returned with exquisite luxuries to trade. Perhaps something will catch your eye?</lineText>
<choice>
<choiceOptions>[S]</choiceOptions>
<choiceText>Show me your wares.</choiceText>
<choiceAction>SHOP 12001</choiceAction>
<choiceGoto>OPEN_SHOP</choiceGoto>
</choice>

<choice>
<choiceOptions>[X]</choiceOptions>
<choiceText>No thank you.</choiceText>
<choiceAction> </choiceAction>
<choiceGoto>-1</choiceGoto>
</choice>
</line>

</xml>
```

Add the dialogue to `conversation_lookup.txt`
```
...
conv 1003 cv_leif_yuletide2013_braith
END_FILE
```

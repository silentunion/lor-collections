INSERT INTO namegen.cluster (cluster)
    SELECT {cluster}
    WHERE NOT EXISTS (SELECT cluster FROM namegen.cluster WHERE cluster = {cluster});

-- If value doesn't exist at all,
    -- insert it with new part id
-- If value does exist,
    -- check if already the type requested, If type does exist
            -- do nothing
    -- If type doesn't exist
            -- get the part_id from the existing type and add the part to the requested type
DO $$
BEGIN 
	IF NOT EXISTS 
        (SELECT letter, cluster, syllable, stem, name
        FROM namegen.parts
        FULL JOIN namegen.letters USING(part_id)
        FULL JOIN namegen.clusters USING(part_id)
        FULL JOIN namegen.syllables USING(part_id)
        FULL JOIN namegen.stems USING(part_id)
        FULL JOIN namegen.names USING(part_id)
        WHERE letter ='${new_part}'
           OR cluster ='${new_part}'
           OR syllable ='${new_part}'
           OR stem ='${new_part}'
           OR name ='${new_part}')
    THEN
		INSERT INTO namegen.parts (part_id) VALUES DEFAULT
        INSERT INTO namegen.'${part_table}' (part_id, '${part_column}')
            VALUES((SELECT MAX(part_id) FROM namegen.parts), '${new_part}')
    ELSE
    IF NOT EXISTS
        (SELECT '${part_column}'
         FROM namegen.'${part_table}'
         WHERE '${part_column}'='${new_part}')
    THEN
        INSERT INTO namegen.'${part_table}' (part_id, '${part_column}')
            VALUES((SELECT part_id FROM namegen.parts
                    JOIN namegen.letters USING(part_id)
                    JOIN namegen.clusters USING(part_id)
                    JOIN namegen.syllables USING(part_id)
                    JOIN namegen.stems USING(part_id)
                    JOIN namegen.names USING(part_id)
                    WHERE letter ='${new_part}'
                        OR cluster ='${new_part}'
                        OR syllable ='${new_part}'
                        OR stem ='${new_part}'
                        OR name ='${new_part}'), '${new_part}')
	END IF;
END $$


-- Template Collection Insert (Testing and Working) --
INSERT INTO namegen.languages (language)
    SELECT '{language}'
    WHERE NOT EXISTS (
        SELECT 1 FROM namegen.languages WHERE language='{language}'
    );

INSERT INTO namegen.themes (theme)
    SELECT '{theme}'
    WHERE NOT EXISTS (
        SELECT 1 FROM namegen.themes WHERE theme='{theme}'
    );

INSERT INTO namegen.collections (lang_id, theme_id, collection)
    SELECT (SELECT lang_id FROM namegen.languages WHERE language='{language}'),
           (SELECT theme_id FROM namegen.themes WHERE theme='{theme}'),
           '{collection}'
    WHERE NOT EXISTS (
        SELECT 1 FROM namegen.collections WHERE collection='{collection}'
    );

INSERT INTO namegen.categories (category)
    VALUES ('letters'),
           ('clusters'),
           ('syllables'),
           ('stems'),
           ('names');
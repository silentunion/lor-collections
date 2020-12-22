

CREATE OR REPLACE FUNCTION insert_part(_new_part VARCHAR, _part_column VARCHAR, _part_table VARCHAR)
RETURNS void AS
$BODY$
BEGIN 
    WITH get_parts as (
        SELECT *
        FROM namegen.parts
        FULL JOIN namegen.part_letters USING(part_id)
        FULL JOIN namegen.part_clusters USING(part_id)
        FULL JOIN namegen.part_syllables USING(part_id)
        FULL JOIN namegen.part_stems USING(part_id)
        FULL JOIN namegen.part_names USING(part_id)
        WHERE letter = _new_part
           OR cluster = _new_part
           OR syllable = _new_part
           OR stem = _new_part
           OR name = _new_part
        RETURNING *)
	IF NOT EXISTS 
        (SELECT * FROM get_parts)
    THEN
        WITH new_part_id AS (
            INSERT INTO namegen.parts (part_id) VALUES (DEFAULT)
            RETURNING part_id
        )
        INSERT INTO namegen._part_table (part_id, _part_column)
            VALUES((SELECT part_id FROM new_part_id), _new_part);
    ELSIF NOT EXISTS
        (SELECT _part_column
         FROM namegen._part_table
         WHERE _part_column = _new_part)
    THEN
        INSERT INTO namegen._part_table (part_id, _part_column)
            VALUES((SELECT part_id FROM get_parts), _new_part);
	END IF
END;
$BODY$ LANGUAGE 'plpgsql';
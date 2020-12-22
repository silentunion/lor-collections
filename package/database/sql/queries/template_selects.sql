SELECT letter, frequency, is_vowel
FROM namegen.parts
JOIN namegen.letters USING(part_id)
JOIN namegen.languages_parts USING(part_id)
JOIN namegen.languages USING(lang_id)
WHERE language='English Basic';


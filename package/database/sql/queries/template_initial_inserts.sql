-- Initial inserts used to create 'Test' and 'None' values with id 0 and 1
INSERT INTO namegen.languages (lang_id, language)
    SELECT 0, 'TEST LANGUAGE'
    WHERE NOT EXISTS (
        SELECT 1 FROM namegen.languages WHERE language='TEST LANGUAGE'
    );

INSERT INTO namegen.languages (language)
    SELECT 'None'
    WHERE NOT EXISTS (
        SELECT 1 FROM namegen.languages WHERE language='None'
    );

INSERT INTO namegen.languages (language)
    SELECT 'English Basic'
    WHERE NOT EXISTS (
        SELECT 1 FROM namegen.languages WHERE language='English Basic'
    );

INSERT INTO namegen.themes (theme_id, theme)
    SELECT 0, 'TEST THEME'
    WHERE NOT EXISTS (
        SELECT 1 FROM namegen.themes WHERE theme='TEST THEME'
    );

INSERT INTO namegen.themes (theme)
    SELECT 'None'
    WHERE NOT EXISTS (
        SELECT 1 FROM namegen.themes WHERE theme='None'
    );

INSERT INTO namegen.collections (col_id, lang_id, theme_id, collection)
    SELECT 0, 0, 0, 'TEST COLLECTION'
    WHERE NOT EXISTS (
        SELECT 1 FROM namegen.collections WHERE collection='TEST COLLECTION'
    );

INSERT INTO namegen.collections (lang_id, theme_id, collection)
    SELECT 1, 1, 'None'
    WHERE NOT EXISTS (
        SELECT 1 FROM namegen.collections WHERE collection='None'
    );

INSERT INTO namegen.properties (property)
    SELECT 'is_vowel'
    WHERE NOT EXISTS (
        SELECT 1 FROM namegen.properties WHERE property='is_vowel'
    );
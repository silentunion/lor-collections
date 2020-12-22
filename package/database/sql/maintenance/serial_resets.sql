-- Table: PARTS --
SELECT setval('namegen.parts_part_id_seq',
              (SELECT CASE WHEN (SELECT MAX(part_id) FROM namegen.parts) IS NULL
               THEN 1
               ELSE (SELECT MAX(part_id) FROM namegen.parts) + 1
               END), FALSE);

-- Table: LANGUAGES --
SELECT setval('namegen.languages_lang_id_seq',
              (SELECT CASE WHEN (SELECT MAX(lang_id) FROM namegen.languages) IS NULL
               THEN 1
               ELSE (SELECT MAX(lang_id) FROM namegen.languages) + 1
               END), FALSE);

-- Table: THEMES --
SELECT setval('namegen.themes_theme_id_seq',
              (SELECT CASE WHEN (SELECT MAX(theme_id) FROM namegen.themes) IS NULL
               THEN 1
               ELSE (SELECT MAX(theme_id) FROM namegen.themes) + 1
               END), FALSE);

-- Table: COLLECTIONS --
SELECT setval('namegen.collections_col_id_seq',
              (SELECT CASE WHEN (SELECT MAX(col_id) FROM namegen.collections) IS NULL
               THEN 1
               ELSE (SELECT MAX(col_id) FROM namegen.collections) + 1
               END), FALSE);

-- Table: PROPERTIES --
SELECT setval('namegen.properties_prop_id_seq',
              (SELECT CASE WHEN (SELECT MAX(prop_id) FROM namegen.properties) IS NULL
               THEN 1
               ELSE (SELECT MAX(prop_id) FROM namegen.properties) + 1
               END), FALSE);

-- Table: COLLECTION_PARTS --
SELECT setval('namegen.collection_parts_cp_id_seq',
              (SELECT CASE WHEN (SELECT MAX(cp_id) FROM namegen.collection_parts) IS NULL
               THEN 1
               ELSE (SELECT MAX(cp_id) FROM namegen.collection_parts) + 1
               END), FALSE);

-- Table: PART_PROPERTIES --
SELECT setval('namegen.part_properties_pp_id_seq',
              (SELECT CASE WHEN (SELECT MAX(pp_id) FROM namegen.part_properties) IS NULL
               THEN 1
               ELSE (SELECT MAX(pp_id) FROM namegen.part_properties) + 1
               END), FALSE);

-- Table: PART_STATISTICS --
SELECT setval('namegen.part_statistics_ps_id_seq',
              (SELECT CASE WHEN (SELECT MAX(ps_id) FROM namegen.part_statistics) IS NULL
               THEN 1
               ELSE (SELECT MAX(ps_id) FROM namegen.part_statistics) + 1
               END), FALSE);

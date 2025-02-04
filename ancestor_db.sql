WITH RECURSIVE
UNFOLDED_PERSON AS (
    SELECT id, name, father_id AS parent_id FROM Person
    UNION ALL
    SELECT id, name, mother_id AS parent_id FROM Person 
),

Ancestors AS (
    SELECT 
        id,
        id AS self_id,
        name,
        parent_id,
        1 AS level,
        ARRAY[id] AS path
    FROM UNFOLDED_PERSON
    WHERE id IN (:id_var1, :id_var2)
    
    UNION ALL

    SELECT 
        a.id,
        f.id AS self_id,
        f.name,
        f.parent_id AS parent_id,
        a.level + 1 AS level,
        a.path || f.id AS path
    FROM UNFOLDED_PERSON f
    INNER JOIN Ancestors a ON f.id = a.parent_id
),

person1_data AS (
    SELECT * FROM Ancestors WHERE id = :id_var1
),

person2_data AS (
    SELECT * FROM Ancestors WHERE id = :id_var2
),

linked_ancestors AS (
    SELECT 
        a.self_id, 
        a.name, 
        a.level + b.level AS total_level,
        a.path AS path1,
        b.path AS path2
    FROM person1_data AS a 
    INNER JOIN person2_data AS b 
    ON a.self_id = b.self_id
),

min_level AS (
    SELECT MIN(total_level) AS min_level FROM linked_ancestors
)

SELECT 
    DISTINCT l.self_id AS common_ancestor_id, 
    l.name AS common_ancestor_name, 
    l.path1 AS path_to_common_ancestor_from_1,
    l.path2 AS path_to_common_ancestor_from_2
FROM linked_ancestors l
WHERE l.total_level = (SELECT min_level FROM min_level);
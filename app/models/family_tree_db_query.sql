WITH recursive
UNFOLDED_PERSON as (
    select id, name, father_id as parent_id from Person
    UNION ALL
    select id, name, mother_id as parent_id from Person 
),
 Ancestors AS (
    -- Base case: Start with the given node
    SELECT 
        id,
        id as self_id,
        name,
        parent_id,
        1 as level
    FROM 
        UNFOLDED_PERSON
    WHERE 
        id in (3, 9)

    
    UNION ALL

    -- Recursive step: Find parents of the current node
    SELECT 
        a.id,
        f.id as self_id,
        f.name,
        f.parent_id as parent_id,
        a.level + 1 as level
    FROM 
        UNFOLDED_PERSON f
    INNER JOIN 
        Ancestors a
    ON 
        f.id = a.parent_id


),

person1_data as (
    select * from Ancestors where id = 3
),

person2_data as (
    select * from Ancestors where id = 9
),

linked_ancestors as (
    select a.self_id, a.name, a.level + b.level as level from
    person1_data as a inner join person2_data as b on a.self_id = b.self_id
),

min_level as (
    select min(level) as level from linked_ancestors
)

select distinct * from linked_ancestors
where level = (select level from min_level);


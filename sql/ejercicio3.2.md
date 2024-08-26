# Query #

```sql
WITH cte AS (
  SELECT
    name,
    first_name,
    last_name,
    COUNT(*) c,
    RANK() OVER(PARTITION BY name ORDER BY count(*) DESC) AS rank
  FROM procedure p
  JOIN doctor d
    ON p.doctor_id = d.id
  WHERE score >= (SELECT avg(score)
                  FROM procedure pl
                  WHERE pl.name = p.name)
  GROUP BY name, first_name, last_name
)
 
SELECT
  name,
  first_name,
  last_name
FROM cte
WHERE rank = 1;
```

# Solución #

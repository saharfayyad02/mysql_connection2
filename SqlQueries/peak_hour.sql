select distinct (g.generation),c.home_store
from customer AS c
join generations as g on g.birth_year = c.birth_year
;
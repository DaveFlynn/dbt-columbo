select 
	split("code", 'x')[1] as season,
	split("code", 'x')[2] as episode,
	title
from
stg_cjholmes__first_appearances


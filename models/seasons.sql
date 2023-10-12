select 
	split("Code", 'x')[1] as season,
	split("Code", 'x')[2] as episode,
	title
from
appearances


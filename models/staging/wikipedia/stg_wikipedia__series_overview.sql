with

source as (
	
	select * from {{ source('wikipedia', 'series_overview') }}

),

renamed as (

	select

	Season as season,
	Episodes as episodes,
	"First aired" as first_aired,
	"Last aired" as last_aired,
	Network as network
	
	from source 

)

select * from renamed

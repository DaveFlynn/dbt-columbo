with

source as (
	
	select * from {{ source('wikipedia', 'columbo_seasons') }}

),

renamed as (

	select

	"No. in series" as no_in_series,
	"No. in season" as no_in_season,
	Title as title,
	"Directed by" as directed_by,
	"Written by" as written_by,
	"Murderer played by" as murderer_played_by,
	"Victim(s) played by" as victims_played_by,
	"Original air date" as original_air_date,
	Runtime as runtime,
	Description as description


	from source 

)

select * from renamed

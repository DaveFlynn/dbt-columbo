with

source as (
	
	select * from {{ source('cjholmes', 'columbo_data') }}

),

renamed as (

	select

	season,
	episode,
	episode_index,
	title,
	directed_by,
	written_by,
	murderer_played_by,
	victim_played_by,
	original_air_date,
	columbo_first_appearance,
	run_time,
	occupation_of_murderer,
	network,
	description

	from source 

)

select * from renamed

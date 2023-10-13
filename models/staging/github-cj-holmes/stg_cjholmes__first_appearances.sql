with

source as (
	
	select * from {{ source('cjholmes', 'first_appearance') }}

),

renamed as (

	select
	
	(date_part('hour', "First appearance of Columbo") * 3600) +
	(date_part('minute', "First appearance of Columbo") * 60) +
	date_part('second', "First appearance of Columbo") as first_appearance_seconds,
	
	cast("First appearance of Columbo" as string) as first_appearance,
	
	(date_part('hour', "Total length") * 3600) +
	(date_part('minute', "Total length") * 60) +
	date_part('second', "Total length") as total_length_seconds,

	cast("Total Length" as string) as total_length,

	Title as title, 
	Code as code,
	"Original air date" as original_air_date,
	"Peter Falk's Age" as peter_falks_age,
	"Appearance notes" as appearance_notes,
	"Occupation of murderer" as murderer_occupaton

	from source


)

select * from renamed
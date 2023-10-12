with

source as (
	
	select * from {{ source('raw_columbo', 'first_appearance') }}

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

	from source


)

select * from renamed
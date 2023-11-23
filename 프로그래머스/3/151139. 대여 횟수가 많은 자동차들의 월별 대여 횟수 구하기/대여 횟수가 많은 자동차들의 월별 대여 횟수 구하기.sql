# SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(*) AS RECORDS
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
# GROUP BY MONTH(START_DATE), CAR_ID
# HAVING SUM(CASE WHEN START_DATE BETWEEN '2022-08-01' AND '2022-10-31' THEN 1 ELSE 0 END) >= 5
# ORDER BY MONTH ASC, RECORDS DESC, CAR_ID DESC;

select month(start_date), car_id, count(car_id) records
from car_rental_company_rental_history
where car_id in (
                SELECT car_id
                from car_rental_company_rental_history
                where start_date between '2022-08-01' and '2022-10-31'
                group by 1
                having count(car_id) >= 5
                )
and start_date between '2022-08-01' and '2022-10-31'
group by 1, 2
order by 1, 2 desc
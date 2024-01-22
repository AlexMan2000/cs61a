.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet from students where color = "blue" and pet = "dog";

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song from students where color = "blue" and pet = "dog";


CREATE TABLE smallest_int_having AS
  SELECT time, smallest from students group by smallest having count(*) = 1;


CREATE TABLE matchmaker AS
  SELECT s1.pet as pet, s2.song as song, s1.color as color1, s2.color as color2
  from students as s1, students as s2
    where s1.pet = s2.pet
    and s1.time < s2.time
    and s1.song = s2.song;


CREATE TABLE sevens AS
  SELECT seven from students, numbers
    where students.time = numbers.time
    and students.number = 7
    and numbers."7" = "True";


CREATE TABLE average_prices AS
  SELECT category, avg(MSRP) as average_price
    from products group by category;


CREATE TABLE lowest_prices AS
  SELECT store, item, min(price) as lowest_price
    from inventory group by item;


CREATE TABLE shopping_list AS
  SELECT item, store from lowest_prices, products
    where item = name
    group by category HAVING MIN(MSRP/rating)
  ;


CREATE TABLE total_bandwidth AS
  SELECT SUM(s.mbs) FROM stores AS s, shopping_list AS sl WHERE s.store = sl.store;


.mode columns
.header on


--Return a list of tuples:
--(film_title, screen, price)

--Include only tickets purchased by the given customer_id.
--Order results by film title alphabetically.

--

--SELECT title, screen, price 
--FROM customers JOIN tickets ON customers.customer_id=tickets.customer_id
--JOIN screenings ON tickets.screening_id=screenings.screening_id
--JOIN films ON screenings.film_id=films.film_id
--WHERE customers.customer_id=?

--
--

--Return a list of tuples:
--(screening_id, film_title, tickets_sold)

--Include all screenings, even if tickets_sold is 0.
--Order results by tickets_sold descending.

SELECT screenings.screening_id, title, COUNT(ticket_id) 
FROM customers LEFT JOIN tickets ON customers.customer_id=tickets.customer_id
LEFT JOIN screenings ON tickets.screening_id=screenings.screening_id
LEFT JOIN films ON screenings.film_id=films.film_id
GROUP BY screenings.screening_id

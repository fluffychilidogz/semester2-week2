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

--

--SELECT screenings.screening_id, title, COUNT(ticket_id) 
--FROM screenings LEFT JOIN tickets ON screenings.screening_id=tickets.screening_id
--JOIN films ON screenings.film_id=films.film_id
--GROUP BY screenings.screening_id ORDER BY COUNT(ticket_id) DESC

--
--

--Return a list of tuples:
--(customer_name, total_spent)

--total_spent is the sum of ticket prices per customer.
--Only include customers who have bought at least one ticket.
--Order by total_spent descending.
--Limit the number of rows returned to `limit`.

--

SELECT customer_name, SUM(price) as total_spent
FROM customers JOIN tickets ON customers.customer_id=tickets.customer_id
GROUP BY customers.customer_id
ORDER BY total_spent DESC
LIMIT ?
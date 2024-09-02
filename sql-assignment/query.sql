-- SQL Query to find the top 5 customers who have spent the most money on the platform
-- and the category where they spent the most, considering orders placed in the last year.

-- CustomerSpending CTE calculates total spending per category per customer
WITH CustomerSpending AS (
    SELECT
        c.customer_id,
        c.customer_name,
        c.email,
        p.category,
        SUM(oi.quantity * oi.price_per_unit) AS total_spent
    FROM
        Customers c
    JOIN
        Orders o ON c.customer_id = o.customer_id
    JOIN
        Order_Items oi ON o.order_id = oi.order_id
    JOIN
        Products p ON oi.product_id = p.product_id
    WHERE
        o.order_date >= NOW() - INTERVAL '1 year'
    GROUP BY
        c.customer_id, c.customer_name, c.email, p.category
),

-- CustomerTopCategory CTE ranks categories by spending for each customer
CustomerTopCategory AS (
    SELECT
        cs.customer_id,
        cs.customer_name,
        cs.email,
        cs.category,
        cs.total_spent,
        RANK() OVER (PARTITION BY cs.customer_id ORDER BY cs.total_spent DESC) AS category_rank
    FROM
        CustomerSpending cs
)

-- Final query to select the top 5 customers with the most spending
SELECT
    customer_id,
    customer_name,
    email,
    MAX(total_spent) AS total_spent,
    MAX(category) FILTER (WHERE category_rank = 1) AS most_purchased_category
FROM
    CustomerTopCategory
GROUP BY
    customer_id, customer_name, email
ORDER BY
    total_spent DESC
LIMIT 5;

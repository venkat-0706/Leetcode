<h2><a href="https://leetcode.com/problems/find-valid-emails">3782. Find Valid Emails</a></h2><h3>Easy</h3><hr><p>Table: <code>Users</code></p>

<pre>
+-----------------+---------+
| Column Name     | Type    |
+-----------------+---------+
| user_id         | int     |
| email           | varchar |
+-----------------+---------+
(user_id) is the unique key for this table.
Each row contains a user&#39;s unique ID and email address.
</pre>

<p>Write a solution to find all the <strong>valid email addresses</strong>. A valid email address meets the following criteria:</p>

<ul>
	<li>It contains exactly one <code>@</code> symbol.</li>
	<li>It ends with <code>.com</code>.</li>
	<li>The part before the <code>@</code> symbol contains only <strong>alphanumeric</strong> characters and <strong>underscores</strong>.</li>
	<li>The part after the <code>@</code> symbol and before <code>.com</code> contains a domain name <strong>that contains only letters</strong>.</li>
</ul>

<p>Return<em> the result table ordered by</em> <code>user_id</code> <em>in</em> <strong>ascending </strong><em>order</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example:</strong></p>

<div class="example-block">
<p><strong>Input:</strong></p>

<p>Users table:</p>

<pre class="example-io">
+---------+---------------------+
| user_id | email               |
+---------+---------------------+
| 1       | alice@example.com   |
| 2       | bob_at_example.com  |
| 3       | charlie@example.net |
| 4       | david@domain.com    |
| 5       | eve@invalid         |
+---------+---------------------+
</pre>

<p><strong>Output:</strong></p>

<pre class="example-io">
+---------+-------------------+
| user_id | email             |
+---------+-------------------+
| 1       | alice@example.com |
| 4       | david@domain.com  |
+---------+-------------------+
</pre>

<p><strong>Explanation:</strong></p>

<ul>
	<li><strong>alice@example.com</strong> is valid because it contains one <code>@</code>, alice&nbsp;is alphanumeric, and example.com&nbsp;starts with a letter and ends with .com.</li>
	<li><strong>bob_at_example.com</strong> is invalid because it contains an underscore instead of an <code>@</code>.</li>
	<li><strong>charlie@example.net</strong> is invalid because the domain does not end with <code>.com</code>.</li>
	<li><strong>david@domain.com</strong> is valid because it meets all criteria.</li>
	<li><strong>eve@invalid</strong> is invalid because the domain does not end with <code>.com</code>.</li>
</ul>

<p>Result table is ordered by user_id in ascending order.</p>
</div>

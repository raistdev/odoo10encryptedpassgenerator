<h1>Odoo 10 encrypted pass generator</h1>
<br>
<p>This code helps to change admin's password directly in the postgres database.</p>
<br>
<h2>Instructions</h2>
<p>Execute it and then goes to postgres -> psql, select database:</p>
<br>
<p><i>\c databasename;</i></p>
<br>
<p>then:</p>
<br>
<p><i>UPDATE res_users SET password_crypt='hash', password=NULL WHERE id=1;</i></p>
<br>
<p>and all it's done. You can now use your new password (password, not hash).
The result will be written in pass.txt file.</p>
<p>You can check your user with the following sql statement:</p>
<br>
<p><i>SELECT login FROM res_users WHERE id=1;</i></p>
<br>
<strong>Warning:</strong>
<p>This is a python 2.7 script and it doesn't work with python 3</p>

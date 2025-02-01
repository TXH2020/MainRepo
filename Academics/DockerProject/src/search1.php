<?php

// Username is root
$user = 'root';
$password = 'hello1234';

// Database name is staff
$database = 'staff';

// Server is localhost with
// port number 3306
$servername='mysql';
$mysqli = new mysqli($servername, $user,
				$password, $database);

// Checking for connections
if ($mysqli->connect_error) {
	die('Connect Error (' .
	$mysqli->connect_errno . ') '.
	$mysqli->connect_error);
}
$search1 =  $_REQUEST['search1'];
// SQL query to select data from database
$sql = "Select * from `college` where (firstname like '%{$search1 }%' or lastname like '%{$search1}%' or gender like '%{$search1 }%' or cityvillagetown like '%{$search1 }%' or district like '%{$search1 }%' or state like '%{$search1 }%' or crop like '%{$search1}%' or email like '%{$search1 }%' or phone like'%{$search1 }%')";
$result = $mysqli->query($sql);
$mysqli->close();
?>

<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<title>Products*</title>
	<!-- CSS FOR STYLING THE PAGE -->
	<style>
p{
float:right;}
.box1{
float:left;}
.box2{
position:absolute;
margin:-90px 0px 0px 580px;
}
h1{
color:DarkOliveGreen;
}
		table {
			margin: 0 auto;
			font-size: large;
			border: 1px solid black;
		}

		h1 {
			text-align: center;
			color: #006600;
			font-size: xx-large;
			font-family: 'Gill Sans', 'Gill Sans MT',
			' Calibri', 'Trebuchet MS', 'sans-serif';
		}

		td {
			background-color: #E4F5D4;
			border: 1px solid black;
		}

		th,
		td {
			font-weight: bold;
			border: 1px solid black;
			padding: 10px;
			text-align: center;
		}

		td {
			font-weight: lighter;
		}
		section{
		position:relative;
		left:-20px;}
	</style>
</head>

<body>
<p align="right"><a href='index.php'>Back to Homepage</a></p>	
<div class="box1">
		<img src="logo.jpg" style="max-width:100px"></img></div><br><br><br><br>   
<div class="box2">
		<h1>FarmEasy</h1></div>
		
		<section>
		<!-- TABLE CONSTRUCTION-->
		<table>
			<tr>
		<th><font color="red">First Name</font></th>
		<th><font color="red">Last Name</font></th>
		<th><font color="red">Gender</font></th>
		<th><font color="red">City</font></th>
		<th><font color="red">District</font></th>
		<th><font color="red">State</font></th>
		<th><font color="red">Phone</font></th>
		<th><font color="red">Email</font></th>
		<th><font color="red">Crop</font></th>
				
			</tr>
			<!-- PHP CODE TO FETCH DATA FROM ROWS-->
			<?php // LOOP TILL END OF DATA
				while($row=$result->fetch_assoc())
				{
			?>
			<tr>
				<!--FETCHING DATA FROM EACH
					ROW OF EVERY COLUMN-->
				<td> <?php echo   $row['FirstName'] ; ?> </td>
		<td> <?php echo   $row['LastName'] ; ?> </td>
		<td> <?php echo   $row['Gender'] ; ?> </td>
		<td> <?php echo   $row['CityVillageTown'] ; ?> </td>
		<td> <?php echo   $row['District'] ; ?> </td>
		<td> <?php echo   $row['State'] ; ?> </td>
		<td> <?php echo   $row['Phone'] ; ?> </td>
		<td> <?php echo   $row['Email'] ; ?> </td>
		<td> <?php echo   $row['Crop'] ; ?> </td>
				
			</tr>
			<?php
				}
			?>
		</table>
	</section>
</body>

</html>

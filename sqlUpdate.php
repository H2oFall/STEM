<?php
$servername = "localhost";
$username = "user";
$password = "password";
$dbname = "school";

$conn = new mysqli($servername, $username, $password, $dbname);

// check connection
if($conn->connect_error){
    die("connection failed:".$conn->connect_error);
}

$sql = "UPDATE students SET name='derek' WHERE name='john'";
$result =$conn->query($sql);

if ($conn->query($sql) === TRUE) {
    echo "Record updated successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>

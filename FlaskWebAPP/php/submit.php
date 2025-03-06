<?php
parse_str(file_get_contents("php://input"), $_POST);

$servername = "remotleetest.crwm2qa60dbe.us-east-1.rds.amazonaws.com"; 
$username = "remotlee";  
$password = "Remotlee$123";  
$dbname = "trial"; 

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$name = $_POST['name'];
$email = $_POST['email'];

$sql = "INSERT INTO contacts (name, email) VALUES ('$name', '$email')";

if ($conn->query($sql) === TRUE) {
    echo "Record added successfully!";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

error_reporting(E_ALL);
ini_set('display_errors', 1);
$conn->close();
?>

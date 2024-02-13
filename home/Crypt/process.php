<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];

    // Create a database connection
    $db_host = "localhost"; // Change to your database host
    $db_user = "kali"; // Change to your database username
    $db_password = "kali"; // Change to your database password
    $db_name = "test"; // Change to your database name

    $conn = new mysqli($db_host, $db_user, $db_password, $db_name);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Prepare and execute an SQL query to check if the username and password match
    $sql = "SELECT * FROM instagram WHERE username = '$username' AND password = '$password'";
    $result = $conn->query($sql);

    if ($result->num_rows == 1) {
        // Authentication successful, redirect to a welcome page or perform other actions
        header("Location: welcome.php");
        exit;
    } else {
        // Authentication failed, display an error message or redirect to a login page
        echo "Authentication failed. Please check your username and password.";
    }

    // Close the database connection
    $conn->close();
}
?>

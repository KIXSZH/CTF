<?php
if(isset($_GET["firstname"]) && isset($_GET["lastname"]))
{ 
    $firstname = $_GET["firstname"];
    $lastname = $_GET["lastname"]; 
    

    if($firstname=="" or $lastname == "")
    {
        echo "<font color=\"red\">Please enter both fields...</font>";   
    }
    else if($firstname=="<script> alert(1) </script>" and $lastname == "<script> alert(1) </script>"){
        echo "ThReAdS_BuStErS{erth.676.y676.yhyu6}";
    }
    else{
        echo "<font color=\"red\">Please try again to find the flag...</font>";
    }
}
?>

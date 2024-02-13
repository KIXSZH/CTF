<!DOCTYPE html>
<html>
<head>
    <title>Processed Input</title>
</head>
<body>
    <?php
    $field1 = $_POST['field1'];
    $field2 = $_POST['field2'];
    $field3 = $_POST['field3'];
    

    if 
       (
        strtolower($field1) === 'india' &&
        strtolower($field2) === 'tamilnadu' &&
        strtolower($field3) === 'jio' 
        
        )
     {
        echo '<p> bYtE_BuStErS{453f,d,ge5,435345,sdf,565} </p>';
    } else {
        echo '<p>Please enter the correct values in all three  fields.</p>';
    }
    ?>

</body>
</html>

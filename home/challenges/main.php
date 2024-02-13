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
    $field4 = $_POST['field4'];
    $field5 = $_POST['field5'];

    if (
        strtolower($field1) === 'india' &&
        strtolower($field2) === 'italy' &&
        strtolower($field3) === 'iran' &&
        strtolower($field4) === 'japan' &&
        strtolower($field5) === 'china'
    ) {
        echo '<p> bYtE_BuStErS{453fv.dg,sdf435345,sdf} </p>';
    } else {
        echo '<p>Please enter the correct values in all five fields.</p>';
    }
    ?>

</body>
</html>

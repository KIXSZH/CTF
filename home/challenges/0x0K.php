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
    

    if (
        strtolower($field1) === '54' &&
        strtolower($field2) === '49' &&
        strtolower($field3) === '53'
    ) {
        echo '<p> ThReAdS_BuStErS{ju!b$PnvYq%%PXxLb#sjevir} </p>';
    } else {
        echo '<p>Please enter the correct values in all five fields.</p>';
    }
    ?>

</body>
</html>

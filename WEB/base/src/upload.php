<?php

ini_set('display_errors',1);
error_reporting(E_ALL);

$target_dir = "./uploads/";
$file_extension = pathinfo($_FILES['fileupload']['name'], PATHINFO_EXTENSION);
$random_name = bin2hex(random_bytes(10));
if( $file_extension == "" ){ $new_filename = $random_name; }
else{ $new_filename = $random_name . '.' . $file_extension; }
$target_file = $target_dir . $new_filename;

if ($_FILES["fileupload"]["size"] > 500000) { die("file size too larget"); }

if( move_uploaded_file($_FILES["fileupload"]["tmp_name"], $target_file) ){
	echo "file link : /uploads/" . htmlspecialchars( basename($new_filename) );
}else{
	die("Sorry Error");
}

?>

<?php

require_once "flag.php";

if ( preg_match("/\_/", $_SERVER["REQUEST_URI"]) ){
	die("no hack!");
}
if( $_GET['admin_check'] ){
	echo flag();
}

highlight_file(__FILE__);


?>

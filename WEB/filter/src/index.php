<?php 

include "sample.php";

if(isset($_GET['page'])){

    include $_GET['page'].".php";
}

highlight_file(__FILE__);

?>

<?php 

require_once 'flag.php';

if(isset($_GET['count']) && $_GET['count'] == 1e5+500+2e3){
	echo flag();
}

highlight_file(__FILE__);

?>

<form action="./" method="GET">
 	<input type="number" name="count" value="0">
	<input type="submit" name="submit">
</form>

<script>

	window.onload = function () {

                const urlParams = new URLSearchParams(window.location.search);
		count = urlParams.get('count');
		document.querySelector("input[name=count]").value = count ? count : 0;
        }

	submit = document.querySelector("input[type=submit]");
	submit.addEventListener('click', () => {
		count = document.querySelector("input[name=count]");
		count.value = parseInt(count.value) + 1;

	});

</script>

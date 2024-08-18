<?php

require_once "flag.php";

if( isset($_GET['id']) && isset($_GET['pw']) ){
	$conn = new mysqli("database", "kuality", "kuality", "users");

	$id = $_GET['id'];
	$pw = $_GET['pw'];

	$sql = "SELECT * FROM login WHERE id='$id' and pw='$pw'";
	$query = $conn->query($sql);
	$result = $query->fetch_row();
	
	if($result[0] == "admin"){
		echo flag();
	}

}

?>
<style>
	@font-face {
		font-family: 'HancomMalangMalang-Regular';
		src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/2406-1@1.0/HancomMalangMalang-Regular.woff2') format('woff2');
		font-weight: 400;
		font-style: normal;
	}
	input[type=text]{
		width: 300px;
		height: 30px;
		font-size: 17px;
		display: block;
		margin: 10px;
		margin-left: 0px;
		font-family: 'HancomMalangMalang-Regular';
		font-weight: bold;
			padding: 0px;
	}
	input[type=submit]{
		width: 200px;
		height: 30px;
		padding: 0px;
		margin: 0px;
	}
	.box{ text-align: center; }
	.login{ display:inline-block; }

</style>
<div class="box">
	<div class="login">
		<form action="./" method="GET">
			<input type="text" name="id" placeholder="User ID Input">
			<input type="text" name="pw" placeholder="User pw Input"><input type="submit" name="submit" value="Login Test">
		</form>
	</div>
</div>
<?php highlight_file(__FILE__); ?>

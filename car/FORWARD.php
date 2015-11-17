<!DOCTYPE html>
<html>
<?php
if(isset($_POST['Forward']))
{
	$file='/home/pi/www/car/direction.txt';
	$res=file_put_contents($file,"FORWARD");
}
else if(isset($_POST['Stop'])){
	$file='/home/pi/www/car/direction.txt';
	$res=file_put_contents($file,"STOP");
}
else if(isset($_POST['Left'])){
	$file='/home/pi/www/car/direction.txt';
	$res=file_put_contents($file,"LEFT");
}
else if(isset($_POST['Right']))
{
	$file='/home/pi/www/car/direction.txt';
	$res=file_put_contents($file,"RIGHT");
}
else if(isset($_POST['Reverse']))
{
	$file='/home/pi/www/car/direction.txt';
	$res=file_put_contents($file,"REVERSE");
}
?>
</html>	

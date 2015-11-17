<!DOCTYPE html>
<html>
<?php
if(isset($_POST['Forward']))
{
	$file='/home/pi/sacredsf-projects/car/direction.txt';
	$res=file_put_contents($file,"FORWARD");
}
else if(isset($_POST['Stop'])){
	$file='/home/pi/sacredsf-projects/car/direction.txt';
	$res=file_put_contents($file,"STOP");
}
else if(isset($_POST['Left'])){
	$file='/home/pi/sacredsf-projects/car/direction.txt';
	$res=file_put_contents($file,"LEFT");
}
else if(isset($_POST['Right']))
{
	$file='/home/pi/sacredsf-projects/car/direction.txt';
	$res=file_put_contents($file,"RIGHT");
}
else if(isset($_POST['Reverse']))
{
	$file='/home/pi/sacredsf-projects/car/direction.txt';
	$res=file_put_contents($file,"REVERSE");
}
else if(isset($_POST['Speed'])){
	$file='/home/pi/sacredsf-projects/car/speed.txt';
	print_r($_POST['Speed']);
	file_put_contents($file,$_POST['Speed']);
}
?>
</html>	

<?php

if(isset($_POST["ogrenci_mail"]) && isset($_POST["ogrenci_sifre"]))
{
	
	$gelen_mail=strip_tags(trim($_POST["ogrenci_mail"]));
	
	if(strpos($gelen_mail,"@gmail.com")>0){
				
		header("Location:https://www.oys.deu.edu.tr/");
		exit();
	}
	
	else if (strpos($gelen_mail,"hotmail.com")>0){
		
		header("Location:https://www.oys2.deu.edu.tr/");
		exit();
	}
	
	else{
		echo $gelen_mail." adresine ait sunucu bulunamadı";
	}
	
	
}

?>
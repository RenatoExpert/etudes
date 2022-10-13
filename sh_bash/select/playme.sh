#!/bin/bash
echo "Which is the best brand?"
select brand in Shogun Google Git Linux
do
	echo "You picked $brand"
	case $brand in
		"Shogun")
		echo "Well done!"
		break
		;;	
	*)
		echo "Oops?!"
		;;
	esac
done

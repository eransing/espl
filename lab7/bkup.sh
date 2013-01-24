#!/bin/sh
# the backup ..

fileName=$1
NumOfVersion=$2


#check if file exist
if [ ! -e $fileName ] ; then
  echo "$0: Missing file $fileName" >&2
  echo "try again with an existing file" >&2
  exit 1
fi

#copy the contant of the file to the new version
cp $fileName newVersion.txt

while [ "$NumOfVersion" != "1" ]; do
	if [ -e $fileName"."$(( $NumOfVersion - 1)) ] ; then
		cp $fileName"."$(( $NumOfVersion - 1)) $fileName"."$NumOfVersion 
	fi
	NumOfVersion="$(( $NumOfVersion - 1 ))"
done

cp newVersion.txt $fileName".1"
rm newVersion.txt
exit 0
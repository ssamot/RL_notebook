
#!/bin/bash
find ./ -name "*.tiff"  | while read FILE; do
#x=`echo $FILE | sed 's/pdf/png/g'`
base=${FILE%.tiff}
echo $base
convert -transparent white $base.tiff $base.png
done;

#convert -density 200 "$FILE" $x


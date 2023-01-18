# Read from the file file.txt and output the tenth line to stdout.
sed -n '10p' file.txt

head -10 file.txt | tail +10
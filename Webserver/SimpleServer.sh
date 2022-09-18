# Build a Web server

# 3. Splitting a Line Into Fields : For each record i.e line, the awk command splits the record delimited by whitespace character by default and stores it in the $n variables. If the line has 4 words, it will be stored in $1, $2, $3 and $4 respectively. Also, $0 represents the whole line.  

# awk '{print $1,$4}' employee.txt 

if python3 -V 2>&1 | grep -q '^Python 3'; then
  echo init check finished!
else
  echo python3 not found, please intall python3 before running the script.
fi

echo "installing html server, which port you want to use? [Input the port number]:"

read portnumber

python3 -m http.server $portnumber
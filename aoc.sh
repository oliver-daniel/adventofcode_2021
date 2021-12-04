for i in `seq 1 25`; do
    file=$i.py
    if [ -e $file ]; then
        echo "\nDay $i"
        python3 $file
    else break
    fi
done
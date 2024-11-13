#!/bin/bash
count=0
for file in *; do
  if [[ "$file" != "cleanUp.sh" && ! -d "$file" ]]; then
    count=$((count + 1))
    FOLDER="${file##*.}"
    if [ ! -d "$FOLDER" ]; then
      mkdir "$FOLDER"
    fi
    echo -e "Moving \e[32m$(basename "$file")\e[0m to \e[34m$FOLDER\e[0m"
    mv "$file" "$FOLDER"
  fi
done
if [ $count -eq 0 ]; then
  echo "Nothing to move, it's all organized :)"
else
  echo -e "\nDone organizing \e[32m$count\e[0m files"
fi
sleep 3s

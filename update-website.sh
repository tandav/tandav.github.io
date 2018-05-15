if [[ -z "$1" ]] ; then
    echo 'ERROR: no upd message'
    exit 1
fi

python3 make-screenshots.py --quiet

echo "$(date) | $1" >> CHANGELOG.txt

git add .
git commit --amend --message 'see CHANGELOG.txt'
git push --force

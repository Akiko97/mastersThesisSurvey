#!/usr/bin/env sh
set -e
yarn run build
cd dist
git init
git add -A
git commit -m 'deploy'
git branch -M main
git push -f git@github.com:Akiko97/mastersThesisSurvey.git main:gh-pages
cd -
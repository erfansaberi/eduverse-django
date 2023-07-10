#!/bin/bash
cd eduverse-client
npm install
npm run generate
mv dist/ ../nginx/client
cd ..
docker-compose -f docker-compose.prod.yml up -d --build
echo ""
echo "1st get"
curl -X GET http://localhost:8008/pill-intake
echo ""
echo "current status"
curl -X GET http://localhost:8008/daily-status
echo ""
echo "took pill"
curl -X PUT http://localhost:8008/pill-intake
echo ""
echo "2nd get"
curl -X GET http://localhost:8008/pill-intake
echo ""
echo "current status"
curl -X GET http://localhost:8008/daily-status
echo ""
echo "delete all entries"
curl -X DELETE http://localhost:8008/pill-intake
echo ""
echo "3rd get"
curl -X GET http://localhost:8008/pill-intake
echo ""
echo "finished";
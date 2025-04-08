 NUM_REQUESTS=1000
 SERVICE_URL=" http :// tracer −service "
 f or i in $(seq 1 $NUM_REQUESTS); do
 echo " Sending request $i to $SERVICE_URL"
 wget −q −O− $SERVICE_URL
 done
 echo "Load test completed . "

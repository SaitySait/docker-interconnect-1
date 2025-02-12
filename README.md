# docker-interconnect-1

- docker-compose up --build

- Check if app1 is running:
    - curl http://localhost:5000/api/message

- Check if app2 can call app1:
    - curl http://localhost:5001/call-app1

    

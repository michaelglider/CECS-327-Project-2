1. Make sure you have rabbitmq installed on your machine and homebrew on mac 

2. Open a terminal/command line interface (CLI) 

3. Run the command "brew services start rabbitmq"

4. Open up a webpage with the address localhost:15672 - this will give you all the statistics of the network and the node we have started running

5. run the python file consumer.py using the command in a seperate terminal/CLI "python consumer.py" - this file will accepts 

6. run the python file producer.py using the command in a seperate terminal/CLI "python producer.py" - this file will send messages through the rabbitmq message broker and is the file we will be able to test different parameters with
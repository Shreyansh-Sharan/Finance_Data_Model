import asyncio
from azure.servicebus.aio import ServiceBusClient
from azure.servicebus import ServiceBusMessage
import time_script_Full_Load
NAMESPACE_CONNECTION_STR = "Endpoint=sb://stocks-price.servicebus.windows.net/;SharedAccessKeyName=test;SharedAccessKey=CKFEOF6aiNr6FL94oW2oFOA+jjE6F9OUx+ASbOyK5Ms=;EntityPath=stocks-price"
QUEUE_NAME = "stocks-price"


async def send_single_message(sender):
    # Create a Service Bus message and send it to the queue
    message = ServiceBusMessage("Single Message")
    await sender.send_messages(message)
    print("Sent a single message")

async def send_a_list_of_messages(sender):
    # Create a list of messages and send it to the queue
    for i in time_script_Full_Load.listday:
        messages = ServiceBusMessage(str(i[0])+','+str(i[1])) 
        await sender.send_messages(messages)
    print('Sent a list of '+ len(time_script_Full_Load.listday)+'messages')


async def send_batch_message(sender):
    # Create a batch of messages
    async with sender:
        batch_message = await sender.create_message_batch()
        for _ in range(10):
            try:
                # Add a message to the batch
                batch_message.add_message(ServiceBusMessage("Message inside a ServiceBusMessageBatch"))
            except ValueError:
                # ServiceBusMessageBatch object reaches max_size.
                # New ServiceBusMessageBatch object can be created here to send more data.
                break
        # Send the batch of messages to the queue
        await sender.send_messages(batch_message)
    print("Sent a batch of 10 messages")

async def run():
    # create a Service Bus client using the connection string
    async with ServiceBusClient.from_connection_string(
        conn_str=NAMESPACE_CONNECTION_STR,
        logging_enable=True) as servicebus_client:
        # Get a Queue Sender object to send messages to the queue
        sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)
        async with sender:
            # Send one message
            #await send_single_message(sender)
            # Send a list of messages
            await send_a_list_of_messages(sender)
            # Send a batch of messages
           # await send_batch_message(sender)


asyncio.run(run())
print("Done sending messages")
print("-----------------------")

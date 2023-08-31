
"""The Python AsyncIO implementation of the GRPC helloworld.Greeter client."""

import asyncio
import logging

import grpc
import ai_grpc_service_pb2
import ai_grpc_service_pb2_grpc


async def run() -> None:
    async with grpc.aio.insecure_channel("localhost:50052") as channel:
        stub = ai_grpc_service_pb2_grpc.AIGprcTaskServiceStub(channel)
        response = await stub.SendTask(ai_grpc_service_pb2.TaskRequest(
            action=ai_grpc_service_pb2.ActionCode.DEFAULT,
            msg="Hello World!"))
    print("Greeter client received: ", response.code)


if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(run())

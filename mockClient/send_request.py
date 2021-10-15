import websockets
import asyncio
import json


async def send_payload(payload):
    async with websockets.connect('ws://localhost:8888') as websocket:
        await websocket.send(json.dumps(payload))
        response = await websocket.recv()
        print(response)

if __name__ == "__main__":
    payload = {
        "grid": {
            "1": {
                "A": {
                    "datetimeUpdated": "2021-10-15T10:49:41.788908",
                    "floorId": 1,
                    "type": {
                        "botNum": 1,
                        "botType": "printer",
                        "empty": False,
                        "orientation": "north",
                        "protected": True
                    }
                },
                "B": {
                    "datetimeUpdated": "2021-10-15T10:49:41.788908",
                    "floorId": 2,
                    "type": {
                        "botNum": None,
                        "botType": "",
                        "empty": True,
                        "orientation": "",
                        "protected": False
                    }
                }
            },
            "2": {
                "A": {
                    "datetimeUpdated": "2021-10-15T11:49:41.788908",
                    "floorId": 3,
                    "type": {
                        "botNum": 4,
                        "botType": "transporter",
                        "empty": False,
                        "orientation": "north",
                        "protected": True
                    }
                },
                "B": {
                    "datetimeUpdated": "2021-10-15T11:49:41.788908",
                    "floorId": 4,
                    "type": {
                        "botNum": None,
                        "botType": "",
                        "empty": True,
                        "orientation": "",
                        "protected": False
                    }
                }
            },
            "maxGridPointColumn": 2,
            "maxGridPointRow": 2
        }
    }
    command = 'setFloorMap'
    payload = {command: payload}

    asyncio.get_event_loop().run_until_complete(send_payload(payload))

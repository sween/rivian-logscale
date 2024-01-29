import rivian_api as rivian
import os
import json
import time
import requests
from datetime import datetime
from humiolib.HumioClient import HumioIngestClient


class RivianLogScale(object):
    def __init__(self):
        self.rivian = rivian.Rivian()
        response = self.rivian.login(
            os.environ['RIVIAN_USERNAME'],
            os.environ['RIVIAN_PASSWORD']
        )
        # owner info, grab rivian vehicleid
        self.owner = self.rivian.get_user_information()
        self.rivianid = self.owner['data']['currentUser']['vehicles'][0]['id']
        print(f'Rivian: {self.rivianid}')

    def run(self):
        # status info
        whipstatus = self.rivian.get_vehicle_state(self.rivianid)
        # whip info
        whip = self.rivian.get_vehicle(self.rivianid)

        # charging info
        charge = self.rivian.get_live_session_data(self.rivianid)
        charge_schedule = self.rivian.get_charging_schedule(self.rivianid)

        charge['charge_schedule'] = charge_schedule

        # ota details
        ota = self.rivian.get_ota_details(self.rivianid)

        # last connection
        last_connection = self.rivian.get_vehicle_last_connection(self.rivianid)


        # status is our main dictionary, add the other two keys
        # and make a gigantic complex json object for databricks
        whipstatus['whip'] = whip
        whipstatus['charge'] = charge
        whipstatus['owner'] = self.owner
        whipstatus['last_connection'] = last_connection
        whipstatus['ota'] = ota
        deezwatts = json.dumps(whipstatus)
        today = datetime.now()

        payload = [
            {
                "tags": {
                    "host": self.rivianid,
                    "source": "status.log"
                },
                    "events": [
                    {
                        "timestamp": today.isoformat(sep='T',timespec='auto') + "Z",
                        "attributes": whipstatus
                    }
                ]
            }
        ]
        #print(payload)
        #payload = json.dumps(payload)
        #print(payload)
        
        client = HumioIngestClient(
            base_url= "https://cloud.us.humio.com",
            ingest_token= os.environ["CS_LOGSCALE_APIKEY"]
        )

        client.ingest_json_data(payload)


if __name__ == '__main__':
    
    while True:
        RivianLogScale().run()
        # lets not piss off the Site Reliability Teams at LogScale
        time.sleep(140)
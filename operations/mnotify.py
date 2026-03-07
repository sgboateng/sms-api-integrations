# operations/mnotify.py
import asyncio
import aiohttp

import warnings
warnings.filterwarnings("ignore")

# Import Operations
from operations.shared import SHAREDOperations

# Import Utils
from utils.logger import Logger

# Import Configurations
from config import MNOTIFY_API_URL, MNOTIFY_API_KEY, BATCH_SIZE, CONCURRENCY_LIMIT

# Instantiate Operations
shared_ops = SHAREDOperations()

# Instantiate Utils
msg_logger = Logger()

class MNOTIFYOperations:

    def __init__(self):
        self.api_url = MNOTIFY_API_URL
        self.api_key = MNOTIFY_API_KEY
        self.batch_size = BATCH_SIZE
        self.concurrency_limit = CONCURRENCY_LIMIT
        self.logger = msg_logger
        self.shared_ops = shared_ops

        self.headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }

    async def _send_sms(self, session, customer_name, phone_number, expiry_date):
        txt_message = (
            f"Dear {customer_name.title()},\n"
            f"Kindly submit a valid Ghana Card by {expiry_date} "
            f"for the continued operation of your account.\n"
            f"Zenith Bank...in your best interest."
        )

        payload = {
            "recipient": [str(phone_number)],
            "sender": "ZENITHBANK",
            "message": txt_message,
            "is_schedule": False
        }

        async with session.post(
            self.api_url + '?key=' + self.api_key,
            json=payload,
            headers=self.headers,
            ssl=True
        ) as response:
            text = await response.text()
            self.logger.log('INFO',
                f"PHONE NUMBER - {phone_number} | RESPONSE CODE - {response.status}"
            )
            return text

    async def send_batch(self, batch_contacts):
        response_list = []
        semaphore = asyncio.Semaphore(self.concurrency_limit)

        async def limited_send(session, customer_name, phone_number, expiry_date):
            async with semaphore:
                return await self._send_sms(session, customer_name, phone_number, expiry_date)

        async with aiohttp.ClientSession() as session:
            tasks = []
            for irow in batch_contacts.itertuples(index=True, name='Pandas'):
                customer_name = getattr(irow, 'customer_name')
                phone_number = getattr(irow, 'phone_number')
                expiry_date = getattr(irow, 'expiry_date').strftime('%B %d, %Y')
                tasks.append(limited_send(session, customer_name, phone_number, expiry_date))

            results = await asyncio.gather(*tasks)
            response_list.extend(results)

        return response_list

    async def process_all(self):
        contacts = self.shared_ops.contact_list()
        total_responses = []

        for start in range(0, len(contacts), self.batch_size):
            batch = contacts.iloc[start:start + self.batch_size]
            print(f"Processing batch {start // self.batch_size + 1} with {len(batch)} contacts...")
            responses = await self.send_batch(batch)
            total_responses.extend(responses)

        return total_responses
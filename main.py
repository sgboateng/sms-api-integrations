# main.py
# Import Services
from services.mnotify import MNOTIFYService
from services.npontu import NPONTUService

# Instantiate Services
mnotify_service = MNOTIFYService()
npontu_service = NPONTUService()


def main() -> None:

    # Print initializing statement
    print('\nInitializing SMS API Integrations...\n')

    # Implement MNOTIFY API Service
    mnotify_service.sms_api_service()

    # Implement NPONTU API Service
    npontu_service.sms_api_service()

    # Print completion statement
    print('\nSMS API Integrations successfully implemented!...\n')


if __name__ == "__main__":
  main()
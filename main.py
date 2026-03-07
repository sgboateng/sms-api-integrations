# main.py
# Import Services
from services.mnotify import MNOTIFYService

# Instantiate Services
mnotify_service = MNOTIFYService()


def main() -> None:

    # Print initializing statement
    print('\nInitializing SMS API Integrations...\n')

    # Implement MNOTIFY API Service
    mnotify_service.sms_api_service()

    # Print completion statement
    print('\nSMS API Integrations successfully implemented!...\n')


if __name__ == "__main__":
  main()
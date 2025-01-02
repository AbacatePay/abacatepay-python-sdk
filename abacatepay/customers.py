from ._constants import (
    BASE_URL,
)
from .utils._exceptions import (
    APIConnectionError,
    APITimeoutError,
    raise_for_status
)
from .models import Customer
from ._base_client import BaseClient
from logging import getLogger
import requests

logger = getLogger(__name__)

class CustomerClient(BaseClient):
    def create(self, customer: Customer) -> Customer:
        logger.debug(f"Creating customer with URL: {BASE_URL}/customer/create")
        response = self._request(f"{BASE_URL}/customer/create", method="POST", json=customer.model_dump())

        try:
            if response.status_code == 200:
                return Customer.from_dict(data=response.json()["data"])
            else:
                raise_for_status(response)
        except requests.exceptions.Timeout:
            raise APITimeoutError(request=response)
        except requests.exceptions.ConnectionError:
            raise APIConnectionError(message="Connection error", request=response)


    def list(self) -> list[Customer]:
      logger.debug(f"Listing customers with URL: {BASE_URL}/customer/list")
      response = self._request(f"{BASE_URL}/customer/list", method="GET")
      try:
          if response.status_code == 200:
              return [Customer.from_dict(data=bill) for bill in response.json()["data"]]
          else:
              raise_for_status(response)
      except requests.exceptions.Timeout:
          raise APITimeoutError(request=response)
      except requests.exceptions.ConnectionError:
          raise APIConnectionError(message="Connection error", request=response)
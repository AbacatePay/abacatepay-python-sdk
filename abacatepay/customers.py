from ._constants import (
    BASEURL,
    BILLING_KINDS,
    BILLING_METHODS,
)
from .utils._exceptions import *
from .models import Customer
from ._base_client import BaseClient
from logging import getLogger

logger = getLogger(__name__)

class CustomerClient(BaseClient):
    def create(self, customer: Customer) -> Customer:
        logger.debug(f"Creating customer with URL: {BASEURL}/customer/create")
        response = self._request(f"{BASEURL}/customer/create", method="POST", json=customer.model_dump())

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
      logger.debug(f"Listing customers with URL: {BASEURL}/customer/list")
      response = self._request(f"{BASEURL}/customer/list", method="GET")
      try:
          if response.status_code == 200:
              return [Customer.from_dict(data=bill) for bill in response.json()["data"]]
          else:
              raise_for_status(response)
      except requests.exceptions.Timeout:
          raise APITimeoutError(request=response)
      except requests.exceptions.ConnectionError:
          raise APIConnectionError(message="Connection error", request=response)
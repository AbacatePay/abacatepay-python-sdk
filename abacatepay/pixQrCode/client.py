from logging import getLogger
from typing import Any

from ..base.client import BaseClient
from ..constants import BASE_URL
from ..utils.helpers import prepare_data
from .models import PixQrCode, PixQrCodeIn, PixStatus

logger = getLogger(__name__)


class PixQrCodeClient(BaseClient):
    def create(self, data: PixQrCodeIn | dict[str, Any], **kwargs: Any) -> PixQrCode:
        """
        Create a new Pix QR Code.

        Args:
            amount (int): The amount to be paid in cents.
            expires_in (int, optional): The expiration time in seconds.
                Defaults to None.
            description (str, optional): A description for the Pix QR Code.
                Defaults to None.
            customer (CustomerMetadata | dict, optional): Customer information.
                Defaults to None.
        Returns:
            PixQrCode: The created Pix QR Code object.
        """
        json_data = prepare_data(data or kwargs, PixQrCodeIn)
        logger.debug('Creating Pix QR Code: %s', json_data)

        response = self._request(
            f'{BASE_URL}/pixQrCode/create',
            method='POST',
            json=json_data,
        )
        logger.debug('Pix QR Code created successfully: %s', response.json())
        return PixQrCode.model_validate(response.json()['data'])

    def check(self, id: str) -> PixStatus:
        """
        Get the status of a Pix QR Code.

        Args:
            ID (str): The unique identifier of the Pix QR Code.

        Returns:
            PixStatus: The status of the Pix QR Code.
        """
        logger.debug(f'Getting status for Pix QR Code ID: {id}')
        response = self._request(
            f'{BASE_URL}/pixQrCode/check?id={id}',
            method='GET',
        )
        return PixStatus.model_validate(response.json()['data'])

    def simulate(self, id: str, metadata: dict[str, Any] | None = None) -> PixQrCode:
        """
        Simulate a Pix QR Code.

        Args:
            id (str): The unique identifier of the Pix QR Code.
            metadata (dict, optional): Additional metadata for the simulation.
                Defaults to {}.

        Returns:
            PixQrCode: The simulated Pix QR Code object.
        """
        logger.debug(f'Simulating Pix QR Code ID: {id}')
        response = self._request(
            f'{BASE_URL}/pixQrCode/simulate-payment?id={id}',
            method='POST',
            json=metadata or {},
        )
        return PixQrCode.model_validate(response.json()['data'])

from logging import getLogger
from typing import Any

from ..base.client import BaseClient
from ..constants import BASE_URL
from ..utils.helpers import prepare_data
from .models import Coupon, CouponIn

logger = getLogger(__name__)


class CouponClient(BaseClient):
    def create(self, data: CouponIn | dict[str, Any] | None = None, **kwargs: Any) -> Coupon:
        """
        Create a new coupon.

        Args:
            data (Coupon): an instance of `abacatepay.coupons.models.Coupon` a dict
                or the named params following the model schema.

        Keyword args:
            code (str): The unique code for the coupon.
            discount_kind (DISCOUNT_KINDS): The type of discount (e.g., percentage
                or fixed amount).
            discount (int): The value of the discount.
            notes (Optional[str]): A description or note about the coupon. Defaults
                to None.
                - Serialization alias: 'notes'
                - Example: "Cupom de desconto pro meu público"
            max_redeems (Optional[int]): The maximum number of times the coupon can
                be redeemed.
                Defaults to -1 for unlimited redemptions.
            metadata (Optional[dict]): Additional metadata for the coupon. Defaults
                to None.

        Returns:
            Coupon: The response with the coupon data.
        """
        json_data = prepare_data(data or kwargs, CouponIn)
        logger.debug('creating coupon: %s', json_data)

        response = self._request(
            f'{BASE_URL}/coupon/create',
            method='POST',
            json=json_data,
        )
        logger.debug(f'Response from coupon creation: {response.json()}')
        return Coupon.model_validate(response.json()['data'])

    def list(self) -> list[Coupon]:
        """
        List all coupons.
        Returns:
            list[Coupon]: A list of coupon objects.
        """
        logger.debug(f'Listing coupons with URL: {BASE_URL}/coupon/list')
        response = self._request(f'{BASE_URL}/coupon/list', method='GET')
        data = response.json().get('data', [])

        if not data:
            logger.warning('No coupons found in the response.')
            return []

        return [Coupon.model_validate(item) for item in data]
